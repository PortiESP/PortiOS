from GUI_WIDGETS.Dashboard.gauge_functions import *

class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self):
		# Setting labels
		self.track = self.BTController.get_player_data('Track')

		try:
			if len(self.track) == 1:
				self.trackDuration = self.track['Duration']
				self.GUI_Dashboard.label_duration.setText(str(Dashboard_funcs.formatDuration( self.trackDuration)))
				self.GUI_Dashboard.slider_duration.setMaximum(int(self.trackDuration/1000))

			self.GUI_Dashboard.label_cancion.setText(str(self.track['Title']))
			self.GUI_Dashboard.label_artista.setText(str(self.track['Artist']))	

			
			
		except KeyError:
			pass
	def moveDurationSlider(self, position):
		if not self.trackDuration: return
		# Map value for get lineDurationTop
		WValue = (260 / (self.trackDuration/1000)) * position
		# Setting slider value and line width
		self.GUI_Dashboard.slider_duration.setValue(position)
		self.GUI_Dashboard.lineDurationTop.setGeometry(QRect(10, 271, WValue, 1))


	def formatDuration(duration):
		duration = int(duration)
		duration /= 1000
		mins = int(duration / 60)
		segs = int(((duration / 60) - mins) * 60)
		return str(mins) + ':' + f'{segs:02}'
