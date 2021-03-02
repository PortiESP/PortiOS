from .ui_design_settings import Ui_Settings_widget



class Settings_funcs:
	def settingsSetup(self):
		# Getting interface
		self.GUI_Settings = Ui_Settings_widget()
		self.GUI_Settings.setupUi(self.GUI_Central.page_settings)

		# Setting pages
		self.GUI_Settings.bearing_settingsBrightness.clicked.connect(lambda:Settings_funcs.setPage(self, 0))
		self.GUI_Settings.bearing_settingsWifi.clicked.connect(lambda:Settings_funcs.setPage(self, 1))
		self.GUI_Settings.bearing_settingsBluetooth.clicked.connect(lambda:Settings_funcs.setPage(self, 2))
		self.GUI_Settings.bearing_settingsSound.clicked.connect(lambda:Settings_funcs.setPage(self, 3))
		self.GUI_Settings.bearing_settingsStatus.clicked.connect(lambda:Settings_funcs.setPage(self, 4))
		self.GUI_Settings.bearing_settingsGpio.clicked.connect(lambda:Settings_funcs.setPage(self, 5))
		self.GUI_Settings.bearing_settingsSystemInfo.clicked.connect(lambda:Settings_funcs.setPage(self, 6))
		self.GUI_Settings.bearing_settingsTerminal.clicked.connect(lambda:Settings_funcs.setPage(self, 7))
		self.GUI_Settings.bearing_settingsAdvanced.clicked.connect(lambda:Settings_funcs.setPage(self, 8))


	def setPage(self, index):
		print('Changing to page ',index)
		self.GUI_Settings.stackedWidget_settings.setCurrentIndex(index)


	# MENUS SETUP
	def wifiSetup(self):
		self.GUI_Settings.bearing_wifi
		pass