from gauge_functions import *


class Dashboard_funcs:

	def dashboardSetup(self):
		Gauge_funcs.setDefaults(self)

	def changeMusicInfo(self, data):
		# Setting labels
		self.GUI_Dashboard.label_cancion.setText(data['Title']) 
		self.GUI_Dashboard.label_artista.setText(data['Artist'])

