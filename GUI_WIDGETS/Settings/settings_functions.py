from .ui_design_settings import Ui_Settings_widget
from ..Dashboard.dashboard_functions import Dashboard_funcs
import subprocess, threading, re, time, os
import RPi.GPIO as gp


class Settings_funcs:
	def settingsSetup(self):
		# Getting interface
		self.GUI_Settings = Ui_Settings_widget()
		self.GUI_Settings.setupUi(self.GUI_Central.page_settings)

		# BT
		self.GUI_Settings.TIMEOUT = 20
		self.GUI_Settings.BTdataDict = {}

		# Remote
		self.GUI_Settings.remoteButtons = {
			'1010001001011101' : 'power',
			'0010001011011101' : 'prev',
			'0000001011111101' : 'play',
			'1100001000111101' : 'next',
			'0110001010011101' : 'vol+',
			'1010100001010111' : 'vol-',
			'1001000001101111' : 'up',
			'1110000000011111' : 'down',
			'1110001000011101' : 'func/stop',
			'1001100001100111' : 'eq',
			'1011000001001111' : 'st/rept',
			'0110100010010111' : '0',
			'0011000011001111' : '1',
			'0001100011100111' : '2',
			'0111101010000101' : '3',
			'0001000011101111' : '4',
			'0011100011000111' : '5',
			'0101101010100101' : '6',
			'0100001010111101' : '7',
			'0100101010110101' : '8',
			'0101001010101101' : '9'
		}

		# Setting pages
		self.GUI_Settings.bearing_settingsWifi.clicked.connect(lambda:Settings_funcs.setPage(self, 1))
		self.GUI_Settings.bearing_settingsBluetooth.clicked.connect(lambda:Settings_funcs.setPage(self, 2))
		self.GUI_Settings.bearing_settingsRemote.clicked.connect(lambda:Settings_funcs.setPage(self, 3))
		self.GUI_Settings.bearing_settingsNavigator.clicked.connect(lambda:Settings_funcs.setPage(self, 4))
		self.GUI_Settings.bearing_settingsStatus.clicked.connect(lambda:Settings_funcs.setPage(self, 5))
		self.GUI_Settings.bearing_settingsGpio.clicked.connect(lambda:Settings_funcs.setPage(self, 6))
		self.GUI_Settings.bearing_settingsSystemInfo.clicked.connect(lambda:Settings_funcs.setPage(self, 7))
		self.GUI_Settings.bearing_settingsTerminal.clicked.connect(lambda:Settings_funcs.setPage(self, 8))
		self.GUI_Settings.bearing_settingsAdvanced.clicked.connect(lambda:Settings_funcs.setPage(self, 9))

		# Setting up pages bearings
		Settings_funcs.wifiSetup(self)
		Settings_funcs.btSetup(self)
		Settings_funcs.remoteSetup(self)
		Settings_funcs.navigatorSetup(self)
		Settings_funcs.servicesStatusSetup(self)
		Settings_funcs.gpioSetup(self)
		Settings_funcs.systemInfoSetup(self)
		Settings_funcs.terminalSetup(self)
		Settings_funcs.advancedSetup(self)

	def setPage(self, index):
		self.GUI_Settings.stackedWidget_settings.setCurrentIndex(index)


