# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardNWgCby.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
import resources_rc

class Ui_Dashboard_widget(object):
    def setupUi(self, Dashboard_widget):
        if not Dashboard_widget.objectName():
            Dashboard_widget.setObjectName(u"Dashboard_widget")
        Dashboard_widget.resize(800, 480)
        self.frame_dashboard = QFrame(Dashboard_widget)
        self.frame_dashboard.setObjectName(u"frame_dashboard")
        self.frame_dashboard.setGeometry(QRect(0, 0, 800, 480))
        self.frame_dashboard.setMinimumSize(QSize(800, 480))
        self.frame_dashboard.setMaximumSize(QSize(800, 480))
        self.frame_gauge = QFrame(self.frame_dashboard)
        self.frame_gauge.setObjectName(u"frame_gauge")
        self.frame_gauge.setGeometry(QRect(0, 35, 400, 360))
        self.gaugeBackground = QFrame(self.frame_gauge)
        self.gaugeBackground.setObjectName(u"gaugeBackground")
        self.gaugeBackground.setGeometry(QRect(64, 60, 270, 270))
        self.gaugeBackground.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(20, 20, 20);\n"
"border-radius:135px;\n"
"}")
        self.gaugeInnerCircle = QFrame(self.gaugeBackground)
        self.gaugeInnerCircle.setObjectName(u"gaugeInnerCircle")
        self.gaugeInnerCircle.setGeometry(QRect(50, 50, 170, 170))
        self.gaugeInnerCircle.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	border-radius:85px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_km = QFrame(self.gaugeInnerCircle)
        self.frame_km.setObjectName(u"frame_km")
        self.frame_km.setGeometry(QRect(10, 10, 150, 150))
        self.frame_km.setMinimumSize(QSize(150, 150))
        font = QFont()
        font.setPointSize(8)
        self.frame_km.setFont(font)
        self.frame_km.setStyleSheet(u"QFrame{\n"
"	background:none; \n"
"	border-radius:75px;\n"
"	\n"
"	border:2px solid rgb(255,0,0);\n"
"}\n"
"QLabel{\n"
"	border:none;\n"
"	color:white;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.frame_km)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_kmh = QLabel(self.frame_km)
        self.label_kmh.setObjectName(u"label_kmh")
        self.label_kmh.setMinimumSize(QSize(0, 38))
        self.label_kmh.setMaximumSize(QSize(16777215, 38))
        font1 = QFont()
        font1.setFamily(u"Eras Light ITC")
        font1.setPointSize(18)
        font1.setItalic(True)
        self.label_kmh.setFont(font1)
        self.label_kmh.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label_kmh)

        self.label_vel = QLabel(self.frame_km)
        self.label_vel.setObjectName(u"label_vel")
        self.label_vel.setMinimumSize(QSize(0, 70))
        self.label_vel.setMaximumSize(QSize(9999, 9999))
        font2 = QFont()
        font2.setFamily(u"DS-Digital")
        font2.setPointSize(58)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_vel.setFont(font2)
        self.label_vel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_vel)

        self.needle = QFrame(self.gaugeBackground)
        self.needle.setObjectName(u"needle")
        self.needle.setGeometry(QRect(10, 10, 250, 250))
        self.needle.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240,stop:1.0 rgba(0,0,0,0),  stop:1.0 rgba(255, 0, 0, 255), stop:1.0 rgba(0, 0, 0, 0));\n"
