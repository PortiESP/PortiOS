

class Player_funcs:
	def playerSetup(self):
		# Control buttons
		pass

		

	def changeMusicInfo(self):
		# Setting labels
		

		try:
			if len(self.track) == 1:
				self.trackDuration = self.track['Duration']
				self.GUI_Player.label_duration.setText(str(self.formatDuration( self.trackDuration)))
				self.GUI_Player.slider_duration.setMaximum(int(self.trackDuration))

			self.GUI_Player.label_cancion.setText(str(self.track['Title']))
			self.GUI_Player.label_artista.setText(str(self.track['Artist']))	

			
			
		except KeyError:
			pass
	def moveDurationSlider(self, position):
		if not self.trackDuration: return
		# Map value for get lineDurationTop
		WValue = (260 / (self.trackDuration/1000)) * (position/1000)
		# Setting slider value and line width
		self.GUI_Player.slider_duration.setValue(position)
		self.GUI_Player.lineDurationTop.setGeometry(QRect(10, 271, WValue, 1))


	