# ----------------------------------------- MENUS SETUP -------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------

	def wifiSetup(self):

		# FUNCTIONS
		def refresh():
			self.GUI_Settings.bearing_wifiSsidText.setText(str(getSSID())) # SSID
			self.GUI_Settings.bearing_wifiIpText.setText(str(getIP()))     # IP
			
			if checkController():
				self.GUI_Settings.bearing_wifiPowerCheckbox.setChecked(True)
			else:
				self.GUI_Settings.bearing_wifiPowerCheckbox.setChecked(False)

		def togglePower():
			if self.GUI_Settings.bearing_wifiPowerCheckbox.isChecked(): 
				setStatus = 'up'
			else: 
				setStatus = 'down'
			subprocess.run([f'sudo ifconfig wlan0 {setStatus}'], shell=True)
			tstart = time.time()
			def waitNetwork(tstart):
				while not getSSID():
					time.sleep(0.5)
					if (time.time() - tstart) > self.GUI_Settings.TIMEOUT:
						break
				refresh()
			if setStatus == 'up':
				threading.Thread(target=waitNetwork, args=(tstart,)).start()
			else: 
				self.GUI_Settings.bearing_wifiSsidText.setText('None')
				self.GUI_Settings.bearing_wifiIpText.setText('None')
		def checkController():
			out = subprocess.run('ifconfig', capture_output=True, text=True, shell=True).stdout.split('\n')
			for line in out:
				if re.match('wlan0', line.strip()): return True
			return False


		def getSSID():
			try:
				out = subprocess.run('iwgetid', capture_output=True, text=True, shell=True).stdout.split(':')[1].strip()[1:-1]
			except IndexError:
				return None
			if out: return out
			else: return None

		def getIP():
			out = subprocess.run('ifconfig wlan0', capture_output=True, text=True, shell=True).stdout.split('\n')[1].strip().split(' ')
			if out[0] == 'inet': 
				out = out[1]
				return out
			else: return None
			
		def connectWifi():
			command = 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\ncountry=ES\n\nnetwork={{\nssid="{}"\npsk="{}"\nkey_mgmt=WPA-PSK\n}}'
			subprocess.run('sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf', capture_output=True, shell=True)
			with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
				f.write(command.format(self.GUI_Settings.bearing_wifiSSIDInput.text(), self.GUI_Settings.bearing_wifiPassInput.text()))
			
			out = subprocess.run('sudo wpa_cli -i wlan0 reconfigure', capture_output=True, text=True, shell=True)
			togglePower()

		
		# SETUP
		refresh()

		# EVENTS
		self.GUI_Settings.bearing_wifiPowerCheckbox.toggled.connect(togglePower)
		self.GUI_Settings.bearing_refreshWifiButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_wifiPassButton.clicked.connect(connectWifi)
		







# ------------------------------------------------------------------------------------------------------
	# BT SETUP
	def btSetup(self):
		def updateData():
			out = subprocess.run('bluetoothctl show', capture_output=True, text=True, shell=True).stdout
			dataLines = out.split('\n')
			for line in dataLines:
				line = line.strip()
				if re.match('Name', line): self.GUI_Settings.BTdataDict['Name'] = line.split(':')[1].strip()
				if re.match('Powered', line): self.GUI_Settings.BTdataDict['Powered'] = line.split(':')[1].strip()
				if re.match('Discoverable', line): self.GUI_Settings.BTdataDict['Discoverable'] = line.split(':')[1].strip()
			
			getConnectedDevice()


		def getConnectedDevice():
			if self.isConnectedDevice:
				name = str(self.BTController.get_device_data('Name'))
				if name == 'False': name = 'None'
			else: 
				name = 'None'
			self.GUI_Settings.BTdataDict['Connected'] = name

		def refresh():
			updateData() #dict values [yes/no]
			if self.GUI_Settings.BTdataDict['Powered'] == 'yes':
				self.GUI_Settings.bearing_btPowerCheckbox.setChecked(True)
				self.GUI_Settings.bearing_btNameText.setText(self.GUI_Settings.BTdataDict['Name'])
				self.GUI_Settings.bearing_btConnectedText.setText(self.GUI_Settings.BTdataDict['Connected'])
				if self.GUI_Settings.BTdataDict['Discoverable'] == 'yes':
					self.GUI_Settings.bearing_btDiscoverableCheckbox.setChecked(True)
				else:
					self.GUI_Settings.bearing_btDiscoverableCheckbox.setChecked(False)
			else:
				self.GUI_Settings.bearing_btPowerCheckbox.setChecked(False)
				self.GUI_Settings.bearing_btDiscoverableCheckbox.setChecked(False)



		def togglePower():
			if self.GUI_Settings.bearing_btPowerCheckbox.isChecked():
				subprocess.run('bluetoothctl power on', capture_output=True, shell=True)
				refresh()
			else:
				subprocess.run('bluetoothctl power off', capture_output=True, shell=True)

		def toggleDiscoverable():
			if self.GUI_Settings.bearing_btDiscoverableCheckbox.isChecked():
				setStatus = 'on'
			else:
				setStatus = 'off'
			subprocess.run(f'bluetoothctl discoverable {setStatus}', capture_output=True, shell=True)
			updateData()

		def openManager():
			def openMgr():
				time.sleep(1)
				os.system('xdotool search --name BTmanager windowraise')

			os.system('x-terminal-emulator -t BTmanager -e bluetoothctl')
			t = threading.Thread(target=openMgr)
			t.start()


		# SETUP
		refresh()

		# EVENTS
		self.GUI_Settings.bearing_refreshBtButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_btPowerCheckbox.toggled.connect(togglePower)
		self.GUI_Settings.bearing_btDiscoverableCheckbox.toggled.connect(toggleDiscoverable)
		self.GUI_Settings.bearing_btManagerButton.clicked.connect(openManager)




