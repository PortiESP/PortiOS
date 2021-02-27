from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Leds_funcs:
	def ledsSetup(self):
		# Color 
		self.GUI_Leds.ledColor = [0,0,0]

		# Programs buttons
		# self.GUI_Leds.ledsProgramJumpButton.clicked.connect()
		# self.GUI_Leds.ledsProgramFadeButton.clicked.connect()
		# self.GUI_Leds.ledsProgramRandomButton.clicked.connect()
		# self.GUI_Leds.ledsProgramFlashButton.clicked.connect()
		# self.GUI_Leds.ledsProgramPoliceButton.clicked.connect()

		# Color picker
		# self.GUI_Leds.ledsColorPickerButton.clicked.connect()

		self.GUI_Leds.ledsSliderRed.valueChanged.connect(Leds_funcs.colorValueSetup(self, 0))
		self.GUI_Leds.ledsSliderGreen.valueChanged.connect(Leds_funcs.colorValueSetup(self, 1))
		self.GUI_Leds.ledsSliderBlue.valueChanged.connect(Leds_funcs.colorValueSetup(self, 2))

	def colorValueSetup(self, index):
		if index == 0:
			self.GUI_Leds.ledColor[0] = self.GUI_Leds.ledsSliderRed.value()
			self.GUI_Leds.ledsValueRed.setText(str(self.GUI_Leds.ledsSliderRed.value()))
		elif index == 1:
			self.GUI_Leds.ledColor[1] = self.GUI_Leds.ledsSliderGreen.value()
			self.GUI_Leds.ledsValueGreen.setText(str(self.GUI_Leds.ledsSliderGreen.value()))
		elif index == 2:
			self.GUI_Leds.ledColor[2] = self.GUI_Leds.ledsSliderBlue.value()
			self.GUI_Leds.ledsValueBlue.setText(str(self.GUI_Leds.ledsSliderBlue.value()))

		self.GUI_Leds.ledsBulb.setStyleSheet(u"background:rgb({});".format(self.GUI_Leds.ledColor))