from .ui_design_player import Ui_Player_widget
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Player_funcs:
	def playerSetup(self):
		self.GUI_Player = Ui_Player_widget()
		self.GUI_Player.setupUi(self.GUI_Central.page_player)
		# Control buttons
		self. GUI_Player.backButton.clicked.connect(lambda:self.BTController.playback_control('previous'))
		self. GUI_Player.rewindButton.clicked.connect(lambda:self.BTController.playback_control('rewind'))
		self. GUI_Player.playButton.clicked.connect(self.toggle_musicStatus)
		self. GUI_Player.forwardButton.clicked.connect(lambda:self.BTController.playback_control('fastforward'))
		self. GUI_Player.nextButton.clicked.connect(lambda:self.BTController.playback_control('next'))


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
