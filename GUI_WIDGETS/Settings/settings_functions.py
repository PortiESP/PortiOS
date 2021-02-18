

class Settings_funcs:
	def settingsSetup(frame):
		frame.bearing_settingsBrightness.clicked.connect(lambda:Settings_funcs.setPage(frame, 0))
		frame.bearing_settingsWifi.clicked.connect(lambda:Settings_funcs.setPage(frame, 1))
		frame.bearing_settingsBluetooth.clicked.connect(lambda:Settings_funcs.setPage(frame, 2))
		frame.bearing_settingsSound.clicked.connect(lambda:Settings_funcs.setPage(frame, 3))
		frame.bearing_settingsStatus.clicked.connect(lambda:Settings_funcs.setPage(frame, 4))
		frame.bearing_settingsGpio.clicked.connect(lambda:Settings_funcs.setPage(frame, 5))
		frame.bearing_settingsSystemInfo.clicked.connect(lambda:Settings_funcs.setPage(frame, 6))
		frame.bearing_settingsTerminal.clicked.connect(lambda:Settings_funcs.setPage(frame, 7))
		frame.bearing_settingsAdvanced.clicked.connect(lambda:Settings_funcs.setPage(frame, 8))

	def setPage(frame, index):
		print('Changing to page ',index)
		frame.stackedWidget_settings.setCurrentIndex(index)