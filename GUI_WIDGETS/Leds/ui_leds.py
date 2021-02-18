# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ledsqKkTwN.ui'
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
        Leds_widget.resize(800, 480)
        self.frame_leds = QFrame(Leds_widget)
        self.frame_leds.setObjectName(u"frame_leds")
        self.frame_leds.setGeometry(QRect(0, 0, 800, 480))
        self.frame_leds.setStyleSheet(u"QFrame#frame_leds{\n"
"	background:rgb(20,20,20);\n"
"}")
        self.frame_leds_config = QFrame(self.frame_leds)
        self.frame_leds_config.setObjectName(u"frame_leds_config")
        self.frame_leds_config.setGeometry(QRect(470, 40, 300, 280))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        self.frame_leds_config.setFont(font)
        self.frame_leds_config.setFrameShape(QFrame.StyledPanel)
        self.frame_leds_config.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_leds_config)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 50, 300, 250))
        self.stackedWidget.setStyleSheet(u"color:white;")
        self.widget_ledPersonalized = QWidget()
        self.widget_ledPersonalized.setObjectName(u"widget_ledPersonalized")
        self.frame_color_slider = QFrame(self.widget_ledPersonalized)
        self.frame_color_slider.setObjectName(u"frame_color_slider")
        self.frame_color_slider.setGeometry(QRect(0, 0, 300, 178))
        self.verticalLayout = QVBoxLayout(self.frame_color_slider)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_slider_label = QFrame(self.frame_color_slider)
        self.frame_slider_label.setObjectName(u"frame_slider_label")
        self.frame_slider_label.setMaximumSize(QSize(300, 16777215))
        self.frame_slider_label.setFrameShape(QFrame.NoFrame)
        self.frame_slider_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_slider_label)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_red = QLabel(self.frame_slider_label)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(13)
        self.label_red.setFont(font1)
        self.label_red.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_red)

        self.label_green = QLabel(self.frame_slider_label)
        self.label_green.setObjectName(u"label_green")
        self.label_green.setMaximumSize(QSize(100, 30))
        self.label_green.setFont(font1)
        self.label_green.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_green)

        self.label_blue = QLabel(self.frame_slider_label)
        self.label_blue.setObjectName(u"label_blue")
        self.label_blue.setMaximumSize(QSize(100, 30))
        self.label_blue.setFont(font1)
        self.label_blue.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_blue)


        self.verticalLayout.addWidget(self.frame_slider_label)

        self.frame_slider_bar = QFrame(self.frame_color_slider)
        self.frame_slider_bar.setObjectName(u"frame_slider_bar")
        self.frame_slider_bar.setMaximumSize(QSize(300, 16777215))
        self.frame_slider_bar.setStyleSheet(u"QSlider::handle:vertical{\n"
"	height:5px;\n"
"	border-radius:5px;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_slider_bar)
        self.horizontalLayout_3.setSpacing(37)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slider_red = QSlider(self.frame_slider_bar)
        self.slider_red.setObjectName(u"slider_red")
        self.slider_red.setMaximumSize(QSize(30, 16777215))
        self.slider_red.setStyleSheet(u"QSlider::handle:vertical{\n"
"	background:red;\n"
"}")
        self.slider_red.setMaximum(255)
        self.slider_red.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.slider_red)

        self.slider_green = QSlider(self.frame_slider_bar)
        self.slider_green.setObjectName(u"slider_green")
        self.slider_green.setMaximumSize(QSize(30, 16777215))
        self.slider_green.setStyleSheet(u"QSlider::handle:vertical{\n"
"	background:green;\n"
"}")
        self.slider_green.setMaximum(255)
        self.slider_green.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.slider_green)

        self.slider_blue = QSlider(self.frame_slider_bar)
        self.slider_blue.setObjectName(u"slider_blue")
        self.slider_blue.setMaximumSize(QSize(30, 16777215))
        self.slider_blue.setStyleSheet(u"QSlider::handle:vertical{\n"
"	background:blue;\n"
"}")
        self.slider_blue.setMaximum(255)
        self.slider_blue.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.slider_blue)


        self.verticalLayout.addWidget(self.frame_slider_bar)

        self.slider_brightness = QSlider(self.widget_ledPersonalized)
        self.slider_brightness.setObjectName(u"slider_brightness")
        self.slider_brightness.setGeometry(QRect(50, 210, 200, 20))
        font2 = QFont()
        font2.setPointSize(4)
        self.slider_brightness.setFont(font2)
        self.slider_brightness.setStyleSheet(u"\n"
"QSlider::groove:horizontal{\n"
"	height:1px;\n"
"	background:gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"	background:rgb(200,200,200);\n"
"	width:10px;\n"
"	border-radius:5px;\n"
"	margin-top:-5px;\n"
"	margin-bottom:-5px;\n"
"\n"
"\n"
"}")
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setOrientation(Qt.Horizontal)
        self.label_brightness = QLabel(self.widget_ledPersonalized)
        self.label_brightness.setObjectName(u"label_brightness")
        self.label_brightness.setGeometry(QRect(50, 188, 200, 30))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight")
        font3.setPointSize(13)
        self.label_brightness.setFont(font3)
        self.label_brightness.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.stackedWidget.addWidget(self.widget_ledPersonalized)
        self.widget_ledProgram = QWidget()
        self.widget_ledProgram.setObjectName(u"widget_ledProgram")
        self.frame_ledPrograms = QFrame(self.widget_ledProgram)
        self.frame_ledPrograms.setObjectName(u"frame_ledPrograms")
        self.frame_ledPrograms.setGeometry(QRect(0, 20, 300, 180))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift")
        font4.setPointSize(20)
        self.frame_ledPrograms.setFont(font4)
        self.frame_ledPrograms.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:1px solid rgb(250, 20, 20);\n"
