# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_playereCvDwh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Player_widget(object):
    def setupUi(self, Player_widget):
        if not Player_widget.objectName():
            Player_widget.setObjectName(u"Player_widget")
        Player_widget.resize(800, 480)
        self.frame_player = QFrame(Player_widget)
        self.frame_player.setObjectName(u"frame_player")
        self.frame_player.setGeometry(QRect(0, 0, 800, 480))
        self.frame_player.setStyleSheet(u"background:none;")
        self.frame_2 = QFrame(self.frame_player)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(100, 340, 600, 50))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background:none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        icon = QIcon()
        icon.addFile(u":/icons_red/Resources/Icons/png-red/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons_red/Resources/Icons/png-red/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons_red/Resources/Icons/png-red/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        icon3 = QIcon()
        icon3.addFile(u":/icons_red/Resources/Icons/png-red/fast-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        icon4 = QIcon()
        icon4.addFile(u":/icons_red/Resources/Icons/png-red/next-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.frame_3 = QFrame(self.frame_player)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(100, 300, 600, 40))
        self.horizontalSlider = QSlider(self.frame_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(100, 5, 400, 20))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{\n"
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
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.frame_durationLabels = QFrame(self.frame_3)
        self.frame_durationLabels.setObjectName(u"frame_durationLabels")
        self.frame_durationLabels.setGeometry(QRect(120, 20, 360, 20))
        self.frame_durationLabels.setStyleSheet(u"color: rgb(94, 94, 94);")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_durationLabels)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_currentTime = QLabel(self.frame_durationLabels)
        self.label_currentTime.setObjectName(u"label_currentTime")
        font = QFont()
        font.setFamily(u"Bahnschrift SemiLight")
        font.setPointSize(10)
        self.label_currentTime.setFont(font)
        self.label_currentTime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_currentTime)

        self.label_duration = QLabel(self.frame_durationLabels)
        self.label_duration.setObjectName(u"label_duration")
        self.label_duration.setFont(font)
        self.label_duration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_duration)

        self.frame_4 = QFrame(self.frame_player)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(100, 240, 600, 60))
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiLight")
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiLight")
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(204, 204, 204);")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_player)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(100, 80, 600, 160))
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 140))
        self.label_3.setMaximumSize(QSize(140, 140))
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.0681818 rgba(255, 255, 255, 255), stop:1 rgba(152, 152, 152, 255));\n"
"border-radius:1px;")
        self.label_3.setPixmap(QPixmap(u":/icons_black/Resources/Icons/png-black/musical-note (1).png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_player)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 800, 480))
        self.label_4.setPixmap(QPixmap(u":/styles/Resources/equalicer_background.jpg"))
        self.label_4.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()

        self.retranslateUi(Player_widget)

        QMetaObject.connectSlotsByName(Player_widget)
    # setupUi

    def retranslateUi(self, Player_widget):
        Player_widget.setWindowTitle(QCoreApplication.translate("Player_widget", u"Form", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_currentTime.setText(QCoreApplication.translate("Player_widget", u"0:00", None))
        self.label_duration.setText(QCoreApplication.translate("Player_widget", u"3:23", None))
        self.label.setText(QCoreApplication.translate("Player_widget", u"Speechless (feat. Erika Sirola)", None))
        self.label_2.setText(QCoreApplication.translate("Player_widget", u"Robin Schulz, Erika Sirola", None))
    # retranslateUi

