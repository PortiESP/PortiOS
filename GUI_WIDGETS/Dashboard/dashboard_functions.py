from GUI_WIDGETS.Dashboard.gauge_functions import *
from math import ceil

class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self):
		# Setting labels and slider
		try:
			# Duration
			self.GUI_Dashboard.label_duration.setText(str(self.formatDuration( self.trackDuration)))
			self.GUI_Dashboard.slider_duration.setMaximum(int(self.trackDuration))

			# Song info
			self.GUI_Dashboard.label_cancion.setText(str(self.track['Title']))
			self.GUI_Dashboard.label_artista.setText(str(self.track['Artist']))	
			
		except KeyError:
			pass
			
	def moveDurationSlider(self, position):
		if not self.trackDuration: return
		# Map value for get lineDurationTop
		WValue = (260 / (self.trackDuration/1000)) * (position/1000)

		# Setting slider value and line width
		self.GUI_Dashboard.slider_duration.setValue(position)
		self.GUI_Dashboard.lineDurationTop.setGeometry(QRect(10, 271, WValue, 1))


	