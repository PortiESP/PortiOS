# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'centralnCUPNC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Central(object):
    def setupUi(self, Central):
        if not Central.objectName():
            Central.setObjectName(u"Central")
        Central.resize(800, 480)
        self.centralwidget = QWidget(Central)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_logo = QFrame(self.centralwidget)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setGeometry(QRect(315, 400, 170, 30))
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.frame_logo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setPixmap(QPixmap(u":/styles/Resources/porti_os.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_logo)

        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 800, 70))
        self.frame_header.setMinimumSize(QSize(800, 70))
        self.frame_header.setMaximumSize(QSize(800, 70))
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.header_background = QLabel(self.frame_header)
        self.header_background.setObjectName(u"header_background")
        self.header_background.setGeometry(QRect(0, 0, 800, 70))
        self.header_background.setMinimumSize(QSize(800, 70))
        self.header_background.setMaximumSize(QSize(800, 70))
        self.header_background.setPixmap(QPixmap(u":/styles/Resources/header_red.png"))
        self.header_background.setScaledContents(True)
        self.label_clock = QLabel(self.frame_header)
        self.label_clock.setObjectName(u"label_clock")
        self.label_clock.setGeometry(QRect(325, 0, 150, 50))
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_clock.setFont(font)
        self.label_clock.setStyleSheet(u"color:rgb(255,0,0);")
        self.label_clock.setAlignment(Qt.AlignCenter)
        self.bluetoothStatusButton = QPushButton(self.frame_header)
        self.bluetoothStatusButton.setObjectName(u"bluetoothStatusButton")
        self.bluetoothStatusButton.setGeometry(QRect(459, 10, 24, 24))
        self.bluetoothStatusButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons-gray/Resources/Icons/bt_states/bluetooth_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bluetoothStatusButton.setIcon(icon)
        self.bluetoothStatusButton.setIconSize(QSize(22, 22))
        self.frame_footer = QFrame(self.centralwidget)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setGeometry(QRect(0, 410, 800, 430))
        palette = QPalette()
        self.frame_footer.setPalette(palette)
        self.frame_footer.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	border:none;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.frame_footer.setFrameShape(QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.footer_i = QFrame(self.frame_footer)
        self.footer_i.setObjectName(u"footer_i")
        self.footer_i.setGeometry(QRect(0, 20, 260, 50))
        self.footer_i.setMinimumSize(QSize(260, 50))
        self.footer_i.setMaximumSize(QSize(260, 30))
        self.footer_i.setFrameShape(QFrame.NoFrame)
        self.footer_i.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.footer_i)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.footerButton_1 = QPushButton(self.footer_i)
        self.footerButton_1.setObjectName(u"footerButton_1")
        self.footerButton_1.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light Condensed")
        font1.setPointSize(8)
        self.footerButton_1.setFont(font1)
        self.footerButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_1.setMouseTracking(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-angle-double-small-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_1.setIcon(icon1)
        self.footerButton_1.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.footerButton_1)

        self.footerButton_2 = QPushButton(self.footer_i)
        self.footerButton_2.setObjectName(u"footerButton_2")
        self.footerButton_2.setMinimumSize(QSize(0, 50))
        self.footerButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons_red/Resources/Icons/png-red/play-fill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_2.setIcon(icon2)
        self.footerButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.footerButton_2)

        self.footerButton_3 = QPushButton(self.footer_i)
        self.footerButton_3.setObjectName(u"footerButton_3")
        self.footerButton_3.setMinimumSize(QSize(0, 50))
        self.footerButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-angle-double-small-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_3.setIcon(icon3)
        self.footerButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.footerButton_3)

        self.footer_d = QFrame(self.frame_footer)
        self.footer_d.setObjectName(u"footer_d")
        self.footer_d.setGeometry(QRect(540, 20, 260, 50))
        self.footer_d.setMinimumSize(QSize(260, 50))
        self.footer_d.setMaximumSize(QSize(260, 50))
        self.footer_d.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_d)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.footerButton_4 = QPushButton(self.footer_d)
        self.footerButton_4.setObjectName(u"footerButton_4")
        self.footerButton_4.setMinimumSize(QSize(0, 50))
        self.footerButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons_red/Resources/Icons/png-red/icons-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_4.setIcon(icon4)
        self.footerButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.footerButton_4)

        self.footerButton_5 = QPushButton(self.footer_d)
        self.footerButton_5.setObjectName(u"footerButton_5")
        self.footerButton_5.setMinimumSize(QSize(0, 50))
        self.footerButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons_red/Resources/Icons/png-red/levels.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_5.setIcon(icon5)
        self.footerButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.footerButton_5)

        self.footerButton_6 = QPushButton(self.footer_d)
        self.footerButton_6.setObjectName(u"footerButton_6")
        self.footerButton_6.setMinimumSize(QSize(0, 50))
        self.footerButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_6.setIcon(icon6)
        self.footerButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.footerButton_6)

        self.footerButton_6.raise_()
        self.footerButton_5.raise_()
        self.footerButton_4.raise_()
        self.footer_background = QLabel(self.frame_footer)
        self.footer_background.setObjectName(u"footer_background")
        self.footer_background.setGeometry(QRect(0, 0, 800, 70))
        self.footer_background.setPixmap(QPixmap(u":/styles/Resources/footer_red.png"))
        self.footer_background.setScaledContents(True)
        self.footer_background.raise_()
        self.footer_i.raise_()
        self.footer_d.raise_()
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 480))
        self.stackedWidget.setMinimumSize(QSize(800, 480))
        self.stackedWidget.setMaximumSize(QSize(800, 480))
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_player = QWidget()
        self.page_player.setObjectName(u"page_player")
        self.stackedWidget.addWidget(self.page_player)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.stackedWidget.addWidget(self.page_settings)
        self.page_apps = QWidget()
        self.page_apps.setObjectName(u"page_apps")
        self.stackedWidget.addWidget(self.page_apps)
        self.page_leds = QWidget()
        self.page_leds.setObjectName(u"page_leds")
        self.stackedWidget.addWidget(self.page_leds)
        self.frame_volume = QFrame(self.centralwidget)
        self.frame_volume.setObjectName(u"frame_volume")
        self.frame_volume.setGeometry(QRect(652, 234, 40, 180))
        self.frame_volume.setStyleSheet(u"QFrame#frame_volume{\n"
"	\n"
"	background:rgba(57, 57, 57, 200);\n"
"	border-radius:20px;\n"
"\n"
"}")
        self.frame_volume.setFrameShape(QFrame.NoFrame)
        self.frame_volume.setFrameShadow(QFrame.Raised)
        self.slider_volume = QSlider(self.frame_volume)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setGeometry(QRect(5, 25, 30, 130))
        self.slider_volume.setStyleSheet(u"\n"
"QSlider::groove:vertical{\n"
"	width:20px;\n"
"	background:transparent;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"	border:1px solid red;\n"
"	background:red;\n"
"	height:6px;\n"
"	width:20px;\n"
"	margin-left:-3px;\n"
"	margin-right:-3px;\n"
"	border-radius:3px;	\n"
"\n"
"}")
        self.slider_volume.setMaximum(100)
        self.line = QFrame(self.frame_volume)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 25, 1, 130))
        self.line.setStyleSheet(u"border:1px solid gray;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.raise_()
        self.slider_volume.raise_()
        self.frame_background = QFrame(self.centralwidget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setGeometry(QRect(0, 0, 800, 480))
        self.frame_background.setStyleSheet(u"QFrame#frame_background{\n"
"	background:rgb(20,20,20);\n"
"}")
        self.frame_power = QFrame(self.centralwidget)
        self.frame_power.setObjectName(u"frame_power")
        self.frame_power.setGeometry(QRect(0, 0, 800, 480))
        self.frame_power.setStyleSheet(u"background-color: rgba(24, 24, 24, 200);")
        self.frame_powerMenu = QFrame(self.frame_power)
        self.frame_powerMenu.setObjectName(u"frame_powerMenu")
        self.frame_powerMenu.setGeometry(QRect(250, 150, 300, 200))
        self.frame_powerMenu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"\n"
"}\n"
"QPushButton{\n"
"	border:2px solid red;\n"
"	background-color: rgb(159, 159, 159);	\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"	color:white;\n"
"}")
        self.centralRebootButton = QPushButton(self.frame_powerMenu)
        self.centralRebootButton.setObjectName(u"centralRebootButton")
        self.centralRebootButton.setGeometry(QRect(10, 130, 280, 50))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light Condensed")
        font2.setPointSize(11)
        self.centralRebootButton.setFont(font2)
        self.centralShutdownButton = QPushButton(self.frame_powerMenu)
        self.centralShutdownButton.setObjectName(u"centralShutdownButton")
        self.centralShutdownButton.setGeometry(QRect(10, 70, 280, 50))
        self.centralShutdownButton.setFont(font2)
        self.frame_8 = QFrame(self.frame_powerMenu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 300, 60))
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 200, 40))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light Condensed")
        font3.setPointSize(21)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color:white;")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_4 = QFrame(self.frame_8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 50, 280, 2))
        self.line_4.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.powerCloseButton = QPushButton(self.frame_8)
        self.powerCloseButton.setObjectName(u"powerCloseButton")
        self.powerCloseButton.setGeometry(QRect(250, 10, 40, 40))
        self.powerCloseButton.setStyleSheet(u"border:none;\n"
"background:none;")
        icon7 = QIcon()
        icon7.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-cross-small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.powerCloseButton.setIcon(icon7)
        self.powerCloseButton.setIconSize(QSize(30, 30))
        Central.setCentralWidget(self.centralwidget)
        self.frame_power.raise_()
        self.frame_background.raise_()
        self.stackedWidget.raise_()
        self.frame_logo.raise_()
        self.frame_header.raise_()
        self.frame_footer.raise_()
        self.frame_volume.raise_()

        self.retranslateUi(Central)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Central)
    # setupUi

    def retranslateUi(self, Central):
        self.label_clock.setText(QCoreApplication.translate("Central", u"23:23", None))
        self.bluetoothStatusButton.setText("")
        self.footer_background.setText("")
        self.centralRebootButton.setText(QCoreApplication.translate("Central", u"REBOOT", None))
        self.centralShutdownButton.setText(QCoreApplication.translate("Central", u"SHUTDOWN", None))
        self.label_13.setText(QCoreApplication.translate("Central", u"Power", None))
        self.powerCloseButton.setText("")
        pass
    # retranslateUi