"	\n"
"	color: rgb(250, 20, 20);\n"
"	padding:5px;\n"
"	margin:5px;	\n"
"	background-color: rgb(30, 30, 30);\n"
"	font: 12pt \"Bahnschrift SemiLight\";\n"
"}")
        self.gridLayout = QGridLayout(self.frame_ledPrograms)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.pushButton_program_fade = QPushButton(self.frame_ledPrograms)
        self.pushButton_program_fade.setObjectName(u"pushButton_program_fade")
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiLight")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.pushButton_program_fade.setFont(font5)

        self.gridLayout.addWidget(self.pushButton_program_fade, 0, 0, 1, 1)

        self.pushButton_program_police = QPushButton(self.frame_ledPrograms)
        self.pushButton_program_police.setObjectName(u"pushButton_program_police")

        self.gridLayout.addWidget(self.pushButton_program_police, 2, 0, 1, 1)

        self.pushButton_program_jump = QPushButton(self.frame_ledPrograms)
        self.pushButton_program_jump.setObjectName(u"pushButton_program_jump")

        self.gridLayout.addWidget(self.pushButton_program_jump, 0, 1, 1, 1)

        self.pushButton_flash = QPushButton(self.frame_ledPrograms)
        self.pushButton_flash.setObjectName(u"pushButton_flash")
        self.pushButton_flash.setFont(font5)

        self.gridLayout.addWidget(self.pushButton_flash, 1, 1, 1, 1)

        self.pushButton_program_random = QPushButton(self.frame_ledPrograms)
        self.pushButton_program_random.setObjectName(u"pushButton_program_random")

        self.gridLayout.addWidget(self.pushButton_program_random, 1, 0, 1, 1)

        self.pushButton_new_program = QPushButton(self.widget_ledProgram)
        self.pushButton_new_program.setObjectName(u"pushButton_new_program")
        self.pushButton_new_program.setGeometry(QRect(135, 200, 30, 30))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift SemiBold")
        font6.setPointSize(12)
        self.pushButton_new_program.setFont(font6)
        self.pushButton_new_program.setStyleSheet(u"padding-bottom:3px;\n"
"color:rgb(30,30,30);\n"
"border-radius:15px;;\n"
"background:rgb(250, 20, 20);\n"
"border: 1px solid rgb(30,30,30);")
        self.label_programs = QLabel(self.widget_ledProgram)
        self.label_programs.setObjectName(u"label_programs")
        self.label_programs.setGeometry(QRect(0, -3, 300, 25))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Light SemiCondensed")
        font7.setPointSize(14)
        self.label_programs.setFont(font7)
        self.label_programs.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.widget_ledProgram)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 27, 281, 2))
        font8 = QFont()
        font8.setPointSize(7)
        self.line.setFont(font8)
        self.line.setStyleSheet(u"background: red; border:none;")
        self.stackedWidget.addWidget(self.widget_ledProgram)
        self.frame_ledColor = QFrame(self.frame_leds)
        self.frame_ledColor.setObjectName(u"frame_ledColor")
        self.frame_ledColor.setGeometry(QRect(60, 130, 200, 200))
        self.frame_ledColor.setStyleSheet(u"QFrame#frame_ledColor{\n"
"\n"
"	border:3px solid black;\n"
"	border-radius:100px;\n"
"	background:rgb(0,0,0);\n"
"\n"
"}")
        self.label_ledColor = QLabel(self.frame_leds)
        self.label_ledColor.setObjectName(u"label_ledColor")
        self.label_ledColor.setGeometry(QRect(60, 80, 200, 50))
        font9 = QFont()
        font9.setFamily(u"Bahnschrift SemiBold SemiConden")
        font9.setPointSize(19)
        self.label_ledColor.setFont(font9)
        self.label_ledColor.setStyleSheet(u"color:lightgray;")
        self.label_ledColor.setAlignment(Qt.AlignCenter)
        self.pushButton_led_onOff = QPushButton(self.frame_leds)
        self.pushButton_led_onOff.setObjectName(u"pushButton_led_onOff")
        self.pushButton_led_onOff.setGeometry(QRect(375, 200, 50, 50))
        self.pushButton_led_onOff.setStyleSheet(u"border-radius:25px;\n"
"border:2px solid lightgray;")
        icon = QIcon()
        icon.addFile(u":/icons_white/Resources/Icons/png-white/fi-rr-power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_led_onOff.setIcon(icon)
        self.pushButton_led_onOff.setIconSize(QSize(24, 24))

        self.retranslateUi(Leds_widget)

        QMetaObject.connectSlotsByName(Leds_widget)
    # setupUi

    def retranslateUi(self, Leds_widget):
        Leds_widget.setWindowTitle(QCoreApplication.translate("Leds_widget", u"Form", None))
        self.label_red.setText(QCoreApplication.translate("Leds_widget", u"RED", None))
        self.label_green.setText(QCoreApplication.translate("Leds_widget", u"GREEN", None))
        self.label_blue.setText(QCoreApplication.translate("Leds_widget", u"BLUE", None))
        self.label_brightness.setText(QCoreApplication.translate("Leds_widget", u"Brightness", None))
        self.pushButton_program_fade.setText(QCoreApplication.translate("Leds_widget", u"Fade", None))
        self.pushButton_program_police.setText(QCoreApplication.translate("Leds_widget", u"Police", None))
        self.pushButton_program_jump.setText(QCoreApplication.translate("Leds_widget", u"Jump", None))
        self.pushButton_flash.setText(QCoreApplication.translate("Leds_widget", u"Flash", None))
        self.pushButton_program_random.setText(QCoreApplication.translate("Leds_widget", u"Random", None))
        self.pushButton_new_program.setText(QCoreApplication.translate("Leds_widget", u"+", None))
        self.label_programs.setText(QCoreApplication.translate("Leds_widget", u"Programs", None))
        self.label_ledColor.setText(QCoreApplication.translate("Leds_widget", u"LED COLOR", None))
        self.pushButton_led_onOff.setText("")
    # retranslateUi

