# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_settingsRTnKFP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Settings_widget(object):
    def setupUi(self, Settings_widget):
        if not Settings_widget.objectName():
            Settings_widget.setObjectName(u"Settings_widget")
        Settings_widget.resize(800, 480)
        self.frame_settings = QFrame(Settings_widget)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setGeometry(QRect(50, 80, 700, 300))
        self.scrollArea = QScrollArea(self.frame_settings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 200, 300))
        self.scrollArea.setMinimumSize(QSize(200, 300))
        self.scrollArea.setMaximumSize(QSize(200, 300))
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border:none;\n"
"	background:transparent;\n"
"\n"
"}\n"
"#scrollAreaWidgetContents{\n"
"	background-color:rgb(54, 54, 54);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border:none;\n"
"	border-bottom:1px solid gray;\n"
"	background:none;\n"
"	font: 10pt \"Bahnschrift SemiLight\";\n"
"	color:rgb(218, 218, 218);\n"
"}\n"
"/**/\n"
"\n"
"QScrollBar:vertical {\n"
"       border:none;\n"
"       background: rgb(20,20,20);\n"
"		width:10px;\n"
"   }\n"
"   QScrollBar::handle:vertical {\n"
"       background: rgb(255, 24, 24);\n"
"		border-radius:5px;\n"
"     \n"
"   }\n"
"  \n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical  {\n"
"       background: none;\n"
"\n"
"   }\n"
"\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 180, 400))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.frame_setting_brightness = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_brightness.setObjectName(u"frame_setting_brightness")
        self.frame_setting_brightness.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.frame_setting_brightness)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsBrightness = QPushButton(self.frame_setting_brightness)
        self.bearing_settingsBrightness.setObjectName(u"bearing_settingsBrightness")
        self.bearing_settingsBrightness.setMinimumSize(QSize(0, 40))
        self.bearing_settingsBrightness.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_5.addWidget(self.bearing_settingsBrightness)


        self.verticalLayout.addWidget(self.frame_setting_brightness)

        self.frame_setting_wifi = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_wifi.setObjectName(u"frame_setting_wifi")
        self.frame_setting_wifi.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_6 = QHBoxLayout(self.frame_setting_wifi)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsWifi = QPushButton(self.frame_setting_wifi)
        self.bearing_settingsWifi.setObjectName(u"bearing_settingsWifi")
        self.bearing_settingsWifi.setMinimumSize(QSize(0, 40))
        self.bearing_settingsWifi.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.bearing_settingsWifi)


        self.verticalLayout.addWidget(self.frame_setting_wifi)

        self.frame_setting_bluetooth = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_bluetooth.setObjectName(u"frame_setting_bluetooth")
        self.frame_setting_bluetooth.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_7 = QHBoxLayout(self.frame_setting_bluetooth)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsBluetooth = QPushButton(self.frame_setting_bluetooth)
        self.bearing_settingsBluetooth.setObjectName(u"bearing_settingsBluetooth")
        self.bearing_settingsBluetooth.setMinimumSize(QSize(0, 40))
        self.bearing_settingsBluetooth.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_7.addWidget(self.bearing_settingsBluetooth)


        self.verticalLayout.addWidget(self.frame_setting_bluetooth)

        self.frame_setting_remote = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_remote.setObjectName(u"frame_setting_remote")
        self.frame_setting_remote.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_8 = QHBoxLayout(self.frame_setting_remote)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsRemote = QPushButton(self.frame_setting_remote)
        self.bearing_settingsRemote.setObjectName(u"bearing_settingsRemote")
        self.bearing_settingsRemote.setMinimumSize(QSize(0, 40))
        self.bearing_settingsRemote.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.bearing_settingsRemote)


        self.verticalLayout.addWidget(self.frame_setting_remote)

        self.frame_setting_navigator = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_navigator.setObjectName(u"frame_setting_navigator")
        self.frame_setting_navigator.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_11 = QHBoxLayout(self.frame_setting_navigator)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsNavigator = QPushButton(self.frame_setting_navigator)
        self.bearing_settingsNavigator.setObjectName(u"bearing_settingsNavigator")
        self.bearing_settingsNavigator.setMinimumSize(QSize(0, 40))
        self.bearing_settingsNavigator.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.bearing_settingsNavigator)


        self.verticalLayout.addWidget(self.frame_setting_navigator)

        self.frame_setting_status = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_status.setObjectName(u"frame_setting_status")
        self.frame_setting_status.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.frame_setting_status)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsStatus = QPushButton(self.frame_setting_status)
        self.bearing_settingsStatus.setObjectName(u"bearing_settingsStatus")
        self.bearing_settingsStatus.setMinimumSize(QSize(0, 40))
        self.bearing_settingsStatus.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.bearing_settingsStatus)


        self.verticalLayout.addWidget(self.frame_setting_status)

        self.frame_setting_gpio = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_gpio.setObjectName(u"frame_setting_gpio")
        self.frame_setting_gpio.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_setting_gpio)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsGpio = QPushButton(self.frame_setting_gpio)
        self.bearing_settingsGpio.setObjectName(u"bearing_settingsGpio")
        self.bearing_settingsGpio.setMinimumSize(QSize(0, 40))
        self.bearing_settingsGpio.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_10.addWidget(self.bearing_settingsGpio)


        self.verticalLayout.addWidget(self.frame_setting_gpio)

        self.frame_setting_systemInfo = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_systemInfo.setObjectName(u"frame_setting_systemInfo")
        self.frame_setting_systemInfo.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.frame_setting_systemInfo)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsSystemInfo = QPushButton(self.frame_setting_systemInfo)
        self.bearing_settingsSystemInfo.setObjectName(u"bearing_settingsSystemInfo")
        self.bearing_settingsSystemInfo.setMinimumSize(QSize(0, 40))
        self.bearing_settingsSystemInfo.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.bearing_settingsSystemInfo)


        self.verticalLayout.addWidget(self.frame_setting_systemInfo)

        self.frame_setting_terminal = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_terminal.setObjectName(u"frame_setting_terminal")
        self.frame_setting_terminal.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.frame_setting_terminal)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsTerminal = QPushButton(self.frame_setting_terminal)
        self.bearing_settingsTerminal.setObjectName(u"bearing_settingsTerminal")
        self.bearing_settingsTerminal.setMinimumSize(QSize(0, 40))
        self.bearing_settingsTerminal.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.bearing_settingsTerminal)


        self.verticalLayout.addWidget(self.frame_setting_terminal)

        self.frame_setting_advanced = QFrame(self.scrollAreaWidgetContents)
        self.frame_setting_advanced.setObjectName(u"frame_setting_advanced")
        self.frame_setting_advanced.setMaximumSize(QSize(180, 40))
        self.horizontalLayout_14 = QHBoxLayout(self.frame_setting_advanced)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bearing_settingsAdvanced = QPushButton(self.frame_setting_advanced)
        self.bearing_settingsAdvanced.setObjectName(u"bearing_settingsAdvanced")
        self.bearing_settingsAdvanced.setMinimumSize(QSize(0, 40))
        self.bearing_settingsAdvanced.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_14.addWidget(self.bearing_settingsAdvanced)


        self.verticalLayout.addWidget(self.frame_setting_advanced)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_settings = QStackedWidget(self.frame_settings)
        self.stackedWidget_settings.setObjectName(u"stackedWidget_settings")
        self.stackedWidget_settings.setGeometry(QRect(300, 0, 400, 300))
        self.page_brightness = QWidget()
        self.page_brightness.setObjectName(u"page_brightness")
        self.p_brightnes_title = QFrame(self.page_brightness)
        self.p_brightnes_title.setObjectName(u"p_brightnes_title")
        self.p_brightnes_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_13 = QLabel(self.p_brightnes_title)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 380, 40))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiLight")
        font.setPointSize(21)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color:white;")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_4 = QFrame(self.p_brightnes_title)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 50, 380, 2))
        self.line_4.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)
        self.p_brightness_level = QFrame(self.page_brightness)
        self.p_brightness_level.setObjectName(u"p_brightness_level")
        self.p_brightness_level.setGeometry(QRect(0, 60, 370, 70))
        self.bearing_brightnessLevelSlide = QSlider(self.p_brightness_level)
        self.bearing_brightnessLevelSlide.setObjectName(u"bearing_brightnessLevelSlide")
        self.bearing_brightnessLevelSlide.setGeometry(QRect(10, 40, 360, 22))
        self.bearing_brightnessLevelSlide.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	height:1px;	\n"
