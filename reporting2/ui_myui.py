# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myuiLbVfFK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Reports import Report
from emaail import Ui_MainWindow as emailmain



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 487)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
        "border:none;\n"
        "background-color:rgb(25,25,25);\n"
        "}\n"
        "QLabel{\n"
        "color:#FFFFFF\n"
        "}")

        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.pending=False
        self.shadow=QGraphicsDropShadowEffect(MainWindow)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))
        self.centralwidget.setGraphicsEffect(self.shadow)
        self.selecteditem=0
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sliderContainer = QFrame(self.centralwidget)
        self.sliderContainer.setObjectName(u"sliderContainer")
        self.sliderContainer.setMaximumSize(QSize(200, 16777215))
        self.sliderContainer.setFrameShape(QFrame.StyledPanel)
        self.sliderContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sliderContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sliderMenu = QFrame(self.sliderContainer)
        self.sliderMenu.setObjectName(u"sliderMenu")
        self.sliderMenu.setMinimumSize(QSize(198, 442))
        self.sliderMenu.setMaximumSize(QSize(196, 16777215))
        self.sliderMenu.setFrameShape(QFrame.StyledPanel)
        self.sliderMenu.setFrameShadow(QFrame.Raised)
        self.sliderMenu.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.verticalLayout_3 = QVBoxLayout(self.sliderMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.sliderMenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(QFont.weight(font))
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap("icons/aperture.svg"))

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.sliderMenu)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pendingRbtn = QPushButton(self.frame_4)
        self.pendingRbtn.setObjectName(u"pendingRbtn")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(QFont.weight(font))
        self.pendingRbtn.setFont(font1)
        self.pendingRbtn.setStyleSheet(u"color:#ffffff\n"
"")
        self.reports=Report()
        icon = QIcon()
        icon.addFile("icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pendingRbtn.setIcon(icon)
        self.pendingRbtn.setIconSize(QSize(20, 20))
        self.pendingRbtn.setFlat(True)

        self.verticalLayout_6.addWidget(self.pendingRbtn)

        self.allRbtn = QPushButton(self.frame_4)
        self.allRbtn.setObjectName(u"allRbtn")
        self.allRbtn.setFont(font1)
        self.allRbtn.setAutoFillBackground(False)
        self.allRbtn.setStyleSheet(u"color:#ffffff\n"
"")
        icon1 = QIcon()
        icon1.addFile("icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.allRbtn.setIcon(icon1)
        self.allRbtn.setIconSize(QSize(20, 20))
        self.allRbtn.setFlat(True)

        self.verticalLayout_6.addWidget(self.allRbtn)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.sliderMenu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(QFont.weight(font2))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"color:#ffffff\n"
"")
        icon2 = QIcon()
        icon2.addFile("icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setFlat(True)

        self.verticalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.sliderMenu)


        self.horizontalLayout.addWidget(self.sliderContainer)

        self.listFrame = QFrame(self.centralwidget)
        self.listFrame.setObjectName(u"listFrame")
        self.listFrame.setMaximumSize(QSize(250, 16777215))
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.listFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.listFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(QFont.weight(font3))
        self.label_9.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_9)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.listFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 300, 600))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_12.addWidget(self.pushButton_9)

        #list view deleted from here
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName("listWidget")



        self.verticalLayout_12.addWidget(self.listWidget)
        self.setList()
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.listWidget.doubleClicked.connect(lambda : self.listviewClick())


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.listFrame)

        self.view = QFrame(self.centralwidget)
        self.view.setObjectName(u"view")
        self.view.setFrameShape(QFrame.StyledPanel)
        self.view.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.view)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.view)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile("icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(25, 30))
        self.pushButton_4.setFlat(True)

        self.verticalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(130, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizebtn = QPushButton(self.frame)
        self.minimizebtn.setObjectName(u"minimizebtn")
        self.minimizebtn.setMaximumSize(QSize(25, 16777215))
        icon4 = QIcon()
        icon4.addFile("icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizebtn.setIcon(icon4)
        self.minimizebtn.setIconSize(QSize(25, 25))
        self.minimizebtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.minimizebtn)

        self.restorebtn = QPushButton(self.frame)
        self.restorebtn.setObjectName(u"restorebtn")
        self.restorebtn.setMaximumSize(QSize(25, 16777215))
        icon5 = QIcon()
        icon5.addFile("icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restorebtn.setIcon(icon5)
        self.restorebtn.setIconSize(QSize(25, 25))
        self.restorebtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.restorebtn)

        self.crossbtn = QPushButton(self.frame)
        self.crossbtn.setObjectName(u"crossbtn")
        self.crossbtn.setMaximumSize(QSize(25, 16777215))
        icon6 = QIcon()
        icon6.addFile("icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.crossbtn.setIcon(icon6)
        self.crossbtn.setIconSize(QSize(25, 25))
        self.crossbtn.setFlat(True)
        self.crossbtn.clicked.connect(lambda: self.closes(MainWindow))

        self.horizontalLayout_4.addWidget(self.crossbtn)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main = QFrame(self.view)
        self.main.setObjectName(u"main")
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.main)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setMinimumSize(QSize(200, 100))
        font4 = QFont()
        font4.setKerning(True)
        self.label_8.setFont(font4)
        self.label_8.setPixmap(QPixmap(u"125437182_3421292957992477_3870826436494938711_n.jpg"))
        self.label_8.setIndent(0)

        self.verticalLayout_10.addWidget(self.label_8)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.main)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(QFont.weight(font5))
        self.label_3.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_7)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_13.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_13.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_13.addWidget(self.label_14)


        self.horizontalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.main)

        self.footer = QFrame(self.view)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon7 = QIcon()
        icon7.addFile("icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon8 = QIcon()
        icon8.addFile("icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon9 = QIcon()
        icon9.addFile("icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        QSizeGrip(self.sizeGrip)

        self.horizontalLayout_3.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.view)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_7.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"We Ensure", None))
        self.label_2.setText("")
        self.pendingRbtn.setText(QCoreApplication.translate("MainWindow", u"MISSED", None))
        self.allRbtn.setText(QCoreApplication.translate("MainWindow", u"FULL list", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText("")
        self.minimizebtn.setText("")
        self.restorebtn.setText("")
        self.crossbtn.setText("")
        self.label_8.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fathers Name:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Registration:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Section:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Camera Location:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_7.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.minimizebtn.clicked.connect(lambda: self.minimize(MainWindow))
        self.restorebtn.clicked.connect(lambda: self.restore(MainWindow))
        self.pushButton_6.clicked.connect(lambda: self.deleteBtnClick())
        self.pendingRbtn.clicked.connect(lambda: self.setMissedList())
        self.allRbtn.clicked.connect(lambda: self.setList())
        self.pushButton_7.clicked.connect(lambda: self.emailWindow())

    def emailWindow(self):
        print(self.selecteditem)
        for i in range(len(self.reports.reportss)):
            if self.reports.reportss[i]['id'] == self.selecteditem:
                cr=self.reports.reportss[i]
                break
        self.emailw=emailmain(cr)
        self.emailw.show()




    def deleteBtnClick(self):
        self.reports.deleteReport(self.selecteditem)
        if self.pending==True:
            self.setMissedList()
        else:
            self.setList()

    def listviewClick(self):
        print(self.listWidget.currentItem().text())
        self.selecteditem = int(self.listWidget.currentItem().text())
        self.showReportData()

    def closes(self,window):
        window.close()

    def showReportData(self):
        for i in range(len(self.reports.reportss)):
            if self.reports.reportss[i]['id'] == self.selecteditem:
                cr=self.reports.reportss[i]
                break
        self.label_8.setPixmap(cr["img"])
        self.label_10.setText(cr["name"])
        self.label_11.setText(cr["FathersName"])
        self.label_12.setText(cr["registration"])
        self.label_13.setText(cr["section"])
        self.label_14.setText(cr["Location"])


    def minimize(self,window):
        window.showMinimized()

    def restore(self,window):
        if window.isMaximized():
            window.showNormal()
            self.restorebtn.setIcon(QIcon("icons/maximize-2.svg"))
        else:
            window.showMaximized()
            self.restorebtn.setIcon(QIcon("icons/minimize-2.svg"))

    def setMissedList(self):
        self.pending=True
        self.listWidget.clear()
        for i in range(len(self.reports.reportss)):
            if self.reports.reportss[i]["type"]=="mis":
                item = QtWidgets.QListWidgetItem()
                item.setText(str(self.reports.reportss[i]["id"]))
                item.setForeground(Qt.white)
                self.listWidget.addItem(item)

    def setList(self):
        self.pending=False
        self.listWidget.clear()
        for i in range(len(self.reports.reportss)):
            item = QtWidgets.QListWidgetItem()
            item.setText(str(self.reports.reportss[i]["id"]))
            item.setForeground(Qt.white)
            self.listWidget.addItem(item)

class startup:
    def __init__(self):
        import sys

        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()




    # retranslateUi

