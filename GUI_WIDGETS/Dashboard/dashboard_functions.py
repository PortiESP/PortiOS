from GUI_WIDGETS.Dashboard.gauge_functions import *


class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self):
		# Setting labels
		self.GUI_Dashboard.label_cancion.setText(str(self.BTController.get_player_data('Track')['Title'] ))
		self.GUI_Dashboard.label_artista.setText(str(self.BTController.get_player_data('Track')['Artist']))	
		self.GUI_Dashboard.label_duration.setText(Dashboard_funcs.formatDuration(self.BTController.playerIface.Get('org.bluez.MediaPlayer1', 'Duration')))
		
	def formatDuration(duration):
		duration /= 1000
		mins = int(duration / 60)
		segs = int(((duration / 60) - mins) * 60)
		return str(mins) + ':' + f'{segs:02}'
