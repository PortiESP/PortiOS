from GUI_WIDGETS.Dashboard.gauge_functions import *


class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self, data):
		# Setting labels
		try:
			if dict(data).has_key('Title'):
				self.GUI_Dashboard.label_cancion.setText(data['Title']) 
				self.GUI_Dashboard.label_artista.setText(data['Artist'])
			else:
				self.GUI_Dashboard.label_duration.setText(Dashboard_funcs.formatDuration(data['Duration']))
		except KeyError:
			pass

	def formatDuration(duration):
		duration /= 1000
		mins = int(duration / 60)
		segs = int(((duration / 60) - mins) * 60)
		return str(mins) + ':' + f'{segs:02}'