"	width:340px;\n"
"	background:gray;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"	background:red;\n"
"	width:10px;\n"
"	margin:-5px;\n"
"	border-radius:5px;	\n"
"\n"
"}")
        self.bearing_brightnessLevelSlide.setMinimum(20)
        self.bearing_brightnessLevelSlide.setMaximum(255)
        self.bearing_brightnessLevelSlide.setOrientation(Qt.Horizontal)
        self.label_37 = QLabel(self.p_brightness_level)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 0, 380, 30))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiLight")
        font1.setPointSize(13)
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"color:rgb(211, 211, 211);")
        self.stackedWidget_settings.addWidget(self.page_brightness)
        self.page_wifi = QWidget()
        self.page_wifi.setObjectName(u"page_wifi")
        self.scrollArea_wifi = QScrollArea(self.page_wifi)
        self.scrollArea_wifi.setObjectName(u"scrollArea_wifi")
        self.scrollArea_wifi.setGeometry(QRect(0, 60, 400, 240))
        self.scrollArea_wifi.setStyleSheet(u"QScrollArea{\n"
"	border:none;\n"
"	background:transparent;\n"
"\n"
"}\n"
"QScrollArea QWidget{\n"
"	background-color:transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"/**/\n"
"\n"
"QScrollBar:vertical {\n"
"       border:none;\n"
"       background: rgb(20,20,20);\n"
"		width:10px;\n"
"   }\n"
"   QScrollBar::handle:vertical {\n"
"       background: rgb(255, 24, 24);\n"
"		border-radius:5px;\n"
"     \n"
"   }\n"
"  \n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical  {\n"
"       background: none;\n"
"\n"
"   }\n"
"\n"
"")
        self.scrollArea_wifi.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_wifi.setWidgetResizable(True)
        self.scrollArea_wifi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 390, 280))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_8.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_8.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_8.setMinimumSize(QSize(0, 280))
        self.p_wifi_power = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_power.setObjectName(u"p_wifi_power")
        self.p_wifi_power.setGeometry(QRect(0, 0, 370, 40))
        self.label_2 = QLabel(self.p_wifi_power)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 5, 240, 30))
        self.label_2.setMaximumSize(QSize(250, 16777215))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.frame_cb = QFrame(self.p_wifi_power)
        self.frame_cb.setObjectName(u"frame_cb")
        self.frame_cb.setGeometry(QRect(310, 0, 60, 40))
        self.a_border_4 = QFrame(self.frame_cb)
        self.a_border_4.setObjectName(u"a_border_4")
        self.a_border_4.setGeometry(QRect(0, 5, 60, 30))
        self.a_border_4.setStyleSheet(u"QFrame{\n"
"	border-radius:15px;\n"
"	border:2px solid gray; \n"
"	border-color: rgb(211, 211, 211);\n"
"}\n"
"QLabel{\n"
"	border:none; \n"
"	color:white;\n"
"	margin-bottom:1px;\n"
"}")
        self.a_border_4.setFrameShape(QFrame.StyledPanel)
        self.a_border_4.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.a_border_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 30, 30))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setPointSize(14)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.a_border_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 0, 30, 30))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.bearing_wifiPowerCheckbox = QCheckBox(self.frame_cb)
        self.bearing_wifiPowerCheckbox.setObjectName(u"bearing_wifiPowerCheckbox")
        self.bearing_wifiPowerCheckbox.setGeometry(QRect(0, 0, 60, 40))
        self.bearing_wifiPowerCheckbox.setFocusPolicy(Qt.NoFocus)
        self.bearing_wifiPowerCheckbox.setStyleSheet(u"QCheckBox{\n"
"	background:none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	height:20px;\n"
"	width:20px;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	margin-left:6px;\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	margin-left:30px;\n"
"	background:rgb(54, 0, 0);\n"
"\n"
"	\n"
"}")
        self.p_wifi_separator_2 = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_separator_2.setObjectName(u"p_wifi_separator_2")
        self.p_wifi_separator_2.setGeometry(QRect(0, 140, 370, 20))
        self.line_5 = QFrame(self.p_wifi_separator_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(10, 10, 360, 1))
        self.line_5.setStyleSheet(u"border:none;\n"
"background:gray;")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)
        self.p_wifi_separator = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_separator.setObjectName(u"p_wifi_separator")
        self.p_wifi_separator.setGeometry(QRect(0, 40, 370, 20))
        self.line = QFrame(self.p_wifi_separator)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 10, 360, 1))
        self.line.setStyleSheet(u"border:none;\n"
"background:gray;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.p_wifi_ip = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_ip.setObjectName(u"p_wifi_ip")
        self.p_wifi_ip.setGeometry(QRect(0, 100, 370, 40))
        self.label_14 = QLabel(self.p_wifi_ip)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 0, 190, 40))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_wifiIpText = QLabel(self.p_wifi_ip)
        self.bearing_wifiIpText.setObjectName(u"bearing_wifiIpText")
        self.bearing_wifiIpText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_wifiIpText.setFont(font1)
        self.bearing_wifiIpText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_wifiIpText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.p_wifi_ssid = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_ssid.setObjectName(u"p_wifi_ssid")
        self.p_wifi_ssid.setGeometry(QRect(0, 60, 370, 40))
        self.label_9 = QLabel(self.p_wifi_ssid)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 190, 40))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_wifiSsidText = QLabel(self.p_wifi_ssid)
        self.bearing_wifiSsidText.setObjectName(u"bearing_wifiSsidText")
        self.bearing_wifiSsidText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_wifiSsidText.setFont(font1)
        self.bearing_wifiSsidText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_wifiSsidText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.p_wifi_connectTitle = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_connectTitle.setObjectName(u"p_wifi_connectTitle")
        self.p_wifi_connectTitle.setGeometry(QRect(0, 160, 370, 40))
        self.label_7 = QLabel(self.p_wifi_connectTitle)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 5, 270, 30))
        self.label_7.setMaximumSize(QSize(9999999, 16777215))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color:red;")
        self.p_wifi_ssid_input = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wifi_ssid_input.setObjectName(u"p_wifi_ssid_input")
        self.p_wifi_ssid_input.setGeometry(QRect(0, 200, 370, 40))
        self.bearing_wifiSSIDInput = QLineEdit(self.p_wifi_ssid_input)
        self.bearing_wifiSSIDInput.setObjectName(u"bearing_wifiSSIDInput")
        self.bearing_wifiSSIDInput.setGeometry(QRect(220, 5, 151, 30))
        self.bearing_wifiSSIDInput.setFont(font1)
        self.bearing_wifiSSIDInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	color:white;\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	\n"
"	\n"
"	border:1px solid rgb(97, 97, 97);\n"
"}")
        self.bearing_wifiSSIDInput.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.p_wifi_ssid_input)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 5, 200, 30))
        self.label_11.setMaximumSize(QSize(250, 16777215))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color:white;")
        self.p_wfi_pass_input = QFrame(self.scrollAreaWidgetContents_8)
        self.p_wfi_pass_input.setObjectName(u"p_wfi_pass_input")
        self.p_wfi_pass_input.setGeometry(QRect(0, 240, 370, 40))
        self.bearing_wifiPassInput = QLineEdit(self.p_wfi_pass_input)
        self.bearing_wifiPassInput.setObjectName(u"bearing_wifiPassInput")
        self.bearing_wifiPassInput.setEnabled(True)
        self.bearing_wifiPassInput.setGeometry(QRect(220, 5, 110, 30))
        self.bearing_wifiPassInput.setFont(font1)
        self.bearing_wifiPassInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	color:white;\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	\n"
