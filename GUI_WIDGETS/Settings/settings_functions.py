

class Settings_funcs:
	def settingsSetup(self, frame):
		self.frame = frame

		self.frame.bearing_settingsBrightness.clicked.connect(lambda:self.setPage(0))
		self.frame.bearing_settingsWifi.clicked.connect(lambda:self.setPage(1))
		self.frame.bearing_settingsBluetooth.clicked.connect(lambda:self.setPage(2))
		self.frame.bearing_settingsSound.clicked.connect(lambda:self.setPage(3))
		self.frame.bearing_settingsStatus.clicked.connect(lambda:self.setPage(4))
		self.frame.bearing_settingsGpio.clicked.connect(lambda:self.setPage(5))
		self.frame.bearing_settingsSystemInfo.clicked.connect(lambda:self.setPage(6))
		self.frame.bearing_settingsTerminal.clicked.connect(lambda:self.setPage(7))
		self.frame.bearing_settingsAdvanced.clicked.connect(lambda:self.setPage(8))

	def setPage(self, index):
		print('Changing to page ',index)
		self.frame.stackedWidget_settings.setCurrentIndex(index)