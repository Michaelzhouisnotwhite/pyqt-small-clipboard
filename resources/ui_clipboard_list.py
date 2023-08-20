# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_clipboard_list.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QListView, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)
from . import font_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(374, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(374, 459))
        MainWindow.setMaximumSize(QSize(374, 459))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.mw_vlayout = QWidget(MainWindow)
        self.mw_vlayout.setObjectName(u"mw_vlayout")
        self.verticalLayout_2 = QVBoxLayout(self.mw_vlayout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(self.mw_vlayout)
        self.listView.setObjectName(u"listView")
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(10)
        self.listView.setFont(font)
        self.listView.setMouseTracking(True)
        self.listView.setFocusPolicy(Qt.NoFocus)
        self.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setTabKeyNavigation(True)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setViewMode(QListView.ListMode)
        self.listView.setWordWrap(False)
        self.listView.setSelectionRectVisible(True)

        self.verticalLayout_2.addWidget(self.listView)

        MainWindow.setCentralWidget(self.mw_vlayout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