"	\n"
"	border:1px solid rgb(97, 97, 97);\n"
"}\n"
"QLineEdit:disabled{\n"
"	background:rgba(57, 57, 57, 250);\n"
"}")
        self.bearing_wifiPassInput.setAlignment(Qt.AlignCenter)
        self.bearing_wifiPassLabel = QLabel(self.p_wfi_pass_input)
        self.bearing_wifiPassLabel.setObjectName(u"bearing_wifiPassLabel")
        self.bearing_wifiPassLabel.setGeometry(QRect(10, 5, 200, 30))
        self.bearing_wifiPassLabel.setMaximumSize(QSize(250, 16777215))
        self.bearing_wifiPassLabel.setFont(font1)
        self.bearing_wifiPassLabel.setStyleSheet(u"color:white;\n"
"")
        self.bearing_wifiPassButton = QPushButton(self.p_wfi_pass_input)
        self.bearing_wifiPassButton.setObjectName(u"bearing_wifiPassButton")
        self.bearing_wifiPassButton.setEnabled(True)
        self.bearing_wifiPassButton.setGeometry(QRect(340, 5, 30, 30))
        self.bearing_wifiPassButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_wifiPassButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}\n"
"QPushButton:disabled{\n"
"	border:2px solid gray;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons_white/Resources/Icons/png-white/fi-rr-arrow-small-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bearing_wifiPassButton.setIcon(icon)
        self.bearing_wifiPassButton.setIconSize(QSize(18, 18))
        self.scrollArea_wifi.setWidget(self.scrollAreaWidgetContents_8)
        self.p_wifi_title = QFrame(self.page_wifi)
        self.p_wifi_title.setObjectName(u"p_wifi_title")
        self.p_wifi_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_25 = QLabel(self.p_wifi_title)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 330, 40))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color:white;")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_14 = QFrame(self.p_wifi_title)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(10, 50, 380, 2))
        self.line_14.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setFrameShape(QFrame.HLine)
        self.bearing_refreshWifiButton = QPushButton(self.p_wifi_title)
        self.bearing_refreshWifiButton.setObjectName(u"bearing_refreshWifiButton")
        self.bearing_refreshWifiButton.setGeometry(QRect(350, 10, 40, 40))
        self.bearing_refreshWifiButton.setStyleSheet(u"border:none;\n"
"background:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bearing_refreshWifiButton.setIcon(icon1)
        self.bearing_refreshWifiButton.setIconSize(QSize(24, 24))
        self.stackedWidget_settings.addWidget(self.page_wifi)
        self.page_bluetooth = QWidget()
        self.page_bluetooth.setObjectName(u"page_bluetooth")
        self.p_bt_power = QFrame(self.page_bluetooth)
        self.p_bt_power.setObjectName(u"p_bt_power")
        self.p_bt_power.setGeometry(QRect(0, 60, 370, 40))
        self.label_3 = QLabel(self.p_bt_power)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 5, 240, 30))
        self.label_3.setMaximumSize(QSize(250, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white;")
        self.frame_cb_2 = QFrame(self.p_bt_power)
        self.frame_cb_2.setObjectName(u"frame_cb_2")
        self.frame_cb_2.setGeometry(QRect(310, 0, 60, 40))
        self.a_border_5 = QFrame(self.frame_cb_2)
        self.a_border_5.setObjectName(u"a_border_5")
        self.a_border_5.setGeometry(QRect(0, 5, 60, 30))
        self.a_border_5.setStyleSheet(u"QFrame{\n"
"	border-radius:15px;\n"
"	border:2px solid gray; \n"
"	border-color: rgb(211, 211, 211);\n"
"}\n"
"QLabel{\n"
"	border:none; \n"
"	color:white;\n"
"	margin-bottom:1px;\n"
"}")
        self.label_8 = QLabel(self.a_border_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 30, 30))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.a_border_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 0, 30, 30))
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.bearing_btPowerCheckbox = QCheckBox(self.frame_cb_2)
        self.bearing_btPowerCheckbox.setObjectName(u"bearing_btPowerCheckbox")
        self.bearing_btPowerCheckbox.setGeometry(QRect(0, 0, 60, 40))
        self.bearing_btPowerCheckbox.setFocusPolicy(Qt.NoFocus)
        self.bearing_btPowerCheckbox.setStyleSheet(u"QCheckBox{\n"
"	background:none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	height:20px;\n"
"	width:20px;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	margin-left:6px;\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	margin-left:30px;\n"
"	background:rgb(54, 0, 0);\n"
"\n"
"	\n"
"}")
        self.p_bt_separator = QFrame(self.page_bluetooth)
        self.p_bt_separator.setObjectName(u"p_bt_separator")
        self.p_bt_separator.setGeometry(QRect(0, 100, 370, 20))
        self.line_8 = QFrame(self.p_bt_separator)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(10, 10, 360, 1))
        self.line_8.setStyleSheet(u"border:none;\n"
"background:gray;")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setFrameShape(QFrame.HLine)
        self.p_bt_separator_2 = QFrame(self.page_bluetooth)
        self.p_bt_separator_2.setObjectName(u"p_bt_separator_2")
        self.p_bt_separator_2.setGeometry(QRect(0, 200, 370, 20))
        self.line_9 = QFrame(self.p_bt_separator_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(10, 10, 360, 1))
        self.line_9.setStyleSheet(u"border:none;\n"
"background:gray;")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.HLine)
        self.p_bt_discoverable = QFrame(self.page_bluetooth)
        self.p_bt_discoverable.setObjectName(u"p_bt_discoverable")
        self.p_bt_discoverable.setGeometry(QRect(0, 160, 370, 40))
        self.label_21 = QLabel(self.p_bt_discoverable)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 5, 240, 30))
        self.label_21.setMaximumSize(QSize(250, 16777215))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"color:white;")
        self.frame_cb_4 = QFrame(self.p_bt_discoverable)
        self.frame_cb_4.setObjectName(u"frame_cb_4")
        self.frame_cb_4.setGeometry(QRect(310, 0, 60, 40))
        self.a_border_6 = QFrame(self.frame_cb_4)
        self.a_border_6.setObjectName(u"a_border_6")
        self.a_border_6.setGeometry(QRect(0, 5, 60, 30))
        self.a_border_6.setStyleSheet(u"QFrame{\n"
"	border-radius:15px;\n"
"	border:2px solid gray; \n"
"	border-color: rgb(211, 211, 211);\n"
"}\n"
"QLabel{\n"
"	border:none; \n"
"	color:white;\n"
"	margin-bottom:1px;\n"
"}")
        self.label_22 = QLabel(self.a_border_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 30, 30))
        self.label_22.setFont(font2)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.a_border_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 0, 30, 30))
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.bearing_btDiscoverableCheckbox = QCheckBox(self.frame_cb_4)
        self.bearing_btDiscoverableCheckbox.setObjectName(u"bearing_btDiscoverableCheckbox")
        self.bearing_btDiscoverableCheckbox.setGeometry(QRect(0, 0, 60, 40))
        self.bearing_btDiscoverableCheckbox.setFocusPolicy(Qt.NoFocus)
        self.bearing_btDiscoverableCheckbox.setStyleSheet(u"QCheckBox{\n"
"	background:none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	height:20px;\n"
"	width:20px;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	margin-left:6px;\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	margin-left:30px;\n"
"	background:rgb(54, 0, 0);\n"
"\n"
"	\n"
"}")
        self.p_bt_btName = QFrame(self.page_bluetooth)
        self.p_bt_btName.setObjectName(u"p_bt_btName")
        self.p_bt_btName.setGeometry(QRect(0, 120, 370, 40))
        self.label_27 = QLabel(self.p_bt_btName)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 0, 190, 40))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_btNameText = QLabel(self.p_bt_btName)
        self.bearing_btNameText.setObjectName(u"bearing_btNameText")
        self.bearing_btNameText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_btNameText.setFont(font1)
        self.bearing_btNameText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_btNameText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.p_bt_btName_2 = QFrame(self.page_bluetooth)
        self.p_bt_btName_2.setObjectName(u"p_bt_btName_2")
        self.p_bt_btName_2.setGeometry(QRect(0, 220, 370, 40))
        self.label_29 = QLabel(self.p_bt_btName_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 0, 190, 40))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_btConnectedText = QLabel(self.p_bt_btName_2)
        self.bearing_btConnectedText.setObjectName(u"bearing_btConnectedText")
        self.bearing_btConnectedText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_btConnectedText.setFont(font1)
        self.bearing_btConnectedText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_btConnectedText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.p_bt_btManager = QFrame(self.page_bluetooth)
        self.p_bt_btManager.setObjectName(u"p_bt_btManager")
        self.p_bt_btManager.setGeometry(QRect(0, 260, 370, 50))
        self.label_31 = QLabel(self.p_bt_btManager)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 0, 200, 50))
        self.label_31.setMaximumSize(QSize(250, 16777215))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"color:white;")
        self.bearing_btManagerButton = QPushButton(self.p_bt_btManager)
        self.bearing_btManagerButton.setObjectName(u"bearing_btManagerButton")
        self.bearing_btManagerButton.setGeometry(QRect(270, 10, 100, 30))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.bearing_btManagerButton.setFont(font3)
        self.bearing_btManagerButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_btManagerButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:15px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")
        self.p_bt_title = QFrame(self.page_bluetooth)
        self.p_bt_title.setObjectName(u"p_bt_title")
        self.p_bt_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_26 = QLabel(self.p_bt_title)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 330, 40))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color:white;")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_15 = QFrame(self.p_bt_title)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(10, 50, 380, 2))
        self.line_15.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setFrameShape(QFrame.HLine)
        self.bearing_refreshBtButton = QPushButton(self.p_bt_title)
        self.bearing_refreshBtButton.setObjectName(u"bearing_refreshBtButton")
        self.bearing_refreshBtButton.setGeometry(QRect(350, 10, 40, 40))
        self.bearing_refreshBtButton.setStyleSheet(u"border:none;\n"
"background:none;")
        self.bearing_refreshBtButton.setIcon(icon1)
        self.bearing_refreshBtButton.setIconSize(QSize(24, 24))
        self.stackedWidget_settings.addWidget(self.page_bluetooth)
        self.page_remote = QWidget()
        self.page_remote.setObjectName(u"page_remote")
        self.frame_5 = QFrame(self.page_remote)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 400, 60))
        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 10, 380, 40))
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color:white;")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_10 = QFrame(self.frame_5)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(10, 50, 380, 2))
        self.line_10.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setFrameShape(QFrame.HLine)
        self.frame_3 = QFrame(self.page_remote)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 60, 370, 40))
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 5, 240, 30))
        self.label_4.setMaximumSize(QSize(250, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:white;")
        self.frame_cb_3 = QFrame(self.frame_3)
        self.frame_cb_3.setObjectName(u"frame_cb_3")
        self.frame_cb_3.setGeometry(QRect(310, 0, 60, 40))
        self.a_border = QFrame(self.frame_cb_3)
        self.a_border.setObjectName(u"a_border")
        self.a_border.setGeometry(QRect(0, 5, 60, 30))
        self.a_border.setStyleSheet(u"QFrame{\n"
"	border-radius:15px;\n"
"	border:2px solid gray; \n"
"	border-color: rgb(211, 211, 211);\n"
"}\n"
"QLabel{\n"
"	border:none; \n"
"	color:white;\n"
"	margin-bottom:1px;\n"
"}")
        self.label_10 = QLabel(self.a_border)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 30, 30))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.a_border)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 0, 30, 30))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.bearing_remoteMultimediaCheckbox = QCheckBox(self.frame_cb_3)
        self.bearing_remoteMultimediaCheckbox.setObjectName(u"bearing_remoteMultimediaCheckbox")
        self.bearing_remoteMultimediaCheckbox.setGeometry(QRect(0, 0, 60, 40))
        self.bearing_remoteMultimediaCheckbox.setFocusPolicy(Qt.NoFocus)
        self.bearing_remoteMultimediaCheckbox.setStyleSheet(u"QCheckBox{\n"
"	background:none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	height:20px;\n"
"	width:20px;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	margin-left:6px;\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	margin-left:30px;\n"
"	background:rgb(54, 0, 0);\n"
"\n"
"	\n"
"}")
        self.stackedWidget_settings.addWidget(self.page_remote)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 400, 60))
        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 380, 40))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color:white;")
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_12 = QFrame(self.frame_9)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(10, 50, 380, 2))
        self.line_12.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setFrameShape(QFrame.HLine)
        self.frame_11 = QFrame(self.page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 60, 370, 40))
        self.bearing_navigatorHomeInput = QLineEdit(self.frame_11)
        self.bearing_navigatorHomeInput.setObjectName(u"bearing_navigatorHomeInput")
        self.bearing_navigatorHomeInput.setGeometry(QRect(120, 5, 210, 30))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(14)
        self.bearing_navigatorHomeInput.setFont(font4)
        self.bearing_navigatorHomeInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	color:white;\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	\n"
