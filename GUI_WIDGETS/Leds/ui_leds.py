# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ledswicbeh.ui'
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
        self.frameLedsBulb = QFrame(self.frame_leds)
        self.frameLedsBulb.setObjectName(u"frameLedsBulb")
        self.frameLedsBulb.setGeometry(QRect(60, 70, 250, 250))
        self.frameLedsBulb.setStyleSheet(u"border-radius:125px;")
        self.frameLedsBulb.setFrameShape(QFrame.StyledPanel)
        self.frameLedsBulb.setFrameShadow(QFrame.Raised)
        self.ledsBulb = QFrame(self.frameLedsBulb)
        self.ledsBulb.setObjectName(u"ledsBulb")
        self.ledsBulb.setGeometry(QRect(0, 0, 250, 250))
        self.ledsBulb.setStyleSheet(u"background:black;\n"
"")
        self.ledsOnOffButton = QCheckBox(self.frameLedsBulb)
        self.ledsOnOffButton.setObjectName(u"ledsOnOffButton")
        self.ledsOnOffButton.setGeometry(QRect(95, 95, 60, 60))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold Condensed")
        font.setPointSize(25)
        self.ledsOnOffButton.setFont(font)
        self.ledsOnOffButton.setFocusPolicy(Qt.NoFocus)
        self.ledsOnOffButton.setStyleSheet(u"QCheckBox{\n"
"	border-radius:30px;\n"
"	\n"
"\n"
"}\n"
"QCheckBox:checked{\n"
"	\n"
"}\n"
"QCheckBox::indicator {\n"
"	width:60px;\n"
"	height:60px;\n"
"	background:rgba(0, 0, 0, 170);\n"
"	border-radius:30px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"		background:rgba(0, 0, 0, 0);\n"
"}")
        self.labelOnOffBackground = QLabel(self.frameLedsBulb)
        self.labelOnOffBackground.setObjectName(u"labelOnOffBackground")
        self.labelOnOffBackground.setGeometry(QRect(95, 95, 60, 60))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiBold SemiConden")
        font1.setPointSize(20)
        self.labelOnOffBackground.setFont(font1)
        self.labelOnOffBackground.setStyleSheet(u"color:white;\n"
"border: 2px solid white;\n"
"border-radius:30px;\n"
"background-color: rgba(0, 0, 0, 100);")
        self.labelOnOffBackground.setAlignment(Qt.AlignCenter)
        self.ledsBulb.raise_()
        self.labelOnOffBackground.raise_()
        self.ledsOnOffButton.raise_()
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
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.ledsProgramJumpButton.setFont(font2)
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
        self.ledsProgramFadeButton.setFont(font2)
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
        self.ledsProgramRandomButton.setFont(font2)
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
        self.ledsProgramFlashButton.setFont(font2)
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
        self.ledsProgramPoliceButton.setFont(font2)
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
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light")
        self.frameLedLabels.setFont(font3)
        self.frameLedLabels.setStyleSheet(u"color:white;")
        self.verticalLayout = QVBoxLayout(self.frameLedLabels)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frameLedLabels)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight SemiConde")
        font4.setPointSize(13)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frameLedLabels)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frameLedLabels)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
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
        self.frameLedValues.setFont(font3)
        self.frameLedValues.setStyleSheet(u"color:white;")
        self.verticalLayout_4 = QVBoxLayout(self.frameLedValues)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ledsValueRed = QLabel(self.frameLedValues)
        self.ledsValueRed.setObjectName(u"ledsValueRed")
        self.ledsValueRed.setMaximumSize(QSize(16777215, 65))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Light")
        font5.setPointSize(13)
        self.ledsValueRed.setFont(font5)

        self.verticalLayout_4.addWidget(self.ledsValueRed)

        self.ledsValueGreen = QLabel(self.frameLedValues)
        self.ledsValueGreen.setObjectName(u"ledsValueGreen")
        self.ledsValueGreen.setFont(font5)

        self.verticalLayout_4.addWidget(self.ledsValueGreen)

        self.ledsValueBlue = QLabel(self.frameLedValues)
        self.ledsValueBlue.setObjectName(u"ledsValueBlue")
        self.ledsValueBlue.setFont(font5)
        self.ledsValueBlue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.ledsValueBlue)


        self.horizontalLayout_4.addWidget(self.frameLedValues)

        self.frameLedColorPicker = QFrame(self.frame_leds)
        self.frameLedColorPicker.setObjectName(u"frameLedColorPicker")
        self.frameLedColorPicker.setGeometry(QRect(545, 70, 200, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.frameLedColorPicker)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frameLedColorPicker)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setFamily(u"Bahnschrift SemiLight SemiConde")
        font6.setPointSize(16)
        self.label_4.setFont(font6)
        self.label_4.setFocusPolicy(Qt.ClickFocus)
        self.label_4.setStyleSheet(u"color:white;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ledsColorPickerButton = QPushButton(self.frameLedColorPicker)
        self.ledsColorPickerButton.setObjectName(u"ledsColorPickerButton")
        self.ledsColorPickerButton.setMaximumSize(QSize(40, 40))
        self.ledsColorPickerButton.setFocusPolicy(Qt.WheelFocus)
        self.ledsColorPickerButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/color_icons/Resources/Icons/color_icons/color_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/color_icons/Resources/Icons/color_icons/color_lightgray.png", QSize(), QIcon.Active, QIcon.Off)
        self.ledsColorPickerButton.setIcon(icon)
        self.ledsColorPickerButton.setIconSize(QSize(240, 24))

        self.horizontalLayout_5.addWidget(self.ledsColorPickerButton)


        self.retranslateUi(Leds_widget)

        QMetaObject.connectSlotsByName(Leds_widget)
    # setupUi

    def retranslateUi(self, Leds_widget):
        Leds_widget.setWindowTitle(QCoreApplication.translate("Leds_widget", u"Form", None))
        self.labelOnOffBackground.setText(QCoreApplication.translate("Leds_widget", u"I", None))
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
        self.label_4.setText(QCoreApplication.translate("Leds_widget", u"Color Picker", None))
    # retranslateUi

