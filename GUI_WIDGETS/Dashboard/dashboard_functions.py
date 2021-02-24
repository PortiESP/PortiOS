from GUI_WIDGETS.Dashboard.gauge_functions import *


class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self, data=None):
		print('Updated labels')
		# Setting labels
		try:
			self.GUI_Dashboard.label_cancion.setText(str(dict(self.BTController.get_player_data('Track'))['Title'] ))
			self.GUI_Dashboard.label_artista.setText(str(dict(self.BTController.get_player_data('Track'))['Artist']))	
			if 'title' not in data[1].keys():
				self.GUI_Dashboard.label_duration.setText(Dashboard_funcs.formatDuration(self.BTController.playerIface.Get('org.bluez.MediaPlayer1', 'Duration')))
		except KeyError:
			pass

	def formatDuration(duration):
		duration = int(duration)
		duration /= 1000
		mins = int(duration / 60)
		segs = int(((duration / 60) - mins) * 60)
		return str(mins) + ':' + f'{segs:02}'