"	\n"
"	border:1px solid rgb(97, 97, 97);\n"
"}")
        self.bearing_navigatorHomeInput.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 5, 100, 30))
        self.label_17.setMaximumSize(QSize(250, 16777215))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"color:white;")
        self.bearing_navigatorHomeButton = QPushButton(self.frame_11)
        self.bearing_navigatorHomeButton.setObjectName(u"bearing_navigatorHomeButton")
        self.bearing_navigatorHomeButton.setGeometry(QRect(340, 5, 30, 30))
        self.bearing_navigatorHomeButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}")
        self.bearing_navigatorHomeButton.setIcon(icon)
        self.bearing_navigatorHomeButton.setIconSize(QSize(18, 18))
        self.stackedWidget_settings.addWidget(self.page)
        self.page_status = QWidget()
        self.page_status.setObjectName(u"page_status")
        self.p_status_title = QFrame(self.page_status)
        self.p_status_title.setObjectName(u"p_status_title")
        self.p_status_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_38 = QLabel(self.p_status_title)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 10, 330, 40))
        self.label_38.setFont(font)
        self.label_38.setStyleSheet(u"color:white;")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_11 = QFrame(self.p_status_title)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(10, 50, 380, 2))
        self.line_11.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setFrameShape(QFrame.HLine)
        self.bearing_statusRefreshButton = QPushButton(self.p_status_title)
        self.bearing_statusRefreshButton.setObjectName(u"bearing_statusRefreshButton")
        self.bearing_statusRefreshButton.setGeometry(QRect(350, 10, 40, 40))
        self.bearing_statusRefreshButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_statusRefreshButton.setStyleSheet(u"border:none;\n"
"background:none;")
        self.bearing_statusRefreshButton.setIcon(icon1)
        self.bearing_statusRefreshButton.setIconSize(QSize(24, 24))
        self.p_status_scrollArea = QFrame(self.page_status)
        self.p_status_scrollArea.setObjectName(u"p_status_scrollArea")
        self.p_status_scrollArea.setGeometry(QRect(0, 60, 400, 240))
        self.scrollArea_2 = QScrollArea(self.p_status_scrollArea)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 400, 240))
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setStyleSheet(u"QScrollArea{\n"
"	border:none;\n"
"	background:transparent;\n"
"\n"
"}\n"
"QScrollArea QWidget{\n"
"	background-color:transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"/**/\n"
"\n"
"QScrollBar:vertical {\n"
"       border:none;\n"
"       background: rgb(20,20,20);\n"
"		width:10px;\n"
"   }\n"
"   QScrollBar::handle:vertical {\n"
"       background: rgb(255, 24, 24);\n"
"		border-radius:5px;\n"
"     \n"
"   }\n"
"  \n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical  {\n"
"       background: none;\n"
"\n"
"   }\n"
"\n"
"")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 400, 240))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 40, 370, 50))
        self.label_55 = QLabel(self.frame_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(10, 0, 200, 50))
        self.label_55.setMaximumSize(QSize(250, 16777215))
        self.label_55.setFont(font1)
        self.label_55.setStyleSheet(u"color:white;")
        self.bearing_statusBtButton = QPushButton(self.frame_7)
        self.bearing_statusBtButton.setObjectName(u"bearing_statusBtButton")
        self.bearing_statusBtButton.setGeometry(QRect(270, 10, 100, 30))
        self.bearing_statusBtButton.setFont(font3)
        self.bearing_statusBtButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_statusBtButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:15px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 370, 40))
        self.label_56 = QLabel(self.frame_6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 0, 190, 40))
        self.label_56.setFont(font1)
        self.label_56.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_statusBtText = QLabel(self.frame_6)
        self.bearing_statusBtText.setObjectName(u"bearing_statusBtText")
        self.bearing_statusBtText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_statusBtText.setFont(font1)
        self.bearing_statusBtText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_statusBtText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.stackedWidget_settings.addWidget(self.page_status)
        self.page_gpio = QWidget()
        self.page_gpio.setObjectName(u"page_gpio")
        self.p_gpio_title = QFrame(self.page_gpio)
        self.p_gpio_title.setObjectName(u"p_gpio_title")
        self.p_gpio_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_64 = QLabel(self.p_gpio_title)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(10, 10, 380, 40))
        self.label_64.setFont(font)
        self.label_64.setStyleSheet(u"color:white;")
        self.label_64.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_21 = QFrame(self.p_gpio_title)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(10, 50, 380, 2))
        self.line_21.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_21.setFrameShadow(QFrame.Plain)
        self.line_21.setFrameShape(QFrame.HLine)
        self.p_gpio_setPin = QFrame(self.page_gpio)
        self.p_gpio_setPin.setObjectName(u"p_gpio_setPin")
        self.p_gpio_setPin.setGeometry(QRect(0, 60, 370, 40))
        self.bearing_gpioSetValueInput = QLineEdit(self.p_gpio_setPin)
        self.bearing_gpioSetValueInput.setObjectName(u"bearing_gpioSetValueInput")
        self.bearing_gpioSetValueInput.setGeometry(QRect(280, 5, 50, 30))
        self.bearing_gpioSetValueInput.setFont(font4)
        self.bearing_gpioSetValueInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	color:white;\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	\n"
