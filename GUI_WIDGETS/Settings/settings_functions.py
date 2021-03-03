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
			self.GUI_Settings.bearing_wifiSsidText.setText(str(getSSID())) # SSID
			self.GUI_Settings.bearing_wifiIpText.setText(str(getIP()))     # IP
			

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
			else: 
				self.GUI_Settings.bearing_wifiSsidText.setText('None')
				self.GUI_Settings.bearing_wifiIpText.setText('None')


		def getSSID():
			try:
				out = subprocess.run('iwgetid', capture_output=True, text=True, shell=True).stdout.split(':')[1].strip()[1:-1]
			except IndexError:
				return None
			print('SSID: ', out)
			if out: return out
			else: return None

		def getIP():
			out = subprocess.run('ifconfig wlan0', capture_output=True, text=True, shell=True).stdout.split('\n')[1].strip().split(' ')
			if out[0] == 'inet': 
				out = out[1]
				print('IP: ', out)
				return out
			else: return None
			
		def connectWifi():
			print('Attempting to connect to "', self.GUI_Settings.bearing_wifiSSIDInput.text(), '" with key "', self.GUI_Settings.bearing_wifiPassInput.text(), '"')
			command = 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\ncountry=ES\n\nnetwork={{\nssid="{}"\npsk="{}"\nkey_mgmt=WPA-PSK\n}}'
			with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
				f.write(command.format(self.GUI_Settings.bearing_wifiSSIDInput.text(), self.GUI_Settings.bearing_wifiPassInput.text()))
			
			out = subprocess.run('sudo wpa_cli -i wlan0 reconfigure', capture_output=True, text=True, shell=True)
			if out.stdout == 'OK':
				print('Connection success')
				refresh()
			else:
				self.GUI_Settings.bearing_wifiSsidText.setText('Error')
				self.GUI_Settings.bearing_wifiIpText.setText('Error')
				print('Connection error')
				print(out.args)

		
		# BEARING SETUP
		refresh()
		self.GUI_Settings.bearing_wifiPowerCheckbox.toggled.connect(togglePower)
		self.GUI_Settings.bearing_refreshWifiButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_wifiPassButton.clicked.connect(connectWifi)
		