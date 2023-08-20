import sys
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
from PySide6.QtCore import QAbstractAnimation
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, QMouseEvent
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
    QTreeWidgetItemIterator,
)
import PySide6.QtCore
from window.clipboard_window import ClipBoardWindow, ClipBoardTrayBtn, Program
from PySide6.QtWidgets import QApplication


class GlobalApp(QApplication):
    # def __init__(self, *args):
    #     super().__init__(*args)

    def notify(self, obj: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.MouseMove:
            ...
        return super().notify(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = ClipBoardWindow()
    # window.show()
    program = Program()
    program.show()
    sys.exit(app.exec())