"	\n"
"	border:1px solid rgb(97, 97, 97);\n"
"}")
        self.bearing_gpioSetValueInput.setMaxLength(3)
        self.bearing_gpioSetValueInput.setAlignment(Qt.AlignCenter)
        self.label_65 = QLabel(self.p_gpio_setPin)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(10, 5, 180, 30))
        self.label_65.setMaximumSize(QSize(250, 16777215))
        self.label_65.setFont(font1)
        self.label_65.setStyleSheet(u"color:white;")
        self.bearing_gpioSetButton = QPushButton(self.p_gpio_setPin)
        self.bearing_gpioSetButton.setObjectName(u"bearing_gpioSetButton")
        self.bearing_gpioSetButton.setGeometry(QRect(340, 5, 30, 30))
        self.bearing_gpioSetButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_gpioSetButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}")
        self.bearing_gpioSetButton.setIcon(icon)
        self.bearing_gpioSetButton.setIconSize(QSize(18, 18))
        self.bearing_gpioSetPinInput = QLineEdit(self.p_gpio_setPin)
        self.bearing_gpioSetPinInput.setObjectName(u"bearing_gpioSetPinInput")
        self.bearing_gpioSetPinInput.setGeometry(QRect(220, 5, 50, 30))
        self.bearing_gpioSetPinInput.setFont(font4)
        self.bearing_gpioSetPinInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	color:white;\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	\n"
"	\n"
"	border:1px solid rgb(97, 97, 97);\n"
"}")
        self.bearing_gpioSetPinInput.setMaxLength(3)
        self.bearing_gpioSetPinInput.setAlignment(Qt.AlignCenter)
        self.p_gpio_setPin_2 = QFrame(self.page_gpio)
        self.p_gpio_setPin_2.setObjectName(u"p_gpio_setPin_2")
        self.p_gpio_setPin_2.setGeometry(QRect(0, 100, 370, 40))
        self.bearing_gpioGetInput = QLineEdit(self.p_gpio_setPin_2)
        self.bearing_gpioGetInput.setObjectName(u"bearing_gpioGetInput")
        self.bearing_gpioGetInput.setGeometry(QRect(280, 5, 50, 30))
        self.bearing_gpioGetInput.setFont(font4)
        self.bearing_gpioGetInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	color:white;\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	\n"
