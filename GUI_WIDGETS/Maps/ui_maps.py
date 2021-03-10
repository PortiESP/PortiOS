# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapsfbfTRh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Map_widget(object):
    def setupUi(self, Map_widget):
        if not Map_widget.objectName():
            Map_widget.setObjectName(u"Map_widget")
        Map_widget.resize(800, 480)
        self.frame_maps = QFrame(Map_widget)
        self.frame_maps.setObjectName(u"frame_maps")
        self.frame_maps.setGeometry(QRect(0, 0, 800, 480))
        self.frame_maps.setStyleSheet(u"#frame_maps{background:rgb(20,20,20)}")
        self.stackedWidget = QStackedWidget(self.frame_maps)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 170, 600, 200))
        self.page_select = QWidget()
        self.page_select.setObjectName(u"page_select")
        self.page_select.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"}")
        self.frame_map = QFrame(self.page_select)
        self.frame_map.setObjectName(u"frame_map")
        self.frame_map.setGeometry(QRect(0, 0, 200, 80))
        self.label_4 = QLabel(self.frame_map)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(14, 14, 50, 50))
        self.label_4.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/maps-and-flags.png"))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame_map)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(88, 16, 98, 46))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiLight")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_map)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 200, 80))
        self.label_6.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_6.setScaledContents(True)
        self.mapsSelectMapButton = QPushButton(self.frame_map)
        self.mapsSelectMapButton.setObjectName(u"mapsSelectMapButton")
        self.mapsSelectMapButton.setGeometry(QRect(0, 0, 200, 80))
        self.mapsSelectMapButton.setFocusPolicy(Qt.NoFocus)
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.mapsSelectMapButton.raise_()
        self.frame_directions = QFrame(self.page_select)
        self.frame_directions.setObjectName(u"frame_directions")
        self.frame_directions.setGeometry(QRect(200, 0, 200, 80))
        self.label_7 = QLabel(self.frame_directions)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(14, 14, 50, 50))
        self.label_7.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/direction.png"))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_directions)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(88, 16, 98, 46))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame_directions)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 200, 80))
        self.label_9.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_9.setScaledContents(True)
        self.mapsSelectDirectionsButton = QPushButton(self.frame_directions)
        self.mapsSelectDirectionsButton.setObjectName(u"mapsSelectDirectionsButton")
        self.mapsSelectDirectionsButton.setGeometry(QRect(0, 0, 200, 80))
        self.mapsSelectDirectionsButton.setFocusPolicy(Qt.NoFocus)
        self.label_9.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.mapsSelectDirectionsButton.raise_()
        self.frame_home = QFrame(self.page_select)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setGeometry(QRect(400, 0, 200, 80))
        self.label_19 = QLabel(self.frame_home)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(14, 14, 50, 50))
        self.label_19.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/home.png"))
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.frame_home)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(88, 16, 98, 46))
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.frame_home)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 200, 80))
        self.label_21.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_21.setScaledContents(True)
        self.mapsSelectHomeButton = QPushButton(self.frame_home)
        self.mapsSelectHomeButton.setObjectName(u"mapsSelectHomeButton")
        self.mapsSelectHomeButton.setGeometry(QRect(0, 0, 200, 80))
        self.mapsSelectHomeButton.setFocusPolicy(Qt.NoFocus)
        self.label_21.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.mapsSelectHomeButton.raise_()
        self.stackedWidget.addWidget(self.page_select)
        self.page_directions = QWidget()
        self.page_directions.setObjectName(u"page_directions")
        self.frame_11 = QFrame(self.page_directions)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 10, 510, 50))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;	\n"
"\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 0))
        self.label_13.setMaximumSize(QSize(0, 16777215))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiBold Condensed")
        font1.setPointSize(16)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"QLabel{\n"
"	background:rgb(220, 0, 0);\n"
"	color:white;\n"
"	border-top-right-radius:0;\n"
"	border-bottom-right-radius:0;\n"
"}")
        self.label_13.setMargin(10)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.mapsDirectionFromInput = QLineEdit(self.frame_11)
        self.mapsDirectionFromInput.setObjectName(u"mapsDirectionFromInput")
        self.mapsDirectionFromInput.setMinimumSize(QSize(0, 50))
        self.mapsDirectionFromInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	background:transparent;\n"
