from .ui_dashboard import Ui_Dashboard_widget
from .gauge_functions import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import threading, time

class Dashboard_funcs:

	def dashboardSetup(self):
		# Getting interface
		self.GUI_Dashboard = Ui_Dashboard_widget()
		self.GUI_Dashboard.setupUi(self.GUI_Central.page_dashboard)
		
		# Getting gauge funcs
		Gauge_funcs.setDefaults(self)

		self.GUI_Dashboard.gaugeThread = None
		self.GUI_Dashboard.gaugePower = False


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
			if self.DEBUG: print("[$] Gauge started")

			while self.GUI_Dashboard.gaugePower:
				if self.GUI_Central.appsWidget.currentIndex() == 0:
					try:
						value = self.adcController.read_adc(self.GAUGE_ADS_CHANNEL, gain=self.GAIN, data_rate=16)
					except OSError:
						print('ADS1x15 Not found')
						continue
					speed = Dashboard_funcs.mapDigitalSpeed(self, value, maxValue=self.MAX_ADS_VALUE)
					try:
						Gauge_funcs.setSpeed(self, speed)
					except:
						print('Gauge exception')

		self.GUI_Dashboard.gaugePower = True
		self.GUI_Dashboard.gaugeThread = threading.Thread(target=gaugeThreadFunc)
		self.GUI_Dashboard.gaugeThread.start()

	def stopGauge(self):
		self.GUI_Dashboard.gaugePower = False
		Gauge_funcs.setSpeed(self, 0)