"	\n"
"	border:1px solid rgb(97, 97, 97);\n"
"}")
        self.bearing_gpioGetInput.setMaxLength(3)
        self.bearing_gpioGetInput.setAlignment(Qt.AlignCenter)
        self.label_66 = QLabel(self.p_gpio_setPin_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(10, 5, 180, 30))
        self.label_66.setMaximumSize(QSize(250, 16777215))
        self.label_66.setFont(font1)
        self.label_66.setStyleSheet(u"color:white;")
        self.bearing_gpioGetButton = QPushButton(self.p_gpio_setPin_2)
        self.bearing_gpioGetButton.setObjectName(u"bearing_gpioGetButton")
        self.bearing_gpioGetButton.setGeometry(QRect(340, 5, 30, 30))
        self.bearing_gpioGetButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_gpioGetButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}")
        self.bearing_gpioGetButton.setIcon(icon)
        self.bearing_gpioGetButton.setIconSize(QSize(18, 18))
        self.frame_8 = QFrame(self.page_gpio)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 140, 370, 20))
        self.line_3 = QFrame(self.frame_8)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 10, 360, 1))
        self.line_3.setStyleSheet(u"border:none;\n"
"background:gray;")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)
        self.frame_22 = QFrame(self.page_gpio)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 200, 370, 40))
        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 0, 190, 40))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_gpioPinValueLabel = QLabel(self.frame_22)
        self.bearing_gpioPinValueLabel.setObjectName(u"bearing_gpioPinValueLabel")
        self.bearing_gpioPinValueLabel.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_gpioPinValueLabel.setFont(font1)
        self.bearing_gpioPinValueLabel.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_gpioPinValueLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_28 = QFrame(self.page_gpio)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(0, 160, 370, 40))
        self.bearing_gpioPinLabel = QLabel(self.frame_28)
        self.bearing_gpioPinLabel.setObjectName(u"bearing_gpioPinLabel")
        self.bearing_gpioPinLabel.setGeometry(QRect(10, 5, 270, 30))
        self.bearing_gpioPinLabel.setMaximumSize(QSize(9999999, 16777215))
        self.bearing_gpioPinLabel.setFont(font1)
        self.bearing_gpioPinLabel.setStyleSheet(u"color:red;")
        self.stackedWidget_settings.addWidget(self.page_gpio)
        self.page_systemInfo = QWidget()
        self.page_systemInfo.setObjectName(u"page_systemInfo")
        self.p_systemInfo_scrollArea = QFrame(self.page_systemInfo)
        self.p_systemInfo_scrollArea.setObjectName(u"p_systemInfo_scrollArea")
        self.p_systemInfo_scrollArea.setGeometry(QRect(0, 60, 400, 240))
        self.scrollArea_4 = QScrollArea(self.p_systemInfo_scrollArea)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 0, 400, 240))
        self.scrollArea_4.setStyleSheet(u"QScrollArea{\n"
"	border:none;\n"
"	background:transparent;\n"
"\n"
"}\n"
"QScrollArea QWidget#scrollAreaWidgetContents_7{\n"
"	background-color:rgb(20,20,20);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/**/\n"
"\n"
"QScrollBar:vertical {\n"
"       border:none;\n"
"       background: rgb(20,20,20);\n"
"		width:10px;\n"
"   }\n"
"   QScrollBar::handle:vertical {\n"
"       background: rgb(255, 24, 24);\n"
"		border-radius:5px;\n"
"     \n"
"   }\n"
"  \n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical  {\n"
"       background: none;\n"
"\n"
"   }\n"
"\n"
"")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 398, 440))
        self.scrollAreaWidgetContents_7.setMinimumSize(QSize(0, 440))
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 120, 370, 40))
        self.label_78 = QLabel(self.frame_10)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(10, 5, 270, 30))
        self.label_78.setMaximumSize(QSize(9999999, 16777215))
        self.label_78.setFont(font1)
        self.label_78.setStyleSheet(u"color:red;")
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 160, 370, 40))
        self.label_79 = QLabel(self.frame_17)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(10, 0, 190, 40))
        self.label_79.setFont(font1)
        self.label_79.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemRamUsedText = QLabel(self.frame_17)
        self.bearing_systemRamUsedText.setObjectName(u"bearing_systemRamUsedText")
        self.bearing_systemRamUsedText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemRamUsedText.setFont(font1)
        self.bearing_systemRamUsedText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemRamUsedText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_18 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(0, 200, 370, 40))
        self.label_81 = QLabel(self.frame_18)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(10, 0, 190, 40))
        self.label_81.setFont(font1)
        self.label_81.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemRamFreeText = QLabel(self.frame_18)
        self.bearing_systemRamFreeText.setObjectName(u"bearing_systemRamFreeText")
        self.bearing_systemRamFreeText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemRamFreeText.setFont(font1)
        self.bearing_systemRamFreeText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemRamFreeText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_19 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(0, 240, 370, 40))
        self.label_83 = QLabel(self.frame_19)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(10, 0, 190, 40))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemRamTotalText = QLabel(self.frame_19)
        self.bearing_systemRamTotalText.setObjectName(u"bearing_systemRamTotalText")
        self.bearing_systemRamTotalText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemRamTotalText.setFont(font1)
        self.bearing_systemRamTotalText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemRamTotalText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_20 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 40, 370, 40))
        self.label_85 = QLabel(self.frame_20)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(10, 0, 190, 40))
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemCpuUseText = QLabel(self.frame_20)
        self.bearing_systemCpuUseText.setObjectName(u"bearing_systemCpuUseText")
        self.bearing_systemCpuUseText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemCpuUseText.setFont(font1)
        self.bearing_systemCpuUseText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemCpuUseText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_21 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(0, 0, 370, 40))
        self.label_87 = QLabel(self.frame_21)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(10, 10, 270, 30))
        self.label_87.setMaximumSize(QSize(9999999, 16777215))
        self.label_87.setFont(font1)
        self.label_87.setStyleSheet(u"color:red;")
        self.frame_23 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(0, 280, 370, 40))
        self.label_98 = QLabel(self.frame_23)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(10, 5, 270, 30))
        self.label_98.setMaximumSize(QSize(9999999, 16777215))
        self.label_98.setFont(font1)
        self.label_98.setStyleSheet(u"color:red;")
        self.frame_24 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 320, 370, 40))
        self.label_99 = QLabel(self.frame_24)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(10, 0, 190, 40))
        self.label_99.setFont(font1)
        self.label_99.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemDiskUsedText = QLabel(self.frame_24)
        self.bearing_systemDiskUsedText.setObjectName(u"bearing_systemDiskUsedText")
        self.bearing_systemDiskUsedText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemDiskUsedText.setFont(font1)
        self.bearing_systemDiskUsedText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemDiskUsedText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_25 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(0, 360, 370, 40))
        self.label_101 = QLabel(self.frame_25)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(10, 0, 190, 40))
        self.label_101.setFont(font1)
        self.label_101.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemDiskFreeText = QLabel(self.frame_25)
        self.bearing_systemDiskFreeText.setObjectName(u"bearing_systemDiskFreeText")
        self.bearing_systemDiskFreeText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemDiskFreeText.setFont(font1)
        self.bearing_systemDiskFreeText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemDiskFreeText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_26 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(0, 400, 370, 40))
        self.label_103 = QLabel(self.frame_26)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(10, 0, 190, 40))
        self.label_103.setFont(font1)
        self.label_103.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemDiskTotalText = QLabel(self.frame_26)
        self.bearing_systemDiskTotalText.setObjectName(u"bearing_systemDiskTotalText")
        self.bearing_systemDiskTotalText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemDiskTotalText.setFont(font1)
        self.bearing_systemDiskTotalText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemDiskTotalText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_27 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(0, 80, 370, 40))
        self.label_105 = QLabel(self.frame_27)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(10, 0, 190, 40))
        self.label_105.setFont(font1)
        self.label_105.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.bearing_systemCpuTempText = QLabel(self.frame_27)
        self.bearing_systemCpuTempText.setObjectName(u"bearing_systemCpuTempText")
        self.bearing_systemCpuTempText.setGeometry(QRect(190, 0, 180, 40))
        self.bearing_systemCpuTempText.setFont(font1)
        self.bearing_systemCpuTempText.setStyleSheet(u"QLabel{\n"
"	color:gray;\n"
"}")
        self.bearing_systemCpuTempText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_7)
        self.p_systemInfo_title = QFrame(self.page_systemInfo)
        self.p_systemInfo_title.setObjectName(u"p_systemInfo_title")
        self.p_systemInfo_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_67 = QLabel(self.p_systemInfo_title)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(10, 10, 330, 40))
        self.label_67.setFont(font)
        self.label_67.setStyleSheet(u"color:white;")
        self.label_67.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_22 = QFrame(self.p_systemInfo_title)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setGeometry(QRect(10, 50, 380, 2))
        self.line_22.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setFrameShape(QFrame.HLine)
        self.bearing_systemRefreshButton = QPushButton(self.p_systemInfo_title)
        self.bearing_systemRefreshButton.setObjectName(u"bearing_systemRefreshButton")
        self.bearing_systemRefreshButton.setGeometry(QRect(350, 10, 40, 40))
        self.bearing_systemRefreshButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_systemRefreshButton.setStyleSheet(u"border:none;\n"
"background:none;")
        self.bearing_systemRefreshButton.setIcon(icon1)
        self.bearing_systemRefreshButton.setIconSize(QSize(24, 24))
        self.stackedWidget_settings.addWidget(self.page_systemInfo)
        self.page_terminal = QWidget()
        self.page_terminal.setObjectName(u"page_terminal")
        self.p_terminal_title = QFrame(self.page_terminal)
        self.p_terminal_title.setObjectName(u"p_terminal_title")
        self.p_terminal_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_107 = QLabel(self.p_terminal_title)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(10, 10, 380, 40))
        self.label_107.setFont(font)
        self.label_107.setStyleSheet(u"color:white;")
        self.label_107.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_23 = QFrame(self.p_terminal_title)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(10, 50, 380, 2))
        self.line_23.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_23.setFrameShadow(QFrame.Plain)
        self.line_23.setFrameShape(QFrame.HLine)
        self.frame = QFrame(self.page_terminal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 60, 370, 50))
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 0, 200, 50))
        self.label_16.setMaximumSize(QSize(250, 16777215))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color:white;")
        self.bearing_terminalOpenButton = QPushButton(self.frame)
        self.bearing_terminalOpenButton.setObjectName(u"bearing_terminalOpenButton")
        self.bearing_terminalOpenButton.setGeometry(QRect(270, 10, 100, 30))
        self.bearing_terminalOpenButton.setFont(font3)
        self.bearing_terminalOpenButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_terminalOpenButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:15px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")
        self.stackedWidget_settings.addWidget(self.page_terminal)
        self.page_advanced = QWidget()
        self.page_advanced.setObjectName(u"page_advanced")
        self.frame_page_advanced = QFrame(self.page_advanced)
        self.frame_page_advanced.setObjectName(u"frame_page_advanced")
        self.frame_page_advanced.setGeometry(QRect(0, 0, 400, 300))
        self.p_advanced_title = QFrame(self.frame_page_advanced)
        self.p_advanced_title.setObjectName(u"p_advanced_title")
        self.p_advanced_title.setGeometry(QRect(0, 0, 400, 60))
        self.label_109 = QLabel(self.p_advanced_title)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(10, 10, 380, 40))
        self.label_109.setFont(font)
        self.label_109.setStyleSheet(u"color:white;")
        self.label_109.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_24 = QFrame(self.p_advanced_title)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setGeometry(QRect(10, 50, 380, 2))
        self.line_24.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_24.setFrameShadow(QFrame.Plain)
        self.line_24.setFrameShape(QFrame.HLine)
        self.p_advanced_separator = QFrame(self.frame_page_advanced)
        self.p_advanced_separator.setObjectName(u"p_advanced_separator")
        self.p_advanced_separator.setGeometry(QRect(0, 140, 370, 20))
        self.line_25 = QFrame(self.p_advanced_separator)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setGeometry(QRect(10, 10, 360, 1))
        self.line_25.setStyleSheet(u"border:none;\n"
"background:gray;")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setFrameShape(QFrame.HLine)
        self.p_advanced_reboot = QFrame(self.frame_page_advanced)
        self.p_advanced_reboot.setObjectName(u"p_advanced_reboot")
        self.p_advanced_reboot.setGeometry(QRect(0, 160, 370, 50))
        self.label_116 = QLabel(self.p_advanced_reboot)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(10, 0, 200, 50))
        self.label_116.setMaximumSize(QSize(250, 16777215))
        self.label_116.setFont(font1)
        self.label_116.setStyleSheet(u"color:white;")
        self.bearing_advancedRebootButton = QPushButton(self.p_advanced_reboot)
        self.bearing_advancedRebootButton.setObjectName(u"bearing_advancedRebootButton")
        self.bearing_advancedRebootButton.setGeometry(QRect(270, 10, 100, 30))
        self.bearing_advancedRebootButton.setFont(font3)
        self.bearing_advancedRebootButton.setFocusPolicy(Qt.NoFocus)
        self.bearing_advancedRebootButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: 2px solid rgb(181, 0, 0);\n"