"	border-radius:5px;\n"
"	border-top-left-radius:0;\n"
"	border-bottom-left-radius:0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background:rgba(57,57,57,150)\n"
"}")
        self.mapsDirectionFromInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.mapsDirectionFromInput)

        self.frame_12 = QFrame(self.page_directions)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 80, 510, 50))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;	\n"
"\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 0))
        self.label_14.setMaximumSize(QSize(0, 16777215))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"QLabel{\n"
"	background:rgb(220, 0, 0);\n"
"	color:white;\n"
"	border-top-right-radius:0;\n"
"	border-bottom-right-radius:0;\n"
"}")
        self.label_14.setMargin(10)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.mapsDirectionToInput = QLineEdit(self.frame_12)
        self.mapsDirectionToInput.setObjectName(u"mapsDirectionToInput")
        self.mapsDirectionToInput.setMinimumSize(QSize(0, 50))
        self.mapsDirectionToInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	background:transparent;\n"
"	border-radius:5px;\n"
"	border-top-left-radius:0;\n"
"	border-bottom-left-radius:0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background:rgba(57,57,57,150)\n"
"}")
        self.mapsDirectionToInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.mapsDirectionToInput)

        self.mapsDirectionsHomeButton = QPushButton(self.page_directions)
        self.mapsDirectionsHomeButton.setObjectName(u"mapsDirectionsHomeButton")
        self.mapsDirectionsHomeButton.setGeometry(QRect(540, 10, 50, 50))
        self.mapsDirectionsHomeButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons_white/Resources/Icons/png-white/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mapsDirectionsHomeButton.setIcon(icon)
        self.mapsDirectionsHomeButton.setIconSize(QSize(24, 24))
        self.mapsDirectionsGoButton = QPushButton(self.page_directions)
        self.mapsDirectionsGoButton.setObjectName(u"mapsDirectionsGoButton")
        self.mapsDirectionsGoButton.setGeometry(QRect(540, 80, 50, 50))
        self.mapsDirectionsGoButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons_white/Resources/Icons/png-white/fi-rr-arrow-small-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mapsDirectionsGoButton.setIcon(icon1)
        self.mapsDirectionsGoButton.setIconSize(QSize(40, 24))
        self.stackedWidget.addWidget(self.page_directions)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.mapsHomeGoButton = QPushButton(self.page_home)
        self.mapsHomeGoButton.setObjectName(u"mapsHomeGoButton")
        self.mapsHomeGoButton.setGeometry(QRect(540, 10, 50, 50))
        self.mapsHomeGoButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background:transparent;\n"
"	border:2px solid red;\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:red;\n"
"}")
        self.mapsHomeGoButton.setIcon(icon1)
        self.mapsHomeGoButton.setIconSize(QSize(40, 24))
        self.frame_13 = QFrame(self.page_home)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 510, 50))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"	background:rgba(57, 57, 57, 150);\n"
"	border-radius:5px;	\n"
"\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setMaximumSize(QSize(0, 16777215))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	background:rgb(220, 0, 0);\n"
"	color:white;\n"
"	border-top-right-radius:0;\n"
"	border-bottom-right-radius:0;\n"
"}")
        self.label_15.setMargin(10)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.mapsHomeUbicationInput = QLineEdit(self.frame_13)
        self.mapsHomeUbicationInput.setObjectName(u"mapsHomeUbicationInput")
        self.mapsHomeUbicationInput.setMinimumSize(QSize(0, 50))
        self.mapsHomeUbicationInput.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"	background:transparent;\n"
