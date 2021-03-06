from .ui_dashboard import Ui_Dashboard_widget
from .gauge_functions import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Dashboard_funcs:

	def dashboardSetup(self):
		# Getting interface
		self.GUI_Dashboard = Ui_Dashboard_widget()
		self.GUI_Dashboard.setupUi(self.GUI_Central.page_dashboard)
		
		# Getting gauge funcs
		Gauge_funcs.setDefaults(self)


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