"\n"
"	border-radius:125px;\n"
"}\n"
"")
        self.needle.raise_()
        self.gaugeInnerCircle.raise_()
        self.frame_nums = QFrame(self.frame_gauge)
        self.frame_nums.setObjectName(u"frame_nums")
        self.frame_nums.setGeometry(QRect(8, 8, 384, 356))
        self.vertical_layout_4 = QVBoxLayout(self.frame_nums)
        self.vertical_layout_4.setObjectName(u"vertical_layout_4")
        self.label_nums = QLabel(self.frame_nums)
        self.label_nums.setObjectName(u"label_nums")
        self.label_nums.setPixmap(QPixmap(u":/styles/Resources/speedNumbers.png"))
        self.label_nums.setScaledContents(True)

        self.vertical_layout_4.addWidget(self.label_nums)

        self.frame_nums.raise_()
        self.gaugeBackground.raise_()
        self.frame_player = QFrame(self.frame_dashboard)
        self.frame_player.setObjectName(u"frame_player")
        self.frame_player.setGeometry(QRect(470, 50, 280, 300))
        self.frame_media_data = QFrame(self.frame_player)
        self.frame_media_data.setObjectName(u"frame_media_data")
        self.frame_media_data.setGeometry(QRect(0, 140, 280, 120))
        self.frame_media_data.setStyleSheet(u"color:white;")
        self.verticalLayout_5 = QVBoxLayout(self.frame_media_data)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_cancion = QLabel(self.frame_media_data)
        self.label_cancion.setObjectName(u"label_cancion")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight")
        font3.setPointSize(14)
        font3.setKerning(True)
        self.label_cancion.setFont(font3)
        self.label_cancion.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.label_cancion.setScaledContents(False)
        self.label_cancion.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_cancion.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_cancion)

        self.label_artista = QLabel(self.frame_media_data)
        self.label_artista.setObjectName(u"label_artista")
        self.label_artista.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(12)
        self.label_artista.setFont(font4)
        self.label_artista.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.label_artista.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_artista.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_artista)

        self.slider_duration = QSlider(self.frame_player)
        self.slider_duration.setObjectName(u"slider_duration")
        self.slider_duration.setGeometry(QRect(0, 260, 280, 22))
        self.slider_duration.setMaximumSize(QSize(16777215, 30))
        self.slider_duration.setCursor(QCursor(Qt.SizeHorCursor))
        self.slider_duration.setTabletTracking(True)
        self.slider_duration.setFocusPolicy(Qt.NoFocus)
        self.slider_duration.setStyleSheet(u"\n"
"QSlider::groove:horizontal{\n"
"	height:1px;	\n"
"	width:248px;\n"
"	background:gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"	background:red;\n"
"	width:12px;\n"
"	margin:-6px;\n"
"	border-radius:6px;	\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
"	background:red;\n"
"}")
        self.slider_duration.setMaximum(100)
        self.slider_duration.setOrientation(Qt.Horizontal)
        self.frame_durationLabels = QFrame(self.frame_player)
        self.frame_durationLabels.setObjectName(u"frame_durationLabels")
        self.frame_durationLabels.setGeometry(QRect(0, 280, 280, 20))
        self.frame_durationLabels.setStyleSheet(u"color: rgb(94, 94, 94);")
        self.frame_durationLabels.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_durationLabels)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 0, 0, 0)
        self.label_currentTime = QLabel(self.frame_durationLabels)
        self.label_currentTime.setObjectName(u"label_currentTime")
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiLight")
        font5.setPointSize(10)
        self.label_currentTime.setFont(font5)
        self.label_currentTime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_currentTime)

        self.label_duration = QLabel(self.frame_durationLabels)
        self.label_duration.setObjectName(u"label_duration")
        self.label_duration.setFont(font5)
        self.label_duration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_duration)

        self.label_albumPhoto = QLabel(self.frame_player)
        self.label_albumPhoto.setObjectName(u"label_albumPhoto")
        self.label_albumPhoto.setGeometry(QRect(70, 0, 140, 140))
        self.label_albumPhoto.setMinimumSize(QSize(140, 140))
        self.label_albumPhoto.setMaximumSize(QSize(140, 140))
        self.label_albumPhoto.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.0681818 rgba(255, 255, 255, 255), stop:1 rgba(152, 152, 152, 255));\n"
"border-radius:1px;")
        self.label_albumPhoto.setPixmap(QPixmap(u":/icons_black/Resources/Icons/png-black/musical-note (1).png"))
        self.label_albumPhoto.setAlignment(Qt.AlignCenter)
        self.frame_media_data.raise_()
        self.frame_durationLabels.raise_()
        self.slider_duration.raise_()
        self.label_albumPhoto.raise_()

        self.retranslateUi(Dashboard_widget)

        QMetaObject.connectSlotsByName(Dashboard_widget)
    # setupUi

    def retranslateUi(self, Dashboard_widget):
        Dashboard_widget.setWindowTitle(QCoreApplication.translate("Dashboard_widget", u"Form", None))
        self.label_kmh.setText(QCoreApplication.translate("Dashboard_widget", u"KM/H ", None))
        self.label_vel.setText(QCoreApplication.translate("Dashboard_widget", u"0", None))
        self.label_cancion.setText(QCoreApplication.translate("Dashboard_widget", u"No data", None))
        self.label_artista.setText(QCoreApplication.translate("Dashboard_widget", u"No data", None))
        self.label_currentTime.setText(QCoreApplication.translate("Dashboard_widget", u"0:00", None))
        self.label_duration.setText(QCoreApplication.translate("Dashboard_widget", u"0:00", None))
    # retranslateUi

