from .ui_design_settings import Ui_Settings_widget
import subprocess


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

		# Setting up pages bearings
		Settings_funcs.wifiSetup(self)

	def setPage(self, index):
		print('Changing to page ',index)
		self.GUI_Settings.stackedWidget_settings.setCurrentIndex(index)


	# MENUS SETUP
	def wifiSetup(self):

		# FUNCTIONS
		def togglePower():
			if self.GUI_Settings.bearing_wifiPowerCheckbox.isChecked(): setStatus = 'up'
			else: setStatus = 'down'
			print('Wifi power ', setStatus)
			subprocess.run(['sudo ifconfig wlan0 ', setStatus] , shell=True)

		def getSSID():
			out = subprocess.run('iwgetid', text=True, shell=True).stdout
			print('SSID: ',out)
			if out:
				return out.split(':').strip()
			else:
				return False
		# SETUP
		self.GUI_Settings.bearing_wifiPowerCheckbox.toggled.connect(togglePower)
		