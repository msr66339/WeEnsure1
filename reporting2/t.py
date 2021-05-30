import numpy as np
import cv2, time

from PySide6 import QtWidgets, QtGui, QtCore
from Users import Users
WINDOW_SIZE = 0;
from PySide6.QtWidgets import QMainWindow
from ui_myui import startup
from real_time_face_recognition import *
class Ui_MainWindow(QMainWindow):
    def setupUi(self,MainWindow,cr):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 497)
        MainWindow.setStyleSheet("QLabel{\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "rgb(255, 255, 255)\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("QFrame{\n"
                                       "    border-bottom: 1px solid #000;\n"
                                       "    \n"
                                       "    background-color: rgb(0, 0, 0);\n"
                                       "}")
        self.main_header.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(self.main_header)
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
                                            "    background-color: #000;\n"
                                            "}\n"
                                            "QPushButton{\n"
                                            "    padding: 5px 10px;\n"
                                            "    border: none;\n"
                                            "    border-radius: 5px;\n"
                                            "    background-color: #000;\n"
                                            "    color: #fff;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(0, 92, 157);\n"
                                            "}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_menu_toggle_btn = QtWidgets.QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.left_menu_toggle_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_toggle_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QtCore.QSize(24, 24))
        self.left_menu_toggle_btn.setObjectName("left_menu_toggle_btn")
        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(self.tittle_bar_container)
        self.tittle_bar.setStyleSheet("QLabel{\n"
                                      "    color: #fff;\n"
                                      "}")
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.tittle_bar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)

        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
                                          "    background-color: #000;\n"
                                          "}\n"
                                          "QPushButton{\n"
                                          "    padding: 20px 10px;\n"
                                          "    border: none;\n"
                                          "    border-radius: 10px;\n"
                                          "    background-color: #000;\n"
                                          "    color: #fff;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(0, 92, 157);\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color:  rgb(0, 92, 157);\n"
                                          "    border-bottom: 2px solid rgb(255, 165, 24);\n"
                                          "}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_menu_top_buttons = QtWidgets.QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.accounts_button = QtWidgets.QPushButton(self.left_menu_top_buttons)

        self.accounts_button.setMinimumSize(QtCore.QSize(100, 0))
        self.accounts_button.setStyleSheet("background-image: url(icons/home.svg);\n"
                                           "background-repeat: none;\n"
                                           "padding-left: 50px;\n"
                                           "background-position: center left;")
        self.accounts_button.setObjectName("accounts_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.accounts_button)
        self.home_button = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.home_button.setMinimumSize(QtCore.QSize(100, 0))
        self.home_button.setStyleSheet("background-image: url(icons/user.svg);\n"
                                       "background-repeat: none;\n"
                                       "padding-left: 50px;\n"
                                       "background-position: center left;")
        self.home_button.setObjectName("home_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.home_button)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)

        self.reports_button = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.reports_button.setMinimumSize(QtCore.QSize(100, 0))
        self.reports_button.setStyleSheet("background-image: url(icons/edit.svg);\n"
                                       "background-repeat: none;\n"
                                       "padding-left: 50px;\n"
                                       "background-position: center left;")
        self.home_button.setObjectName("reports_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.reports_button)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)


        self.settings_button = QtWidgets.QPushButton(self.left_side_menu)
        self.settings_button.setMinimumSize(QtCore.QSize(100, 0))
        self.settings_button.setStyleSheet(                                        "background-repeat: none;\n"
                                           "padding-left: 50px;\n"
                                           "background-position: center left;")
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_3.addWidget(self.settings_button)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("")
        self.home_page.setObjectName("home_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.home_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rightsideframe = QtWidgets.QFrame(self.frame)
        self.rightsideframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightsideframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightsideframe.setObjectName("rightsideframe")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.rightsideframe)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_16 = QtWidgets.QFrame(self.rightsideframe)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_16.setMinimumWidth(300)
        self.label_11 = QtWidgets.QLabel(self.frame_16)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_16)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_16)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame_16)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_11.addWidget(self.label_14)
        self.horizontalLayout_11.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.rightsideframe)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")

        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.frame_18)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.verticalLayout_12.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_16 = QtWidgets.QLabel(self.frame_19)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        self.verticalLayout_12.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_17)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_21.setMaximumWidth(200)
        self.label_17 = QtWidgets.QLabel(self.frame_21)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.horizontalLayout_14.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_7.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/cil-pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_13.addWidget(self.pushButton_7)
        self.horizontalLayout_14.addWidget(self.frame_22)
        self.verticalLayout_12.addWidget(self.frame_20)
        self.frame_23 = QtWidgets.QFrame(self.frame_17)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.frame_24.setMaximumWidth(200)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.frame_24)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.horizontalLayout_16.addWidget(self.frame_24)
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_14.addWidget(self.pushButton_8)
        self.horizontalLayout_16.addWidget(self.frame_25)
        self.verticalLayout_12.addWidget(self.frame_23)
        self.horizontalLayout_11.addWidget(self.frame_17)
        self.horizontalLayout_7.addWidget(self.rightsideframe)
        self.verticalLayout_7.addWidget(self.frame)
        self.stackedWidget.addWidget(self.home_page)
        self.cameramanagement = QtWidgets.QWidget()
        self.cameramanagement.setStyleSheet("")
        self.cameramanagement.setObjectName("cameramanagement")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.cameramanagement)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.cameramanagement)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("camera 2")
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/cil-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/cil-trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.horizontalLayout_6.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.cameramanagement)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 49, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.cameramanagement)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setStyleSheet("")
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.settings_page)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.settings_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow,cr)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def mousePressEvent(self, event):

        self.clickPosition = event.globalPos()


    def moveWindow(self):
        print("s")
    def moveWindow1(self):
        camera_source = 0  # can be also the path of a clip
        pb_path = r"pb_model_select_num=15.pb"
        node_dict = {'input': 'input:0',
                     'keep_prob': 'keep_prob:0',
                     'phase_train': 'phase_train:0',
                     'embeddings': 'embeddings:0',
                     }
        # ref_dir = r"F:\dataset\CASIA\test_database_4"
        ref_dir = r"D:\Casia\test"
        stream(pb_path, node_dict, ref_dir, camera_source=camera_source, resolution="720", to_write=False,
               save_dir=None)

    def editemail(self):
        self.label_17.deleteLater()
        self.this=QtWidgets.QLineEdit(self.frame_21)
        self.this.setText(self.label_17.text())
        self.this.setMaximumWidth(200)
        self.horizontalLayout_15.addWidget(self.this)
        self.pushButton_7.deleteLater()
        self.thiss=QtWidgets.QPushButton(self.frame_22)
        self.thiss.setText("text")
        self.verticalLayout_13.addWidget(self.thiss)



    def editpassword(self):
        self.label_18.deleteLater()
        self.thisss = QtWidgets.QLineEdit(self.frame_24)
        self.horizontalLayout_17.addWidget(self.thisss)
        self.thisss.setText(self.label_18.text())
        self.thisss.setMaximumWidth(200)
        self.pushButton_8.deleteLater()
        self.thissss = QtWidgets.QPushButton(self.frame_25)
        self.thissss.setText("Button")
        self.verticalLayout_14.addWidget(self.thissss)

    def retranslateUi(self, MainWindow,cr):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "WE ENSURE"))
        self.accounts_button.setText(_translate("MainWindow", "ACCOUNT"))
        self.home_button.setText(_translate("MainWindow", "HOME"))
        self.settings_button.setText(_translate("MainWindow", "SETTINGS"))
        self.label_11.setText(_translate("MainWindow", "Name"))
        self.label_12.setText(_translate("MainWindow", "CNIC"))
        self.label_13.setText(_translate("MainWindow", "Email"))
        self.label_14.setText(_translate("MainWindow", "Password"))
        self.label_15.setText(_translate("MainWindow", cr["name"]))
        self.label_16.setText(_translate("MainWindow", cr["CNIC"]))
        self.label_17.setText(_translate("MainWindow", cr["Email"]))
        self.label_18.setText(_translate("MainWindow", cr["Password"]))
        self.comboBox.setItemText(0, _translate("MainWindow", "camera 0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "camera 1"))
        self.label.setText(_translate("MainWindow", "Location:"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Setttings Page"))
        self.home_button.clicked.connect(lambda:self.moveWindow())
        self.accounts_button.clicked.connect(lambda:self.moveWindow1())
        self.pushButton_7.clicked.connect(lambda:self.editemail())
        self.pushButton_8.clicked.connect(lambda: self.editpassword())
        self.reports_button.clicked.connect(lambda: self.repp())
    def repp(self):
        startup()


    #     self.comboBox.activated.connect(self.showcam())
    #
    #
    #
    # def showcam(self):
    #     self.comboBox.currentData()
    #
    #
    #
    #
    #     video1=cv2.VideoCapture(0)
    #
    #     while True:
    #         ret0, frame1 = video1.read()
    #
    #         if (ret0):
    #             cv2.imshow("camera 1", frame1)
    #
    #         if cv2.waitKey(1) & 0xFF==ord('q'):
    #             break
    #
    #     video1.release()
    #     cv2.destroyAllWindows()




class start:
    def __init__(self,cr):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow,cr)
        MainWindow.show()
        sys.exit(app.exec_())
