from .ui_design_settings import Ui_Settings_widget
import subprocess, threading, re, time
import RPi.GPIO as gp


class Settings_funcs:
	def settingsSetup(self):
		# Getting interface
		self.GUI_Settings = Ui_Settings_widget()
		self.GUI_Settings.setupUi(self.GUI_Central.page_settings)

		self.GUI_Settings.TIMEOUT = 20
		self.GUI_Settings.BTdataDict = {}

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
		Settings_funcs.btSetup(self)
		Settings_funcs.servicesStatusSetup(self)
		Settings_funcs.gpioSetup(self)

	def setPage(self, index):
		print('Changing to page ',index)
		self.GUI_Settings.stackedWidget_settings.setCurrentIndex(index)


# ----------------------------------------- MENUS SETUP -------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------

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
			tstart = time.time()
			def waitNetwork(tstart):
				while not getSSID():
					time.sleep(0.5)
					if (time.time() - tstart) > self.GUI_Settings.TIMEOUT:
						print('Connection timeout')
						break
				refresh()
			if setStatus == 'up':
				threading.Thread(target=waitNetwork, args=(tstart,)).start()
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
			subprocess.run('sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf', capture_output=True, shell=True)
			with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
				f.write(command.format(self.GUI_Settings.bearing_wifiSSIDInput.text(), self.GUI_Settings.bearing_wifiPassInput.text()))
			
			out = subprocess.run('sudo wpa_cli -i wlan0 reconfigure', capture_output=True, text=True, shell=True)
			togglePower()

		
		# BEARING SETUP
		refresh()
		self.GUI_Settings.bearing_wifiPowerCheckbox.toggled.connect(togglePower)
		self.GUI_Settings.bearing_refreshWifiButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_wifiPassButton.clicked.connect(connectWifi)
		







# ------------------------------------------------------------------------------------------------------
	# BT SETUP
	def btSetup(self):
		def updateData():
			out = subprocess.run('bluetoothctl show', capture_output=True, text=True, shell=True).stdout
			print(out)
			dataLines = out.split('\n')
			for line in dataLines:
				line = line.strip()
				if re.match('Name', line): self.GUI_Settings.BTdataDict['Name'] = line.split(':')[1].strip()
				if re.match('Powered', line): self.GUI_Settings.BTdataDict['Powered'] = line.split(':')[1].strip()
				if re.match('Discoverable', line): self.GUI_Settings.BTdataDict['Discoverable'] = line.split(':')[1].strip()
			
			getConnectedDevice()

			print('BT data = ', self.GUI_Settings.BTdataDict)

		def getConnectedDevice():
			if self.isConnectedDevice:
				name = str(self.BTController.get_device_data('Name'))
				if name == 'False': name = 'None'
			else: 
				name = 'None'
			print('BT Connected device: ', name)
			self.GUI_Settings.BTdataDict['Connected'] = name

		def refresh():
			updateData() #dict values [yes/no]
			if self.GUI_Settings.BTdataDict['Powered'] == 'yes':
				self.GUI_Settings.bearing_btNameText.setText(self.GUI_Settings.BTdataDict['Name'])
				self.GUI_Settings.bearing_btConnectedText.setText(self.GUI_Settings.BTdataDict['Connected'])
				if self.GUI_Settings.BTdataDict['Discoverable'] == 'yes':
					self.GUI_Settings.bearing_btDiscoverableCheckbox.setChecked(False)
				else:
					self.GUI_Settings.bearing_btDiscoverableCheckbox.setChecked(True)


		def togglePower():
			if self.GUI_Settings.bearing_btPowerCheckbox.isChecked():
				print('Powering BT off')
				subprocess.run('bluetoothctl power off', capture_output=True, shell=True)
			else:
				print('Powering BT on')
				subprocess.run('bluetoothctl power on', capture_output=True, shell=True)
				refresh()

		def toggleDiscoverable():
			if self.GUI_Settings.bearing_btDiscoverableCheckbox.isChecked():
				setStatus = 'off'
			else:
				setStatus = 'on'
			print('Setting discoverable to: ', setStatus)
			subprocess.run(f'bluetoothctl discoverable {setStatus}', capture_output=True, shell=True)
			updateData()

		def openManager():
			print('Opening bluetoothctl')
			subprocess.run('x-terminal-emulator -e bluetoothctl', capture_output=True, shell=True)

		self.GUI_Settings.bearing_refreshBtButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_btPowerCheckbox.toggled.connect(togglePower)
		self.GUI_Settings.bearing_btDiscoverableCheckbox.toggled.connect(toggleDiscoverable)
		self.GUI_Settings.bearing_btManagerButton.clicked.connect(openManager)
















# ------------------------------------------------------------------------------------------------------

	def servicesStatusSetup(self):
		def getServiceStatus(service):
			out = subprocess.run(f'systemctl is-active {service}', capture_output=True, text=True, shell=True).stdout.strip()
			return out


		def refresh():
			self.GUI_Settings.bearing_statusBtText.setText(getServiceStatus('bluetooth'))

		def restartService(service):
			print('Restarting ', service)
			subprocess.run(f'sudo systemctl restart {service}', shell=True)

		self.GUI_Settings.bearing_statusRefreshButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_statusBtButton.clicked.connect(lambda: restartService('bluetooth'))


	def gpioSetup(self):

		def setPin():
			pin = int(self.GUI_Settings.bearing_gpioSetPinInput.text())
			value = int(self.GUI_Settings.bearing_gpioSetValueInput.text())
			gp.setup(pin, gp.OUT)
			gp.output(pin, value)
			self.GUI_Settings.bearing_gpioPinLabel.setText(str(pin))
			self.GUI_Settings.bearing_gpioPinValueLabel.setText(str(value))
			print('Pin ', pin , ' set to ', value)

		def getPin():
			pin = int(self.GUI_Settings.bearing_gpioGetInput.text())
			value = gp.input(pin)
			print('Pin ', pin , ' value: ', value)
			self.GUI_Settings.bearing_gpioPinLabel.setText(self.GUI_Settings.bearing_gpioGetPinInput.text())
			self.GUI_Settings.bearing_gpioPinValueLabel.setText(str(value))




		self.GUI_Settings.bearing_gpioGetButton.clicked.connect(getPin)
		self.GUI_Settings.bearing_gpioSetButton.clicked.connect(setPin)