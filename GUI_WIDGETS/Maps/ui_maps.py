# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapsvScahR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Maps_widget(object):
    def setupUi(self, Maps_widget):
        if not Maps_widget.objectName():
            Maps_widget.setObjectName(u"Maps_widget")
        Maps_widget.resize(800, 480)
        self.frame_maps = QFrame(Maps_widget)
        self.frame_maps.setObjectName(u"frame_maps")
        self.frame_maps.setGeometry(QRect(0, 0, 800, 480))
        self.frame_maps.setStyleSheet(u"#frame_maps{background:rgb(20,20,20)}")
        self.stackedWidget = QStackedWidget(self.frame_maps)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 170, 600, 200))
        font = QFont()
        font.setPointSize(17)
        self.stackedWidget.setFont(font)
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
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiLight")
        font1.setPointSize(13)
        self.label_5.setFont(font1)
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
        self.label_8.setFont(font1)
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
        self.label_20.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiLight Condensed")
        font2.setPointSize(17)
        self.label_13.setFont(font2)
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
        self.label_14.setFont(font2)
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
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight SemiConde")
        font3.setPointSize(14)
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	background:rgb(220, 0, 0);\n"
"	color:white;\n"
"	border-top-right-radius:0;\n"
"	border-bottom-right-radius:0;\n"
"}")
        self.label_15.setMargin(6)

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
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Light")
        font4.setPointSize(32)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color:white;")
        self.label_12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line_3 = QFrame(self.frame_title)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 70, 580, 2))
        self.line_3.setStyleSheet(u"background:red;\n"
"border:none;")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)
        self.mapsTitleCloseButton = QPushButton(self.frame_title)
        self.mapsTitleCloseButton.setObjectName(u"mapsTitleCloseButton")
        self.mapsTitleCloseButton.setGeometry(QRect(540, 20, 50, 50))
        self.mapsTitleCloseButton.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/icons_red/Resources/Icons/png-red/fi-rr-cross-small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mapsTitleCloseButton.setIcon(icon2)
        self.mapsTitleCloseButton.setIconSize(QSize(30, 30))

        self.retranslateUi(Maps_widget)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Maps_widget)
    # setupUi

    def retranslateUi(self, Maps_widget):
        Maps_widget.setWindowTitle(QCoreApplication.translate("Maps_widget", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Maps_widget", u"Map", None))
        self.mapsSelectMapButton.setText("")
        self.label_8.setText(QCoreApplication.translate("Maps_widget", u"Directions", None))
        self.mapsSelectDirectionsButton.setText("")
        self.label_20.setText(QCoreApplication.translate("Maps_widget", u"Home", None))
        self.mapsSelectHomeButton.setText("")
        self.label_13.setText(QCoreApplication.translate("Maps_widget", u"From", None))
        self.label_14.setText(QCoreApplication.translate("Maps_widget", u"To", None))
        self.mapsDirectionsHomeButton.setText("")
        self.mapsDirectionsGoButton.setText("")
        self.mapsHomeGoButton.setText("")
        self.label_15.setText(QCoreApplication.translate("Maps_widget", u"Ubication", None))
        self.label_12.setText(QCoreApplication.translate("Maps_widget", u"GOOGLE MAPS", None))
    # retranslateUi

