from .ui_design_settings import Ui_Settings_widget
import subprocess, threading, re, time


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
		def refresh():
			self.GUI_Settings.bearing_wifiSsidText.setText(getSSID()) # SSID
			self.GUI_Settings.bearing_wifiIpText.setText(getIP())     # IP
			

		def togglePower():
			if self.GUI_Settings.bearing_wifiPowerCheckbox.isChecked(): setStatus = 'down'
			else: setStatus = 'up'
			subprocess.run([f'sudo ifconfig wlan0 {setStatus}'], shell=True)
			print('Wifi power ', setStatus)

			def waitNetwork():
				while not getSSID():
					time.sleep(0.5)
				refresh()
			if setStatus == 'up':
				threading.Thread(target=waitNetwork).start()


		def getSSID():
			try:
				out = subprocess.run('iwgetid', capture_output=True, text=True, shell=True).stdout.split(':')[1].strip()[1:-1]
			except IndexError:
				return False
			print('SSID: ', out)
			if out: return out
			else: return False

		def getIP():
			out = subprocess.run('ifconfig wlan0', capture_output=True, text=True, shell=True).stdout.split('\n')[1].strip().split(' ')
			if out[0] == 'inet': 
				out = out[1]
				return True
			else: return False
			print('IP: ', out)
			
			

		
		# BEARING SETUP
		self.GUI_Settings.bearing_wifiPowerCheckbox.toggled.connect(togglePower)
		self.GUI_Settings.bearing_refreshWifiButton.clicked.connect(refresh)
		