# ------------------------------------------------------------------------------------------------------

	def remoteSetup(self):
		def setup():
			self.GUI_Settings.bearing_remoteMultimediaCheckbox.setChecked(self.getConfig('irr_power'))
			self.GUI_Settings.bearing_remoteButtonsCheckbox.setChecked(self.getConfig('buttonsEnabled'))

			if self.getConfig('irr_power'):
				self.IRR.startIRR()
			if self.getConfig('buttonsEnabled'):
				startButtons()

		def startButtons():
			def callbackButtons(button):
				print(f"Button: {button}")

			for pin in self.pinsButtons:
				gp.setup(pin, gp.IN)
				gp.add_event_detect(pin, gp.RISING, callback=lambda x: callbackButtons(pin))

		def stopButtons():
			for pin in self.pinsButtons:
				gp.remove_event_detect(pin)

		def toggleMultimedia():
			if self.GUI_Settings.bearing_remoteMultimediaCheckbox.isChecked():
				self.IRR.startIRR()
			else:
				self.IRR.stopIRR()

		def toggleButtons():
			if self.GUI_Settings.bearing_remoteButtonsCheckbox.isChecked():
				self.setConfig('buttonsEnabled', "true")
				startButtons()
			else:
				self.setConfig('buttonsEnabled', "false")
				stopButtons()

		setup()
		self.GUI_Settings.bearing_remoteMultimediaCheckbox.toggled.connect(toggleMultimedia)
		self.GUI_Settings.bearing_remoteButtonsCheckbox.toggled.connect(toggleButtons)


# ------------------------------------------------------------------------------------------------------

	def navigatorSetup(self):
		def setHome():
			self.setConfig('home', self.GUI_Settings.bearing_navigatorHomeInput.text())
			self.GUI_Settings.bearing_navigatorHomeInput.setText('')

		self.GUI_Settings.bearing_navigatorHomeButton.clicked.connect(setHome)
		


# ------------------------------------------------------------------------------------------------------

	def servicesStatusSetup(self):
		def getServiceStatus(service):
			out = subprocess.run(f'systemctl is-active {service}', capture_output=True, text=True, shell=True).stdout.strip()
			return out


		def refresh():
			self.GUI_Settings.bearing_statusBtText.setText(getServiceStatus('bluetooth'))

		def restartService(service):
			subprocess.run(f'sudo systemctl restart {service}', shell=True)

		# EVENTS
		self.GUI_Settings.bearing_statusRefreshButton.clicked.connect(refresh)
		self.GUI_Settings.bearing_statusBtButton.clicked.connect(lambda: restartService('bluetooth'))

