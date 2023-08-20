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
    QAbstractItemView,
    QWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QLabel,
    QSystemTrayIcon,
    QTreeWidgetItemIterator,
)
from typing import Optional
import pyperclip

class ClipBoardListener(QThread):
    new_content = Signal(str)

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.stop = False

    def run(self) -> None:
        while not self.stop:
            try:
                content = pyperclip.waitForNewPaste(1)
                self.new_content.emit(content)
            except pyperclip.PyperclipTimeoutException:
                ...

    def close(self):
        self.stop = True