"	border-radius:5px;\n"
"	border-top-left-radius:0;\n"
"	border-bottom-left-radius:0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background:rgba(57,57,57,150)\n"
"}")
        self.mapsHomeUbicationInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.mapsHomeUbicationInput)

        self.stackedWidget.addWidget(self.page_home)
        self.frame_title = QFrame(self.frame_maps)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setGeometry(QRect(100, 90, 600, 80))
        self.label_12 = QLabel(self.frame_title)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 380, 60))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light")
        font2.setPointSize(32)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color:white;")
        self.label_12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_3 = QFrame(self.frame_title)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 70, 580, 2))
        self.line_3.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)
        self.frame_header = QFrame(Map_widget)
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
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light Condensed")
        font3.setPointSize(25)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_clock.setFont(font3)
        self.label_clock.setStyleSheet(u"color:rgb(255,0,0);")
        self.label_clock.setAlignment(Qt.AlignCenter)
        self.bluetoothStatusButton = QPushButton(self.frame_header)
        self.bluetoothStatusButton.setObjectName(u"bluetoothStatusButton")
        self.bluetoothStatusButton.setGeometry(QRect(459, 10, 24, 24))
        self.bluetoothStatusButton.setFocusPolicy(Qt.NoFocus)
        self.bluetoothStatusButton.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/bt_icons/Resources/Icons/bt_states/bluetooth_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bluetoothStatusButton.setIcon(icon2)
        self.bluetoothStatusButton.setIconSize(QSize(22, 22))
        self.frame_footer = QFrame(Map_widget)
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
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Light Condensed")
        font4.setPointSize(8)
        self.footerButton_1.setFont(font4)
        self.footerButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_1.setMouseTracking(False)
        self.footerButton_1.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-angle-double-small-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_1.setIcon(icon3)
        self.footerButton_1.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.footerButton_1)

        self.footerButton_2 = QPushButton(self.footer_i)
        self.footerButton_2.setObjectName(u"footerButton_2")
        self.footerButton_2.setMinimumSize(QSize(0, 50))
        self.footerButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_2.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/icons_red/Resources/Icons/png-red/play-fill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_2.setIcon(icon4)
        self.footerButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.footerButton_2)

        self.footerButton_3 = QPushButton(self.footer_i)
        self.footerButton_3.setObjectName(u"footerButton_3")
        self.footerButton_3.setMinimumSize(QSize(0, 50))
        self.footerButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_3.setFocusPolicy(Qt.NoFocus)
        icon5 = QIcon()
        icon5.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-angle-double-small-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_3.setIcon(icon5)
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
        self.footerButton_4.setFocusPolicy(Qt.NoFocus)
        icon6 = QIcon()
        icon6.addFile(u":/icons_red/Resources/Icons/png-red/icons-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_4.setIcon(icon6)
        self.footerButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.footerButton_4)

        self.footerButton_5 = QPushButton(self.footer_d)
        self.footerButton_5.setObjectName(u"footerButton_5")
        self.footerButton_5.setMinimumSize(QSize(0, 50))
        self.footerButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_5.setFocusPolicy(Qt.NoFocus)
        icon7 = QIcon()
        icon7.addFile(u":/icons_red/Resources/Icons/png-red/levels.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_5.setIcon(icon7)
        self.footerButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.footerButton_5)

        self.footerButton_6 = QPushButton(self.footer_d)
        self.footerButton_6.setObjectName(u"footerButton_6")
        self.footerButton_6.setMinimumSize(QSize(0, 50))
        self.footerButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.footerButton_6.setFocusPolicy(Qt.NoFocus)
        icon8 = QIcon()
        icon8.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footerButton_6.setIcon(icon8)
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
        self.frame_logo = QFrame(Map_widget)
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


        self.retranslateUi(Map_widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Map_widget)
    # setupUi

    def retranslateUi(self, Map_widget):
        Map_widget.setWindowTitle(QCoreApplication.translate("Map_widget", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Map_widget", u"Map", None))
        self.mapsSelectMapButton.setText("")
        self.label_8.setText(QCoreApplication.translate("Map_widget", u"Directions", None))
        self.mapsSelectDirectionsButton.setText("")
        self.label_20.setText(QCoreApplication.translate("Map_widget", u"Home", None))
        self.mapsSelectHomeButton.setText("")
        self.label_13.setText(QCoreApplication.translate("Map_widget", u"From", None))
        self.label_14.setText(QCoreApplication.translate("Map_widget", u"To", None))
        self.mapsDirectionsHomeButton.setText("")
        self.mapsDirectionsGoButton.setText("")
        self.mapsHomeGoButton.setText("")
        self.label_15.setText(QCoreApplication.translate("Map_widget", u"Ubication", None))
        self.label_12.setText(QCoreApplication.translate("Map_widget", u"GOOGLE MAPS", None))
        self.label_clock.setText(QCoreApplication.translate("Map_widget", u"23:23", None))
        self.bluetoothStatusButton.setText("")
        self.footer_background.setText("")
    # retranslateUi

