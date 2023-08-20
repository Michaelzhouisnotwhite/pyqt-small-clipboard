from collections import deque
import os
from typing import Union
import settings
from PySide6.QtCore import (
    QSize,
    Qt,
    QThread,
    QEvent,
    Signal,
    Slot,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    QObject,
    QAbstractItemModel,
)
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, QMouseEvent, QFocusEvent
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QLayout,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QLabel,
    QSystemTrayIcon,
    QTreeWidgetItemIterator,
)

import pickle


class ClipBoardItemRecorder:
    def __init__(self, max_len=99999, item_height=150, top_duplicate=False):
        super().__init__()
        self.item_height = item_height
        self.list_data = deque(maxlen=max_len)
        self.model = QStandardItemModel()
        self.top_duplicate = top_duplicate

    def load(self, cur_width: int):
        if not os.path.exists(settings.LOCAL_STORAGE):
            return
        with open(settings.LOCAL_STORAGE, "rb") as f:
            self.clear()
            history_data: list = pickle.load(f)
            history_data.reverse()
            for data in history_data:
                self.insert(data, cur_width)

    def delete(self, idx):
        item = self.model.takeItem(idx, 0)
        self.list_data.remove(item.text())

    def save(self):
        os.makedirs(os.path.abspath(os.path.dirname(settings.LOCAL_STORAGE)), exist_ok=True)
        with open(settings.LOCAL_STORAGE, "wb") as f:
            pickle.dump(self.list_data, f)

    def insert(self, content: str, cur_width: int) -> bool:
        if content in self.list_data:
            if self.top_duplicate:
                self.list_data.remove(content)
                self.list_data.appendleft(content)
            else:
                return
        else:
            self.list_data.appendleft(content)

        cur_model_row_count = self.model.rowCount()
        for i, data in enumerate(self.list_data):
            if i < cur_model_row_count:
                item = self.model.item(i, 0)
                item.setText(data)
            else:
                item = QStandardItem(data)
                item.setSizeHint(QSize(cur_width, self.item_height))
                self.model.appendRow(item)

    def clear(self):
        self.model.clear()
        self.list_data.clear()
