# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ledskoDZZe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Leds_widget(object):
    def setupUi(self, Leds_widget):
        if not Leds_widget.objectName():
            Leds_widget.setObjectName(u"Leds_widget")
        Leds_widget.resize(796, 480)
        self.frame_leds = QFrame(Leds_widget)
        self.frame_leds.setObjectName(u"frame_leds")
        self.frame_leds.setGeometry(QRect(0, 0, 800, 480))
        self.frame_leds.setStyleSheet(u"QFrame#frame_leds{\n"
"	background:rgb(20,20,20);\n"
"}")
        self.frameLeds = QFrame(self.frame_leds)
        self.frameLeds.setObjectName(u"frameLeds")
        self.frameLeds.setGeometry(QRect(60, 70, 250, 250))
        self.frameLeds.setStyleSheet(u"border-radius:125px;")
        self.frameLeds.setFrameShape(QFrame.StyledPanel)
        self.frameLeds.setFrameShadow(QFrame.Raised)
        self.ledsBulb = QFrame(self.frameLeds)
        self.ledsBulb.setObjectName(u"ledsBulb")
        self.ledsBulb.setGeometry(QRect(0, 0, 250, 250))
        self.ledsBulb.setStyleSheet(u"background:black;\n"
"")
        self.ledsOnOffButton = QCheckBox(self.frameLeds)
        self.ledsOnOffButton.setObjectName(u"ledsOnOffButton")
        self.ledsOnOffButton.setGeometry(QRect(95, 95, 60, 60))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold Condensed")
        font.setPointSize(25)
        self.ledsOnOffButton.setFont(font)
        self.ledsOnOffButton.setStyleSheet(u"QCheckBox{\n"
"	border-radius:30px;\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"	border: 2px solid gray;\n"
"	color:gray;\n"
"}\n"
"QCheckBox:checked{\n"
"	border: 2px solid lightGray;\n"
"	color:lightGray;\n"
"	\n"
"\n"
"}\n"
"QCheckBox::indicator {\n"
"	width:18.5px;\n"
"   background:transparent;\n"
"}")
        self.frameLedButtons = QFrame(self.frame_leds)
        self.frameLedButtons.setObjectName(u"frameLedButtons")
        self.frameLedButtons.setGeometry(QRect(50, 340, 700, 40))
        self.frameLedButtons.setStyleSheet(u"QPushButton{\n"
"	background:rgb(94, 94, 94);\n"
"	border:2px solid white;\n"
"	border-radius:20px;\n"
"	color:white;\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.frameLedButtons)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frameLedButtons)
        self.frame_8.setObjectName(u"frame_8")
        self.ledsProgramJumpButton = QPushButton(self.frame_8)
        self.ledsProgramJumpButton.setObjectName(u"ledsProgramJumpButton")
        self.ledsProgramJumpButton.setGeometry(QRect(0, 0, 124, 40))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.ledsProgramJumpButton.setFont(font1)
        self.ledsProgramJumpButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:20px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frameLedButtons)
        self.frame_7.setObjectName(u"frame_7")
        self.ledsProgramFadeButton = QPushButton(self.frame_7)
        self.ledsProgramFadeButton.setObjectName(u"ledsProgramFadeButton")
        self.ledsProgramFadeButton.setGeometry(QRect(0, 0, 124, 40))
        self.ledsProgramFadeButton.setFont(font1)
        self.ledsProgramFadeButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:20px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frameLedButtons)
        self.frame_6.setObjectName(u"frame_6")
        self.ledsProgramRandomButton = QPushButton(self.frame_6)
        self.ledsProgramRandomButton.setObjectName(u"ledsProgramRandomButton")
        self.ledsProgramRandomButton.setGeometry(QRect(0, 0, 124, 40))
        self.ledsProgramRandomButton.setFont(font1)
        self.ledsProgramRandomButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:20px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frameLedButtons)
        self.frame_5.setObjectName(u"frame_5")
        self.ledsProgramFlashButton = QPushButton(self.frame_5)
        self.ledsProgramFlashButton.setObjectName(u"ledsProgramFlashButton")
        self.ledsProgramFlashButton.setGeometry(QRect(0, 0, 124, 40))
        self.ledsProgramFlashButton.setFont(font1)
        self.ledsProgramFlashButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:20px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frameLedButtons)
        self.frame_4.setObjectName(u"frame_4")
        self.ledsProgramPoliceButton = QPushButton(self.frame_4)
        self.ledsProgramPoliceButton.setObjectName(u"ledsProgramPoliceButton")
        self.ledsProgramPoliceButton.setGeometry(QRect(0, 0, 124, 40))
        self.ledsProgramPoliceButton.setFont(font1)
        self.ledsProgramPoliceButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:20px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.frame_4)

        self.frameLedControls = QFrame(self.frame_leds)
        self.frameLedControls.setObjectName(u"frameLedControls")
        self.frameLedControls.setGeometry(QRect(400, 100, 350, 200))
        self.horizontalLayout_4 = QHBoxLayout(self.frameLedControls)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frameLedLabels = QFrame(self.frameLedControls)
        self.frameLedLabels.setObjectName(u"frameLedLabels")
        self.frameLedLabels.setMaximumSize(QSize(60, 16777215))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light")
        self.frameLedLabels.setFont(font2)
        self.frameLedLabels.setStyleSheet(u"color:white;")
        self.verticalLayout = QVBoxLayout(self.frameLedLabels)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frameLedLabels)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight SemiConde")
        font3.setPointSize(13)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frameLedLabels)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frameLedLabels)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frameLedLabels)

        self.frame_3 = QFrame(self.frameLedControls)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	background:transparent;\n"