# ------------------------------------------------------------------------------------------------------

	def gpioSetup(self):

		def setPin():
			pin = int(self.GUI_Settings.bearing_gpioSetPinInput.text())
			value = int(self.GUI_Settings.bearing_gpioSetValueInput.text())
			gp.setup(pin, gp.OUT)
			gp.output(pin, value)
			self.GUI_Settings.bearing_gpioPinLabel.setText(str(pin))
			self.GUI_Settings.bearing_gpioPinValueLabel.setText(str(value))

		def getPin():
			pin = int(self.GUI_Settings.bearing_gpioGetInput.text())
			value = subprocess.run(f'gpio -1 read {pin}', capture_output=True, text=True, shell=True).stdout
			self.GUI_Settings.bearing_gpioPinLabel.setText('Pin: ' + self.GUI_Settings.bearing_gpioGetInput.text())
			self.GUI_Settings.bearing_gpioPinValueLabel.setText(str(value).strip())



		# EVENTS
		self.GUI_Settings.bearing_gpioGetButton.clicked.connect(getPin)
		self.GUI_Settings.bearing_gpioSetButton.clicked.connect(setPin)


# ------------------------------------------------------------------------------------------------------

	def systemInfoSetup(self):
		def refresh():
			# CPU
			self.GUI_Settings.bearing_systemCpuUseText.setText(str(self.systemInfo.getCPUuse()) + '%')
			self.GUI_Settings.bearing_systemCpuTempText.setText(str(self.systemInfo.getCPUtemperature()) + 'ºC')

			# RAM
			ram = self.systemInfo.getRAMinfo()
			ram = tuple(map(lambda i: str(round((int(i)*(10**(-6))), 1)) + 'G', ram))
			self.GUI_Settings.bearing_systemRamUsedText.setText(ram[1])
			self.GUI_Settings.bearing_systemRamFreeText.setText(ram[2])
			self.GUI_Settings.bearing_systemRamTotalText.setText(ram[0])

			# DISK
			diskSpace = self.systemInfo.getDiskSpace()
			self.GUI_Settings.bearing_systemDiskUsedText.setText(diskSpace[1])
			self.GUI_Settings.bearing_systemDiskFreeText.setText(diskSpace[2])
			self.GUI_Settings.bearing_systemDiskTotalText.setText(diskSpace[0])


		# EVENTS
		self.GUI_Settings.bearing_systemRefreshButton.clicked.connect(refresh)


# ------------------------------------------------------------------------------------------------------

	def terminalSetup(self):
		def openTerm():
			os.system('x-terminal-emulator -t newTerminal')
			os.system('xdotool search --name newTerminal windowraise')
		# EVENTS
		self.GUI_Settings.bearing_terminalOpenButton.clicked.connect(openTerm)


# ------------------------------------------------------------------------------------------------------

	def advancedSetup(self):
		def setup():	
			gp.setup(self.pinsPower, gp.IN, pull_up_down=gp.PUD_DOWN)
			self.GUI_Settings.bearing_advancedAutopowerCheckbox.setChecked(self.getConfig('auto-power'))
			self.GUI_Settings.bearing_advancedGaugePowerCheckbox.setChecked(self.getConfig('gauge_power'))

			# config
			if self.getConfig('auto-power'):
				gp.add_event_detect(self.pinsPower, gp.RISING, callback=autoPowerCallback)
			if self.getConfig('gauge_power'):
				Dashboard_funcs.startGauge(self)
			
		def autoPowerCallback(self):
			os.system('shutdown -P now')

		def toggleAutoPower():
			if self.GUI_Settings.bearing_advancedAutopowerCheckbox.isChecked():
				gp.add_event_detect(self.pinsPower, gp.RISING, callback=autoPowerCallback)
				self.setConfig('auto-power', 'true')
			else:
				gp.remove_event_detect(self.pinsPower)
				self.setConfig('auto-power', 'false')



		def toggleGaugePower():
			if self.GUI_Settings.bearing_advancedGaugePowerCheckbox.isChecked():
				Dashboard_funcs.startGauge(self)
				self.setConfig('gauge_power', 'true')
			else:
				Dashboard_funcs.stopGauge(self)
				self.setConfig('gauge_power', 'false')

		# SETUP
		setup()

		# EVENTS
		self.GUI_Settings.bearing_advancedAutopowerCheckbox.toggled.connect(toggleAutoPower)
		self.GUI_Settings.bearing_advancedGaugePowerCheckbox.toggled.connect(toggleGaugePower)
		self.GUI_Settings.bearing_advancedRebootButton.clicked.connect(lambda: os.system('sudo reboot'))