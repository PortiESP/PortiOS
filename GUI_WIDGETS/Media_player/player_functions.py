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
			
	def moveDurationSlider(self, position):
		if not self.trackDuration: return
		# Map value for get lineDurationTop
		WValue = (360 / (self.trackDuration/1000)) * (position/1000)

		# Setting slider value and line width
		self.GUI_Player.slider_duration.setValue(position)
		self.GUI_Player.lineDurationTop.setGeometry(QRect(70, 15, WValue, 1))
