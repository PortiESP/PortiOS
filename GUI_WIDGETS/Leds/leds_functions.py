from .ui_leds import Ui_Leds_widget
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import threading, time

class Leds_funcs:
	def ledsSetup(self):
		# Getting interface
		self.GUI_Leds = Ui_Leds_widget()
		self.GUI_Leds.setupUi(self.GUI_Central.page_leds)
		
		# Color 
		self.GUI_Leds.ledColor = [0,0,0]
		self.GUI_Leds.slidersList = (self.GUI_Leds.ledsSliderRed,
									 self.GUI_Leds.ledsSliderGreen,
									 self.GUI_Leds.ledsSliderBlue)
		self.GUI_Leds.ledPower = False

		self.GUI_Leds.colorUpdateHz = 10
		self.GUI_Leds.actualProgram = None

		# Programs buttons
		self.GUI_Leds.ledsProgramJumpButton.clicked.connect(lambda: Leds_funcs.setProgram(self, 'jump'))
		self.GUI_Leds.ledsProgramFadeButton.clicked.connect(lambda: Leds_funcs.setProgram(self, 'fade'))
		self.GUI_Leds.ledsProgramRandomButton.clicked.connect(lambda: Leds_funcs.setProgram(self, 'random'))
		self.GUI_Leds.ledsProgramFlashButton.clicked.connect(lambda: Leds_funcs.setProgram(self, 'flash'))
		self.GUI_Leds.ledsProgramPoliceButton.clicked.connect(lambda: Leds_funcs.setProgram(self, 'police'))

		# Color picker
		self.GUI_Leds.ledsColorPickerButton.clicked.connect(lambda: Leds_funcs.pickColor(self))

		# On/off Button
		self.GUI_Leds.ledsOnOffButton.clicked.connect(lambda: Leds_funcs.toggleLedPower(self))


		self.GUI_Leds.ledsSliderRed.valueChanged.connect(lambda: Leds_funcs.colorSliderRedMoved(self))
		self.GUI_Leds.ledsSliderGreen.valueChanged.connect(lambda: Leds_funcs.colorSliderGreenMoved(self))
		self.GUI_Leds.ledsSliderBlue.valueChanged.connect(lambda: Leds_funcs.colorSliderBlueMoved(self))

		

	def colorValueSetup(self, index):
		if index == 0:
			self.GUI_Leds.ledColor[0] = self.GUI_Leds.ledsSliderRed.value()
			self.GUI_Leds.ledsValueRed.setText(str(self.GUI_Leds.ledColor[0]))
		elif index == 1:
			self.GUI_Leds.ledColor[1] = self.GUI_Leds.ledsSliderGreen.value()
			self.GUI_Leds.ledsValueGreen.setText(str(self.GUI_Leds.ledColor[1]))
		elif index == 2:
			self.GUI_Leds.ledColor[2] = self.GUI_Leds.ledsSliderBlue.value()
			self.GUI_Leds.ledsValueBlue.setText(str(self.GUI_Leds.ledColor[2]))
		
		self.GUI_Leds.ledsBulb.setStyleSheet(u"background:rgb({},{},{});".format(*self.GUI_Leds.ledColor))



	def pickColor(self):
		# Getting color without alpha
		color = QColorDialog.getColor().getRgb()

		# Setting slider value and set valuesoption
		for i in range(3): 
			self.GUI_Leds.slidersList[i].setValue(color[i])
			Leds_funcs.colorValueSetup(self, i)

		print('Setted color: ', color)



	def toggleLedPower(self):

		self.GUI_Leds.ledPower = not self.GUI_Leds.ledPower

		if self.GUI_Leds.ledPower:
			self.ledsController.set_color(self.GUI_Leds.ledColor)

		if self.GUI_Leds.ledPower == False:
			self.GUI_Leds.actualProgram = None
			self.ledsController.program_stop()
			print('Led program: None')




		print('Led power is: ', self.GUI_Leds.ledPower)

	def setProgram(self, option):
		if not self.GUI_Leds.ledPower: return

		speed = self.GUI_Leds.ledSpeedSlider.value()
		

		if option == self.GUI_Leds.actualProgram and option == 'random': option += '-jump'
		print('Setting program: ', option, ' - with speed: ', speed)

		self.GUI_Leds.actualProgram = option

		if option == 'jump':
			self.ledsController.set_program(program=self.ledsController.RAINBOW, hz=0.1, mode='jump')
		elif option == 'fade':
			self.ledsController.set_program(program=self.ledsController.RAINBOW, hz=0.1, mode='fade', method='chromatic')
		elif option == 'random':
			self.ledsController.set_program(hz=0.1, mode='random-fade')
		elif option == 'random-jump':
			self.ledsController.set_program(hz=0.2, mode='random-jump')
		elif option == 'flash':
			self.ledsController.set_program(program=(self.GUI_Leds.ledColor, (0,0,0)), hz=speed, mode='jump')
		elif option == 'police':
			self.ledsController.set_program(program=self.ledsController.POLICE, hz=speed, mode='jump')


	def colorSliderRedMoved(self):
		Leds_funcs.colorValueSetup(self, 0)
		if self.GUI_Leds.ledPower:
			self.ledsController.program_stop()
			self.ledsController.set_color(self.GUI_Leds.ledColor)
	def colorSliderGreenMoved(self):
		Leds_funcs.colorValueSetup(self, 1)
		if self.GUI_Leds.ledPower:
			self.ledsController.program_stop()
			self.ledsController.set_color(self.GUI_Leds.ledColor)
	def colorSliderBlueMoved(self):
		Leds_funcs.colorValueSetup(self, 2)
		if self.GUI_Leds.ledPower:
			self.ledsController.program_stop()
			self.ledsController.set_color(self.GUI_Leds.ledColor)
	
