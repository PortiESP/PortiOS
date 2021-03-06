from .ui_dashboard import Ui_Dashboard_widget
from .gauge_functions import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import threading, Adafruit_ADS1x15

class Dashboard_funcs:

	def dashboardSetup(self):
		# Getting interface
		self.GUI_Dashboard = Ui_Dashboard_widget()
		self.GUI_Dashboard.setupUi(self.GUI_Central.page_dashboard)

		# ADC converter
		adc = Adafruit_ADS1x15.ADS1115()
		self.GUI_Dashboard.GAUGE_ADS_CHANNEL = 0
		self.GUI_Dashboard.MAX_ADS_VALUE = 25200
		
		# Getting gauge funcs
		Gauge_funcs.setDefaults(self)

		self.GUI_Dashboard.gaugeThread = None
		self.GUI_Dashboard.gaugePower = False
		Dashboard_funcs.startGauge(self)


	def changeMusicInfo(self):
		# Setting labels and slider
		try:
			# Set duration data to sliderMax and progress line
			if len(self.track) == 1:
				self.GUI_Dashboard.label_duration.setText(str(self.formatDuration(self.trackDuration)))
				self.GUI_Dashboard.slider_duration.setMaximum(self.trackDuration)

			# Song info to labels
			self.GUI_Dashboard.label_cancion.setText(self.songTitle)
			self.GUI_Dashboard.label_artista.setText(self.songArtist)	
			
		except KeyError:
			pass


	def mapDigitalSpeed(self, value, maxValue=200):
		value = (value / maxValue) * self.GUI_Dashboard.TOP_SPEED
		return value

	def startGauge(self):
		def gaugeThreadFunc():
			while self.GUI_Dashboard.gaugePower:
				value = adc.read_adc(self.GUI_Dashboard.GAUGE_ADS_CHANNEL, gain=2, data_rate=16)
				value = Dashboard_funcs.mapDigitalSpeed(self, value, maxValue=self.GUI_Dashboard.MAX_ADS_VALUE)
				Gauge_funcs.setSpeed(self, value)

		self.GUI_Dashboard.gaugePower = True
		self.GUI_Dashboard.gaugeThread = threading.Thread(target=gaugeThreadFunc)
		self.GUI_Dashboard.gaugeThread.start()

	def stopGauge(self):
		self.GUI_Dashboard.gaugePower = False
