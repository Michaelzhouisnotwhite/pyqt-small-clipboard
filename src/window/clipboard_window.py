import os
from typing import Optional, Union, Callable
import settings
import pyperclip
from resources.ui_clipboard_list import Ui_MainWindow
from .clipboard_item_recorder import ClipBoardItemRecorder
import pickle


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
from PySide6.QtGui import (
    QIcon,
    QStandardItemModel,
    QStandardItem,
    QMouseEvent,
    QFocusEvent,
    QAction,
)
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
    QMenu,
    QHeaderView,
    QAbstractItemView,
    QLabel,
    QSystemTrayIcon,
    QTreeWidgetItemIterator,
)
from .clipboard_listener import ClipBoardListener


class Program(QMainWindow):
    def __init__(self) -> None:
        self.tray_btn_view = ClipBoardTrayBtn(self.onTrayIconActivated)
        self.cw = ClipBoardWindow()
        self.clipboard_listener = ClipBoardListener()
        self.clipboard_listener.start()
        self.clipboard_listener.new_content.connect(self.cw.add_item)

    def show(self):
        self.clipboard_listener.start()
        self.cw.show()
        self.tray_btn_view.show()

    def onTrayIconActivated(self, reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            # self.cw = ClipBoardWindow()
            self.cw.show()


class ClipBoardTrayBtn(QSystemTrayIcon):
    def __init__(self, onTrayIconActivated: Callable):
        super().__init__()
        self.setIcon(QIcon(os.path.join(settings._WORKSPACE_, "icon.png")))
        self.setToolTip("open clipboard")
        self.activated.connect(onTrayIconActivated)


class ClipBoardWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.clipboard_main_window = Ui_MainWindow()
        # print(self.winId())
        self.clipboard_main_window.setupUi(self)
        self.clipboard_main_window.listView.clicked.connect(self.onlistViewClicked)
        self.clipboard_main_window.listView.doubleClicked.connect(self.onlistViewDoubleClicked)
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)

        self.clipboard_item_recorder = ClipBoardItemRecorder(item_height=100)
        self.clipboard_item_recorder.load(self.clipboard_main_window.listView.width())
        self.clipboard_main_window.listView.setModel(self.clipboard_item_recorder.model)

        self.clipboard_main_window.listView.setMouseTracking(True)
        self.get_list_view().setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.get_list_view().customContextMenuRequested.connect(self.listWidgetContext)

    def listWidgetContext(self, position):
        pop_menu = QMenu()
        del_action = QAction("删除项目")

        pop_menu.addAction(del_action)
        # pop_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        # self.setFocus()
        del_action.triggered.connect(self.delete_item)
        pop_menu.exec(self.get_list_view().mapToGlobal(position))

    def delete_item(self):
        # print(self.get_list_view().currentIndex().row())
        self.clipboard_item_recorder.delete(self.get_list_view().currentIndex().row())
        ...

    def get_list_view(self):
        return self.clipboard_main_window.listView

    def onlistViewDoubleClicked(self, idx: QModelIndex):
        pyperclip.copy(self.clipboard_item_recorder.model.item(idx.row(), idx.column()).text())

    def focusInEvent(self, event: QFocusEvent) -> None:
        ...

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event == QEvent.Type.FocusOut:
            ...
        return super().eventFilter(watched, event)

    def focusOutEvent(self, event: QFocusEvent) -> None:
        if event.reason() == Qt.FocusReason.PopupFocusReason:
            return
        print(event.reason().name)
        self.hide()
        self.close()
        # self.destroy(True, True)
        # return super().focusOutEvent(event)

    def debug_item(self):
        content1 = """
       self.clipboard_main_window.listView.setModel(self.list_view_model)
        self.clipboard_main_window.listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # self.clipboard_main_window.listView.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.clipboard_main_window.listView.setMouseTracking(True)
        self.clipboard_main_window.listView.setWordWrap(True)
        # self.clipboard_main_window.listView.setWrapping(True)
        # self.clipboard_main_window.listView.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.centralWidget().setMouseTracking(True)
        self.setMouseTracking(True)
        self.clipboard_main_window.listView.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.clipboard_listener = ListenClipBoard(self)
        self.clipboard_listener.new_content.connect(self.add_item)
        # self.setStyle(QStyleFactory.create('Fusion'))
        self.window_show=False
                                                     """

        content2 = """
        self.clipboard_listener.new_content.connect(self.add_item)
        # self.setStyle(QStyleFactory.create('Fusion'))
        self.window_show = False
        self.mouse_pos = (10, 10)
                                                     """
        self.clipboard_item_recorder.insert(content1, self.clipboard_main_window.listView.width())
        self.clipboard_item_recorder.insert(content2, self.clipboard_main_window.listView.width())

    def close(self) -> bool:
        # self.clipboard_listener.close()
        self.clipboard_item_recorder.save()
        return super().close()

    @Slot(str)
    def add_item(self, clipboard_content):
        self.clipboard_item_recorder.insert(
            clipboard_content, self.clipboard_main_window.listView.width()
        )

    def onlistViewClicked(self, model_index: QModelIndex):
        ...

    def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None:
        print("call destroy")
        return super().destroy(destroyWindow, destroySubWindows)
