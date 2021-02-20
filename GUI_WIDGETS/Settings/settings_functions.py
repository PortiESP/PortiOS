

class Settings_funcs:
	def settingsSetup(self, frame):
		self.frame = frame

		self.frame.bearing_settingsBrightness.clicked.connect(lambda:Settings_funcs.setPage(0))
		self.frame.bearing_settingsWifi.clicked.connect(lambda:Settings_funcs.setPage(1))
		self.frame.bearing_settingsBluetooth.clicked.connect(lambda:Settings_funcs.setPage(2))
		self.frame.bearing_settingsSound.clicked.connect(lambda:Settings_funcs.setPage(3))
		self.frame.bearing_settingsStatus.clicked.connect(lambda:Settings_funcs.setPage(4))
		self.frame.bearing_settingsGpio.clicked.connect(lambda:Settings_funcs.setPage(5))
		self.frame.bearing_settingsSystemInfo.clicked.connect(lambda:Settings_funcs.setPage(6))
		self.frame.bearing_settingsTerminal.clicked.connect(lambda:Settings_funcs.setPage(7))
		self.frame.bearing_settingsAdvanced.clicked.connect(lambda:Settings_funcs.setPage(8))

	def setPage(self, index):
		print('Changing to page ',index)
		self.frame.stackedWidget_settings.setCurrentIndex(index)