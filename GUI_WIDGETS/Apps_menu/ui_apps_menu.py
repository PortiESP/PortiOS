# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apps_menuChaAdA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Apps_widget(object):
    def setupUi(self, Apps_widget):
        if not Apps_widget.objectName():
            Apps_widget.setObjectName(u"Apps_widget")
        Apps_widget.resize(800, 480)
        Apps_widget.setMinimumSize(QSize(800, 480))
        Apps_widget.setMaximumSize(QSize(800, 480))
        self.frame_apps = QFrame(Apps_widget)
        self.frame_apps.setObjectName(u"frame_apps")
        self.frame_apps.setGeometry(QRect(0, 0, 800, 480))
        self.frame_apps.setStyleSheet(u"QFrame#frame_apps{\n"
"	background:rgb(20,20,20)\n"
"}\n"
"QPushButton{\n"
"	background:none; \n"
"	border:none;\n"
"}\n"
"QLabel{\n"
"	color:white;\n"
"	background:none;\n"
"}")
        self.frame_apps.setFrameShape(QFrame.NoFrame)
        self.frame_apps.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_apps)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(50, 60, 50, 120)
        self.frame_4 = QFrame(self.frame_apps)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 80))
        self.frame_4.setStyleSheet(u"")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(14, 14, 50, 50))
        self.label_10.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/fi-rr-dashboard.png"))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 0, 200, 80))
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(88, 16, 98, 46))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiLight")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 200, 80))
        self.label_12.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_12.setScaledContents(True)
        self.label_12.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton_4.raise_()

        self.gridLayout.addWidget(self.frame_4, 6, 5, 1, 1)

        self.frame_2 = QFrame(self.frame_apps)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 80))
        self.frame_2.setStyleSheet(u"")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(14, 14, 50, 50))
        self.label_4.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/maps-and-flags.png"))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 0, 200, 80))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(88, 16, 98, 46))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 200, 80))
        self.label_6.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_6.setScaledContents(True)
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()

        self.gridLayout.addWidget(self.frame_2, 4, 7, 1, 1)

        self.frame_6 = QFrame(self.frame_apps)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(200, 80))
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(14, 14, 50, 50))
        self.label_16.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/fi-rr-settings-sliders.png"))
        self.label_16.setAlignment(Qt.AlignCenter)
        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 0, 200, 80))
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(88, 16, 98, 46))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 200, 80))
        self.label_18.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_18.setScaledContents(True)
        self.label_18.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.pushButton_6.raise_()

        self.gridLayout.addWidget(self.frame_6, 6, 8, 1, 1)

        self.frame = QFrame(self.frame_apps)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 14, 50, 50))
        self.label.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/chrome (1).png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(88, 16, 98, 46))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 200, 80))
        self.label_3.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_3.setScaledContents(True)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 200, 80))
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()

        self.gridLayout.addWidget(self.frame, 4, 5, 1, 1)

        self.frame_3 = QFrame(self.frame_apps)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(200, 80))
        self.frame_3.setStyleSheet(u"")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(14, 14, 50, 50))
        self.label_7.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/idea.png"))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 0, 200, 80))
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(88, 16, 98, 46))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 200, 80))
        self.label_9.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_9.setScaledContents(True)
        self.label_9.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_3.raise_()

        self.gridLayout.addWidget(self.frame_3, 4, 8, 1, 1)

        self.frame_5 = QFrame(self.frame_apps)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(200, 80))
        self.frame_5.setStyleSheet(u"")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(14, 14, 50, 50))
        self.label_13.setPixmap(QPixmap(u":/icons_white/Resources/Icons/png-white/seno.png"))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 0, 200, 80))
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(88, 16, 98, 46))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 200, 80))
        self.label_15.setPixmap(QPixmap(u":/styles/Resources/appbox.png"))
        self.label_15.setScaledContents(True)
        self.label_15.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.pushButton_5.raise_()

        self.gridLayout.addWidget(self.frame_5, 6, 7, 1, 1)


        self.retranslateUi(Apps_widget)

        QMetaObject.connectSlotsByName(Apps_widget)
    # setupUi

    def retranslateUi(self, Apps_widget):
        Apps_widget.setWindowTitle(QCoreApplication.translate("Apps_widget", u"Form", None))
        self.label_10.setText("")
        self.pushButton_4.setText("")
        self.label_11.setText(QCoreApplication.translate("Apps_widget", u"Dashboard", None))
        self.label_12.setText("")
        self.label_4.setText("")
        self.pushButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Apps_widget", u"Maps", None))
        self.label_6.setText("")
        self.label_16.setText("")
        self.pushButton_6.setText("")
        self.label_17.setText(QCoreApplication.translate("Apps_widget", u"Settings", None))
        self.label_18.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Apps_widget", u"Browser", None))
        self.label_3.setText("")
        self.pushButton.setText("")
        self.label_7.setText("")
        self.pushButton_3.setText("")
        self.label_8.setText(QCoreApplication.translate("Apps_widget", u"Leds", None))
        self.label_9.setText("")
        self.label_13.setText("")
        self.pushButton_5.setText("")
        self.label_14.setText(QCoreApplication.translate("Apps_widget", u"Music", None))
        self.label_15.setText("")
    # retranslateUi

