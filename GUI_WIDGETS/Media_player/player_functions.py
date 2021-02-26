from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Player_funcs:
	def playerSetup(self):
		# Control buttons
		pass

		

	def changeMusicInfo(self):
		# Setting labels and slider
		try:
			# Set duration data to sliderMax and progress line
			if len(self.track) == 1:
				self.GUI_Player.label_duration.setText(str(self.formatDuration(self.trackDuration)))
				self.GUI_Player.slider_duration.setMaximum(self.trackDuration)

			# Song info to labels
			self.GUI_Player.label_cancion.setText(self.songTitle)
			self.GUI_Player.label_artista.setText(self.songArtist)	
			
		except KeyError:
			pass
