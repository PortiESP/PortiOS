from GUI_WIDGETS.Dashboard.gauge_functions import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Dashboard_funcs:

	def dashboardSetup(self):
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
			
	def moveDurationSlider(self, position):
		if not self.trackDuration: return
		# Map value for get lineDurationTop
		WValue = (260 / (self.trackDuration/1000)) * (position/1000)

		# Setting slider value and line width
		self.GUI_Dashboard.slider_duration.setValue(position)
		self.GUI_Dashboard.lineDurationTop.setGeometry(QRect(10, 271, WValue, 1))


	