"	\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	border-radius:5px;\n"
"	width:22px;\n"
"	\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(23)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.ledsSliderRed = QSlider(self.frame_3)
        self.ledsSliderRed.setObjectName(u"ledsSliderRed")
        self.ledsSliderRed.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background:rgb(240, 0, 0 );\n"
"	\n"
"}\n"
"QSlider::sub-page:horizontal{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgb(255, 0, 0 ));\n"
"}")
        self.ledsSliderRed.setMaximum(255)
        self.ledsSliderRed.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.ledsSliderRed)

        self.ledsSliderGreen = QSlider(self.frame_3)
        self.ledsSliderGreen.setObjectName(u"ledsSliderGreen")
        self.ledsSliderGreen.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background:rgb(0, 240, 0 );\n"
"	\n"
"}\n"
"QSlider::sub-page:horizontal{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgb(0, 255, 0 ));\n"
"}")
        self.ledsSliderGreen.setMaximum(255)
        self.ledsSliderGreen.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.ledsSliderGreen)

        self.ledsSliderBlue = QSlider(self.frame_3)
        self.ledsSliderBlue.setObjectName(u"ledsSliderBlue")
        self.ledsSliderBlue.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background:rgb(0, 0, 240);\n"
"	\n"
"}\n"
"QSlider::sub-page:horizontal{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgb(0, 0, 255));\n"
"}")
        self.ledsSliderBlue.setMaximum(255)
        self.ledsSliderBlue.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.ledsSliderBlue)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frameLedValues = QFrame(self.frameLedControls)
        self.frameLedValues.setObjectName(u"frameLedValues")
        self.frameLedValues.setMinimumSize(QSize(30, 0))
        self.frameLedValues.setMaximumSize(QSize(50, 16777215))
        self.frameLedValues.setFont(font2)
        self.frameLedValues.setStyleSheet(u"color:white;")
        self.verticalLayout_4 = QVBoxLayout(self.frameLedValues)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ledsValueRed = QLabel(self.frameLedValues)
        self.ledsValueRed.setObjectName(u"ledsValueRed")
        self.ledsValueRed.setMaximumSize(QSize(16777215, 65))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Light")
        font4.setPointSize(13)
        self.ledsValueRed.setFont(font4)

        self.verticalLayout_4.addWidget(self.ledsValueRed)

        self.ledsValueGreen = QLabel(self.frameLedValues)
        self.ledsValueGreen.setObjectName(u"ledsValueGreen")
        self.ledsValueGreen.setFont(font4)

        self.verticalLayout_4.addWidget(self.ledsValueGreen)

        self.ledsValueBlue = QLabel(self.frameLedValues)
        self.ledsValueBlue.setObjectName(u"ledsValueBlue")
        self.ledsValueBlue.setFont(font4)
        self.ledsValueBlue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.ledsValueBlue)


        self.horizontalLayout_4.addWidget(self.frameLedValues)

        self.frame_footer = QFrame(self.frame_leds)
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
        self.horizontalLayout_2 = QHBoxLayout(self.footer_i)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.footerButton_1 = QPushButton(self.footer_i)
        self.footerButton_1.setObjectName(u"footerButton_1")
        self.footerButton_1.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Light Condensed")
        font5.setPointSize(8)
        self.footerButton_1.setFont(font5)
        self.footerButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_1.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-angle-double-small-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_1.setIcon(icon)
        self.footerButton_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.footerButton_1)

        self.footerButton_2 = QPushButton(self.footer_i)
        self.footerButton_2.setObjectName(u"footerButton_2")
        self.footerButton_2.setMinimumSize(QSize(0, 50))
        self.footerButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons_red/Resources/Icons/png-red/play-fill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_2.setIcon(icon1)
        self.footerButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.footerButton_2)

        self.footerButton_3 = QPushButton(self.footer_i)
        self.footerButton_3.setObjectName(u"footerButton_3")
        self.footerButton_3.setMinimumSize(QSize(0, 50))
        self.footerButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-angle-double-small-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_3.setIcon(icon2)
        self.footerButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.footerButton_3)

        self.footer_d = QFrame(self.frame_footer)
        self.footer_d.setObjectName(u"footer_d")
        self.footer_d.setGeometry(QRect(540, 20, 260, 50))
        self.footer_d.setMinimumSize(QSize(260, 50))
        self.footer_d.setMaximumSize(QSize(260, 50))
        self.footer_d.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_d)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.footerButton_4 = QPushButton(self.footer_d)
        self.footerButton_4.setObjectName(u"footerButton_4")
        self.footerButton_4.setMinimumSize(QSize(0, 50))
        self.footerButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons_red/Resources/Icons/png-red/icons-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_4.setIcon(icon3)
        self.footerButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.footerButton_4)

        self.footerButton_5 = QPushButton(self.footer_d)
        self.footerButton_5.setObjectName(u"footerButton_5")
        self.footerButton_5.setMinimumSize(QSize(0, 50))
        self.footerButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons_red/Resources/Icons/png-red/levels.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_5.setIcon(icon4)
        self.footerButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.footerButton_5)

        self.footerButton_6 = QPushButton(self.footer_d)
        self.footerButton_6.setObjectName(u"footerButton_6")
        self.footerButton_6.setMinimumSize(QSize(0, 50))
        self.footerButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_6.setIcon(icon5)
        self.footerButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.footerButton_6)

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
        self.frame_logo = QFrame(self.frame_leds)
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

        self.frame_header = QFrame(self.frame_leds)
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
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Light Condensed")
        font6.setPointSize(25)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_clock.setFont(font6)
        self.label_clock.setStyleSheet(u"color:rgb(255,0,0);")
        self.label_clock.setAlignment(Qt.AlignCenter)
        self.bluetoothStatusButton = QPushButton(self.frame_header)
        self.bluetoothStatusButton.setObjectName(u"bluetoothStatusButton")
        self.bluetoothStatusButton.setGeometry(QRect(459, 10, 24, 24))
        font7 = QFont()
        font7.setFamily(u"MT Extra")
        self.bluetoothStatusButton.setFont(font7)
        self.bluetoothStatusButton.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/icons-gray/Resources/Icons/bt_states/bluetooth_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bluetoothStatusButton.setIcon(icon6)
        self.bluetoothStatusButton.setIconSize(QSize(22, 22))
        self.frame = QFrame(self.frame_leds)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(545, 70, 200, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamily(u"Bahnschrift SemiLight SemiConde")
        font8.setPointSize(16)
        self.label_4.setFont(font8)
        self.label_4.setFocusPolicy(Qt.ClickFocus)
        self.label_4.setStyleSheet(u"color:white;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ledsColorPickerButton = QPushButton(self.frame)
        self.ledsColorPickerButton.setObjectName(u"ledsColorPickerButton")
        self.ledsColorPickerButton.setMaximumSize(QSize(40, 40))
        self.ledsColorPickerButton.setFocusPolicy(Qt.WheelFocus)
        self.ledsColorPickerButton.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/color_icons/Resources/Icons/color_icons/color_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/color_icons/Resources/Icons/color_icons/color_lightgray.png", QSize(), QIcon.Active, QIcon.Off)
        self.ledsColorPickerButton.setIcon(icon7)
        self.ledsColorPickerButton.setIconSize(QSize(240, 24))

        self.horizontalLayout_5.addWidget(self.ledsColorPickerButton)


        self.retranslateUi(Leds_widget)

        QMetaObject.connectSlotsByName(Leds_widget)
    # setupUi

    def retranslateUi(self, Leds_widget):
        Leds_widget.setWindowTitle(QCoreApplication.translate("Leds_widget", u"Form", None))
        self.ledsOnOffButton.setText(QCoreApplication.translate("Leds_widget", u"I", None))
        self.ledsProgramJumpButton.setText(QCoreApplication.translate("Leds_widget", u"Jump", None))
        self.ledsProgramFadeButton.setText(QCoreApplication.translate("Leds_widget", u"Fade", None))
        self.ledsProgramRandomButton.setText(QCoreApplication.translate("Leds_widget", u"Random", None))
        self.ledsProgramFlashButton.setText(QCoreApplication.translate("Leds_widget", u"Flash", None))
        self.ledsProgramPoliceButton.setText(QCoreApplication.translate("Leds_widget", u"Police", None))
        self.label.setText(QCoreApplication.translate("Leds_widget", u"RED", None))
        self.label_2.setText(QCoreApplication.translate("Leds_widget", u"GREEN", None))
        self.label_3.setText(QCoreApplication.translate("Leds_widget", u"BLUE", None))
        self.ledsValueRed.setText(QCoreApplication.translate("Leds_widget", u"0", None))
        self.ledsValueGreen.setText(QCoreApplication.translate("Leds_widget", u"0", None))
        self.ledsValueBlue.setText(QCoreApplication.translate("Leds_widget", u"0", None))
        self.footer_background.setText("")
        self.label_clock.setText(QCoreApplication.translate("Leds_widget", u"23:23", None))
        self.bluetoothStatusButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Leds_widget", u"Color Picker", None))
    # retranslateUi