"	border-radius:15px;\n"
"	color:gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(188, 0, 0);\n"
"	color:white;\n"
"}")
        self.p_advanced_autoPower = QFrame(self.frame_page_advanced)
        self.p_advanced_autoPower.setObjectName(u"p_advanced_autoPower")
        self.p_advanced_autoPower.setGeometry(QRect(0, 60, 370, 40))
        self.label_113 = QLabel(self.p_advanced_autoPower)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(10, 5, 240, 30))
        self.label_113.setMaximumSize(QSize(250, 16777215))
        self.label_113.setFont(font1)
        self.label_113.setStyleSheet(u"color:white;")
        self.frame_cb_8 = QFrame(self.p_advanced_autoPower)
        self.frame_cb_8.setObjectName(u"frame_cb_8")
        self.frame_cb_8.setGeometry(QRect(310, 0, 60, 40))
        self.a_border_7 = QFrame(self.frame_cb_8)
        self.a_border_7.setObjectName(u"a_border_7")
        self.a_border_7.setGeometry(QRect(0, 5, 60, 30))
        self.a_border_7.setStyleSheet(u"QFrame{\n"
"	border-radius:15px;\n"
"	border:2px solid gray; \n"
"	border-color: rgb(211, 211, 211);\n"
"}\n"
"QLabel{\n"
"	border:none; \n"
"	color:white;\n"
"	margin-bottom:1px;\n"
"}")
        self.a_border_7.setFrameShape(QFrame.StyledPanel)
        self.a_border_7.setFrameShadow(QFrame.Raised)
        self.label_114 = QLabel(self.a_border_7)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(0, 0, 30, 30))
        self.label_114.setFont(font2)
        self.label_114.setAlignment(Qt.AlignCenter)
        self.label_115 = QLabel(self.a_border_7)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(30, 0, 30, 30))
        self.label_115.setFont(font2)
        self.label_115.setAlignment(Qt.AlignCenter)
        self.bearing_advancedAutopowerCheckbox = QCheckBox(self.frame_cb_8)
        self.bearing_advancedAutopowerCheckbox.setObjectName(u"bearing_advancedAutopowerCheckbox")
        self.bearing_advancedAutopowerCheckbox.setGeometry(QRect(0, 0, 60, 40))
        self.bearing_advancedAutopowerCheckbox.setFocusPolicy(Qt.NoFocus)
        self.bearing_advancedAutopowerCheckbox.setStyleSheet(u"QCheckBox{\n"
"	background:none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	height:20px;\n"
"	width:20px;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	margin-left:6px;\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	margin-left:30px;\n"
"	background:rgb(54, 0, 0);\n"
"\n"
"	\n"
"}")
        self.p_advanced_autoPower_2 = QFrame(self.frame_page_advanced)
        self.p_advanced_autoPower_2.setObjectName(u"p_advanced_autoPower_2")
        self.p_advanced_autoPower_2.setGeometry(QRect(0, 100, 370, 40))
        self.label_117 = QLabel(self.p_advanced_autoPower_2)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(10, 5, 240, 30))
        self.label_117.setMaximumSize(QSize(250, 16777215))
        self.label_117.setFont(font1)
        self.label_117.setStyleSheet(u"color:white;")
        self.frame_cb_9 = QFrame(self.p_advanced_autoPower_2)
        self.frame_cb_9.setObjectName(u"frame_cb_9")
        self.frame_cb_9.setGeometry(QRect(310, 0, 60, 40))
        self.a_border_8 = QFrame(self.frame_cb_9)
        self.a_border_8.setObjectName(u"a_border_8")
        self.a_border_8.setGeometry(QRect(0, 5, 60, 30))
        self.a_border_8.setStyleSheet(u"QFrame{\n"
"	border-radius:15px;\n"
"	border:2px solid gray; \n"
"	border-color: rgb(211, 211, 211);\n"
"}\n"
"QLabel{\n"
"	border:none; \n"
"	color:white;\n"
"	margin-bottom:1px;\n"
"}")
        self.a_border_8.setFrameShape(QFrame.StyledPanel)
        self.a_border_8.setFrameShadow(QFrame.Raised)
        self.label_118 = QLabel(self.a_border_8)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(0, 0, 30, 30))
        self.label_118.setFont(font2)
        self.label_118.setAlignment(Qt.AlignCenter)
        self.label_119 = QLabel(self.a_border_8)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(30, 0, 30, 30))
        self.label_119.setFont(font2)
        self.label_119.setAlignment(Qt.AlignCenter)
        self.bearing_advancedGaugePowerCheckbox = QCheckBox(self.frame_cb_9)
        self.bearing_advancedGaugePowerCheckbox.setObjectName(u"bearing_advancedGaugePowerCheckbox")
        self.bearing_advancedGaugePowerCheckbox.setGeometry(QRect(0, 0, 60, 40))
        self.bearing_advancedGaugePowerCheckbox.setFocusPolicy(Qt.NoFocus)
        self.bearing_advancedGaugePowerCheckbox.setStyleSheet(u"QCheckBox{\n"
"	background:none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	height:20px;\n"
"	width:20px;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	margin-left:6px;\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	margin-left:30px;\n"
"	background:rgb(54, 0, 0);\n"
"\n"
"	\n"
"}")
        self.stackedWidget_settings.addWidget(self.page_advanced)

        self.retranslateUi(Settings_widget)

        self.stackedWidget_settings.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Settings_widget)
    # setupUi

    def retranslateUi(self, Settings_widget):
        Settings_widget.setWindowTitle(QCoreApplication.translate("Settings_widget", u"Form", None))
        self.bearing_settingsBrightness.setText(QCoreApplication.translate("Settings_widget", u"BRIGHTNESS", None))
        self.bearing_settingsWifi.setText(QCoreApplication.translate("Settings_widget", u"WIFI", None))
        self.bearing_settingsBluetooth.setText(QCoreApplication.translate("Settings_widget", u"BLUETOOTH", None))
        self.bearing_settingsRemote.setText(QCoreApplication.translate("Settings_widget", u"REMOTE", None))
        self.bearing_settingsNavigator.setText(QCoreApplication.translate("Settings_widget", u"NAVIGATOR", None))
        self.bearing_settingsStatus.setText(QCoreApplication.translate("Settings_widget", u"STATUS", None))
        self.bearing_settingsGpio.setText(QCoreApplication.translate("Settings_widget", u"GPIO", None))
        self.bearing_settingsSystemInfo.setText(QCoreApplication.translate("Settings_widget", u"SYSTEM INFO", None))
        self.bearing_settingsTerminal.setText(QCoreApplication.translate("Settings_widget", u"TERMINAL", None))
        self.bearing_settingsAdvanced.setText(QCoreApplication.translate("Settings_widget", u"ADVANCED", None))
        self.label_13.setText(QCoreApplication.translate("Settings_widget", u"Brightness", None))
        self.label_37.setText(QCoreApplication.translate("Settings_widget", u"Level", None))
        self.label_2.setText(QCoreApplication.translate("Settings_widget", u"Power", None))
        self.label_5.setText(QCoreApplication.translate("Settings_widget", u"O", None))
        self.label_6.setText(QCoreApplication.translate("Settings_widget", u"I", None))
        self.bearing_wifiPowerCheckbox.setText("")
        self.label_14.setText(QCoreApplication.translate("Settings_widget", u"IP:", None))
        self.bearing_wifiIpText.setText(QCoreApplication.translate("Settings_widget", u"None", None))
        self.label_9.setText(QCoreApplication.translate("Settings_widget", u"SSID:", None))
        self.bearing_wifiSsidText.setText(QCoreApplication.translate("Settings_widget", u"None", None))
        self.label_7.setText(QCoreApplication.translate("Settings_widget", u"Connect", None))
        self.bearing_wifiSSIDInput.setPlaceholderText(QCoreApplication.translate("Settings_widget", u"Network", None))
        self.label_11.setText(QCoreApplication.translate("Settings_widget", u"Name", None))
        self.bearing_wifiPassInput.setPlaceholderText(QCoreApplication.translate("Settings_widget", u"Password", None))
        self.bearing_wifiPassLabel.setText(QCoreApplication.translate("Settings_widget", u"Password", None))
        self.bearing_wifiPassButton.setText("")
        self.label_25.setText(QCoreApplication.translate("Settings_widget", u"WIFI", None))
        self.bearing_refreshWifiButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Settings_widget", u"Power", None))
        self.label_8.setText(QCoreApplication.translate("Settings_widget", u"O", None))
        self.label_18.setText(QCoreApplication.translate("Settings_widget", u"I", None))
        self.bearing_btPowerCheckbox.setText("")
        self.label_21.setText(QCoreApplication.translate("Settings_widget", u"Discoverable", None))
        self.label_22.setText(QCoreApplication.translate("Settings_widget", u"O", None))
        self.label_23.setText(QCoreApplication.translate("Settings_widget", u"I", None))
        self.bearing_btDiscoverableCheckbox.setText("")
        self.label_27.setText(QCoreApplication.translate("Settings_widget", u"BT Name", None))
        self.bearing_btNameText.setText(QCoreApplication.translate("Settings_widget", u"None", None))
        self.label_29.setText(QCoreApplication.translate("Settings_widget", u"Connected device", None))
        self.bearing_btConnectedText.setText(QCoreApplication.translate("Settings_widget", u"None", None))
        self.label_31.setText(QCoreApplication.translate("Settings_widget", u"Bluetooth manager", None))
        self.bearing_btManagerButton.setText(QCoreApplication.translate("Settings_widget", u"BTManager", None))
        self.label_26.setText(QCoreApplication.translate("Settings_widget", u"Bluetooth", None))
        self.bearing_refreshBtButton.setText("")
        self.label_32.setText(QCoreApplication.translate("Settings_widget", u"Remote", None))
        self.label_4.setText(QCoreApplication.translate("Settings_widget", u"Multimedia remote", None))
        self.label_10.setText(QCoreApplication.translate("Settings_widget", u"O", None))
        self.label_12.setText(QCoreApplication.translate("Settings_widget", u"I", None))
        self.bearing_remoteMultimediaCheckbox.setText("")
        self.label_33.setText(QCoreApplication.translate("Settings_widget", u"Navigator", None))
        self.label_17.setText(QCoreApplication.translate("Settings_widget", u"Set home", None))
        self.bearing_navigatorHomeButton.setText("")
        self.label_38.setText(QCoreApplication.translate("Settings_widget", u"Services status", None))
        self.bearing_statusRefreshButton.setText("")
        self.label_55.setText(QCoreApplication.translate("Settings_widget", u"Restart bluetooth", None))
        self.bearing_statusBtButton.setText(QCoreApplication.translate("Settings_widget", u"Restart", None))
        self.label_56.setText(QCoreApplication.translate("Settings_widget", u"Bluetooth", None))
        self.bearing_statusBtText.setText(QCoreApplication.translate("Settings_widget", u"None", None))
        self.label_64.setText(QCoreApplication.translate("Settings_widget", u"GPIO", None))
        self.bearing_gpioSetValueInput.setPlaceholderText(QCoreApplication.translate("Settings_widget", u"--", None))
        self.label_65.setText(QCoreApplication.translate("Settings_widget", u"Set pin", None))
        self.bearing_gpioSetButton.setText("")
        self.bearing_gpioSetPinInput.setPlaceholderText(QCoreApplication.translate("Settings_widget", u"--", None))
        self.bearing_gpioGetInput.setPlaceholderText(QCoreApplication.translate("Settings_widget", u"--", None))
        self.label_66.setText(QCoreApplication.translate("Settings_widget", u"Get pin", None))
        self.bearing_gpioGetButton.setText("")
        self.label_15.setText(QCoreApplication.translate("Settings_widget", u"Pin value", None))
        self.bearing_gpioPinValueLabel.setText(QCoreApplication.translate("Settings_widget", u"No data", None))
        self.bearing_gpioPinLabel.setText(QCoreApplication.translate("Settings_widget", u"Pin: None", None))
        self.label_78.setText(QCoreApplication.translate("Settings_widget", u"RAM", None))
        self.label_79.setText(QCoreApplication.translate("Settings_widget", u"Used", None))
        self.bearing_systemRamUsedText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_81.setText(QCoreApplication.translate("Settings_widget", u"Free", None))
        self.bearing_systemRamFreeText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_83.setText(QCoreApplication.translate("Settings_widget", u"Total", None))
        self.bearing_systemRamTotalText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_85.setText(QCoreApplication.translate("Settings_widget", u"Use", None))
        self.bearing_systemCpuUseText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_87.setText(QCoreApplication.translate("Settings_widget", u"CPU", None))
        self.label_98.setText(QCoreApplication.translate("Settings_widget", u"Disk", None))
        self.label_99.setText(QCoreApplication.translate("Settings_widget", u"Used", None))
        self.bearing_systemDiskUsedText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_101.setText(QCoreApplication.translate("Settings_widget", u"Free", None))
        self.bearing_systemDiskFreeText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_103.setText(QCoreApplication.translate("Settings_widget", u"Total", None))
        self.bearing_systemDiskTotalText.setText(QCoreApplication.translate("Settings_widget", u"0GB", None))
        self.label_105.setText(QCoreApplication.translate("Settings_widget", u"Temp", None))
        self.bearing_systemCpuTempText.setText(QCoreApplication.translate("Settings_widget", u"0\u00baC", None))
        self.label_67.setText(QCoreApplication.translate("Settings_widget", u"SYSTEM INFO", None))
        self.bearing_systemRefreshButton.setText("")
        self.label_107.setText(QCoreApplication.translate("Settings_widget", u"Terminal", None))
        self.label_16.setText(QCoreApplication.translate("Settings_widget", u"Open terminal", None))
        self.bearing_terminalOpenButton.setText(QCoreApplication.translate("Settings_widget", u"Open", None))
        self.label_109.setText(QCoreApplication.translate("Settings_widget", u"ADVANCED", None))
        self.label_116.setText(QCoreApplication.translate("Settings_widget", u" Reboot now", None))
        self.bearing_advancedRebootButton.setText(QCoreApplication.translate("Settings_widget", u"Reboot", None))
        self.label_113.setText(QCoreApplication.translate("Settings_widget", u"Auto-power", None))
        self.label_114.setText(QCoreApplication.translate("Settings_widget", u"O", None))
        self.label_115.setText(QCoreApplication.translate("Settings_widget", u"I", None))
        self.bearing_advancedAutopowerCheckbox.setText("")
        self.label_117.setText(QCoreApplication.translate("Settings_widget", u"Gauge power", None))
        self.label_118.setText(QCoreApplication.translate("Settings_widget", u"O", None))
        self.label_119.setText(QCoreApplication.translate("Settings_widget", u"I", None))
        self.bearing_advancedGaugePowerCheckbox.setText("")
    # retranslateUi

