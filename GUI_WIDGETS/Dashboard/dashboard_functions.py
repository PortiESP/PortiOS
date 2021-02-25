from GUI_WIDGETS.Dashboard.gauge_functions import *


class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self):
		# Setting labels
		track = self.BTController.get_player_data('Track')
		try:
			if len(track) == 1:
				self.GUI_Dashboard.label_duration.setText(str(Dashboard_funcs.formatDuration( track['Duration'])))
			self.GUI_Dashboard.label_cancion.setText(str(track['Title']))
			self.GUI_Dashboard.label_artista.setText(str(track['Artist']))	 
			
			
		except KeyError:
			pass

	def formatDuration(duration):
		duration = int(duration)
		duration /= 1000
		mins = int(duration / 60)
		segs = int(((duration / 60) - mins) * 60)
		return str(mins) + ':' + f'{segs:02}'
