from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Gauge_funcs:
	def setDefaults(self):
		# Arc of min degree and max degree
		self.GUI_Dashboard.DEGREE_RANGE = [240, 300] 
		# Constant for degree in base1 for 360º
		self.GUI_Dashboard.DEGREE_VALUE = (1/360)
		# Calculate max value in Base1 for needle
		self.GUI_Dashboard.RANGE_VALUE = self.GUI_Dashboard.DEGREE_VALUE * (360 - (self.GUI_Dashboard.DEGREE_RANGE[1] - self.GUI_Dashboard.DEGREE_RANGE[0]))
		self.GUI_Dashboard.MAX_VALUE = 1.0 - self.GUI_Dashboard.RANGE_VALUE
		# Max speed for our progressbar
		self.GUI_Dashboard.TOP_SPEED = 200
		# Calculate speed in baseMAX_VALUE for needle
		self.GUI_Dashboard.NEEDLE_CONSTANT = self.GUI_Dashboard.RANGE_VALUE / self.GUI_Dashboard.TOP_SPEED
		# Needle position in baseRANGE_VALUE
		self.GUI_Dashboard.needleForward = 1.0
		self.GUI_Dashboard.needleBackward = 1.0

		# Numbers pixmap path
		self.GUI_Dashboard.numRingSrc = r'C:/Users/elp0r/Desktop/porti_os/Recursos/dashnums3.png'

		# StyleSheets
		self.GUI_Dashboard.needleStylesheet	= 'QFrame{{		\
									border:none;	\
									background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240,stop:1.0 rgba(0,0,0,0),  stop:{needleForward} {needleColor}, stop:{needleBackward} rgba(0, 0, 0, 0));	\
									border-radius:125px;	\
									}}'
		self.GUI_Dashboard.kmCircleStyleSheet = 'QFrame{{	background:none; 	border-radius:75px;	border:2px solid {borderColor};}}QLabel{{	border:none; color:{fontColor};}}'
		self.GUI_Dashboard.backgroundCircleStyleSheet = 'QFrame{{background-color: {}; border-radius:135px;}}'
		self.GUI_Dashboard.innerCircleStyleSheet = 'QFrame{{	background-color: {};	border-radius:85px;}}'

		Gauge_funcs.setGaugeShadow(self, True)
		


	def setGaugeShadow(self, flag, blur=20, color=(0,0,0)):

		shadow = QGraphicsDropShadowEffect(self.GUI_Dashboard.Dashboard_widget)
		shadow.setBlurRadius(blur)
		shadow.setXOffset(0)
		shadow.setYOffset(0)
		shadow.setColor(QColor(*color))
		if flag:
			self.GUI_Dashboard.Dashboard_widget.gaugeBackground.setGraphicsEffect(shadow)
		else:
			self.GUI_Dashboard.Dashboard_widget.gaugeBackground.setGraphicsEffect(None)

	# Set speed in label and update progressbar
	def setSpeed(self, speed):

		self.GUI_Dashboard.gauge_widget.label_vel.setText(str(int(float(speed))))

		self.GUI_Dashboard.needleForward = Gauge_funcs.mapValue(self, speed)

		if speed == 0: 
			self.GUI_Dashboard.needleBackward = self.GUI_Dashboard.needleForward
		else: 
			self.GUI_Dashboard.needleBackward = self.GUI_Dashboard.needleForward - 0.001

		self.GUI_Dashboard.gauge_widget.needle.setStyleSheet(self.GUI_Dashboard.needleStylesheet.format(needleForward = self.GUI_Dashboard.needleForward,
																	needleColor = 'rgba(255,170,0,255)',
																	needleBackward = self.GUI_Dashboard.needleBackward))		

	# Gets the baseNEEDLE_CONSTANT value for speed in Kmh
	def mapValue(self, value):
		self.GUI_Dashboard.needleValue = 1.0 - (float(value) * self.GUI_Dashboard.NEEDLE_CONSTANT)
		return self.GUI_Dashboard.needleValue



