from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import threading, time
from PIL import Image


class Gauge_funcs(QMainWindow):
	def setDefaults(self):
		# Arc of min degree and max degree
		self.DEGREE_RANGE = [240, 300] 
		# Constant for degree in base1 for 360º
		self.DEGREE_VALUE = (1/360)
		# Calculate max value in Base1 for needle
		self.RANGE_VALUE = self.DEGREE_VALUE * (360 - (self.DEGREE_RANGE[1] - self.DEGREE_RANGE[0]))
		self.MAX_VALUE = 1.0 - self.RANGE_VALUE
		# Max speed for our progressbar
		self.TOP_SPEED = 200
		# Calculate speed in baseMAX_VALUE for needle
		self.NEEDLE_CONSTANT = self.RANGE_VALUE / self.TOP_SPEED
		# Needle position in baseRANGE_VALUE
		self.needleForward = 1.0
		self.needleBackward = 1.0

		# Gauge color
		self.gaugeColors = {'needle' : 'rgba(255,170,0,255)', 
							'kmCircle' : 'rgb(255,170,0)', 
							'fontColor' : 'white',
							'background' : 'rgba(0,0,0,0)'}

		# Numbers pixmap path
		self.numRingSrc = r'C:/Users/elp0r/Desktop/porti_os/Recursos/dashnums3.png'

		# StyleSheets
		self.needleStylesheet	= 'QFrame{{		\
									border:none;	\
									background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240,stop:1.0 rgba(0,0,0,0),  stop:{needleForward} {needleColor}, stop:{needleBackward} rgba(0, 0, 0, 0));	\
									border-radius:125px;	\
									}}'
		self.kmCircleStyleSheet = 'QFrame{{	background:none; 	border-radius:75px;	border:2px solid {borderColor};}}QLabel{{	border:none; color:{fontColor};}}'
		self.backgroundCircleStyleSheet = 'QFrame{{background-color: {}; border-radius:135px;}}'
		self.innerCircleStyleSheet = 'QFrame{{	background-color: {};	border-radius:85px;}}'

		Gauge_funcs.setGaugeShadow(self, True)
		

		
		# Printing variables

	# Change the colors of the gauge
	def setDesignColors(self, **kwargs):
		for k, v in kwargs.items():
			self.gaugeColors[k] = v
		self.gauge_widget.needle.setStyleSheet(self.needleStylesheet.format(needleForward = self.needleForward, needleColor = self.gaugeColors['needle'], needleBackward = self.needleBackward))
		self.gauge_widget.frame_km.setStyleSheet(self.kmCircleStyleSheet.format(borderColor = self.gaugeColors['kmCircle'], fontColor = self.gaugeColors['fontColor']))
		self.gauge_widget.gaugeInnerCircle.setStyleSheet(self.innerCircleStyleSheet.format(self.gaugeColors['background']))
		self.gauge_widget.gaugeBackground.setStyleSheet(self.backgroundCircleStyleSheet.format(self.gaugeColors['background']))

	def setGaugeShadow(self, flag, blur=20, color=(0,0,0)):

		shadow = QGraphicsDropShadowEffect(self)
		shadow.setBlurRadius(blur)
		shadow.setXOffset(0)
		shadow.setYOffset(0)
		shadow.setColor(QColor(*color))
		if flag:
			self.gauge_widget.gaugeBackground.setGraphicsEffect(shadow)
		else:
			self.gauge_widget.gaugeBackground.setGraphicsEffect(None)

	def setSpeedNumbersColor(self, color):
		img = Image.open(self.numRingSrc)
		new_img = []
		for p in img.getdata():
			if p[:-1] == (0,0,0):
				new_img.append((*color, p[-1]))
			else:
				new_img.append(p)
		img.putdata(new_img)
		img.save('speedNumbers.png')
		img.close()
		Gauge_funcs.setNumsPixmap(self, 'speedNumbers.png')

		
	def setNumsPixmap(self, src):
		pixmap = QPixmap(src)
		self.gauge_widget.label_nums.setPixmap(pixmap)
		self.numRingSrc = src

	# Set speed in label and update progressbar
	def setSpeed(self, speed):

		self.gauge_widget.label_vel.setText(str(int(float(speed))))

		self.needleForward = Gauge_funcs.mapValue(self, speed)

		if speed == 0: 
			self.needleBackward = self.needleForward
		else: 
			self.needleBackward = self.needleForward - 0.001

		self.gauge_widget.needle.setStyleSheet(self.needleStylesheet.format(needleForward = self.needleForward,
																	needleColor = self.gaugeColors['needle'],
																	needleBackward = self.needleBackward))		

	# Gets the baseNEEDLE_CONSTANT value for speed in Kmh
	def mapValue(self, value):
		self.needleValue = 1.0 - (float(value) * self.NEEDLE_CONSTANT)
		return self.needleValue


	# Test values
	def gauge_test(self):
		def event1():		
			while 1: 
				Gauge_funcs.setSpeed(self, input('Speed ==> '))		

		def event2():
			import sys
			for i in range(2010):
				
				# print(i/10)
				Gauge_funcs.setSpeed(self,i/10)
				time.sleep(0.01)

		a = threading.Thread(target=event2)
		a.start()
		
		# a.join()

