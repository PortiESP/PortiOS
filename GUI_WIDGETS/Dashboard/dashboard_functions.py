from GUI_WIDGETS.Dashboard.gauge_functions import *


class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self, data):
		# Setting labels
		try:
			self.GUI_Dashboard.label_duration.setText(Dashboard_funcs.formatDuration(data['Duration']))
			self.GUI_Dashboard.label_cancion.setText(data['Title']) 
			self.GUI_Dashboard.label_artista.setText(data['Artist'])
		except KeyError:
			pass

	def formatDuration(duration):
		duration /= 1000
		mins = duration // 60
		segs = int((duration % 60) * 60)
		return str(mins) + ':' + str(segs)
