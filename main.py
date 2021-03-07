from portiOSEssentials import *

#######################################################
class Main_GUI:
	def __init__(self, main_win):
		# Setting window
		self.win = main_win

		# Setting fullscreen
		# self.win.showFullScreen()		

		if not os.path.exists('config.txt'):
			with open('config.txt', 'w'):
				print('"config.txt" created')

		self.config = {}
		self.setupConfig()

		self.mainLoopHz = 1

		# Setting media player
		self.isConnectedDevice = False
		self.BTController = BT_Control_Panel()
		self.startMediaPlayer()

		# GPIO setup
		gp.setmode(gp.BOARD)
		gp.setwarnings(False)

		# Leds controller
		self.ledsController = RGB_Controller((40, 38, 36)) # Pins

		# ADC converter controller
		self.adcController = Adafruit_ADS1x15.ADS1115()
		self.GAUGE_ADS_CHANNEL = 0
		self.MAX_ADS_VALUE = 32752

		# System info manager
		self.systemInfo = System_info()

		# Media info
		self.track = None # Track info dictionary
		self.songTitle = None
		self.songArtist = None
		self.trackDuration = None # Duration of the actual track
		self.currentMusicTime = None # Music position in microseconds
		self.currentMusicTimeF = None # Formated music porsition time (M:SS)

		self.GUI_Central = None
		self.GUI_Dashboard = None
		self.GUI_Apps = None
		self.GUI_Leds = None
		self.GUI_Player = None
		self.GUI_Settings = None

		# Widget funcs setup
		Central_funcs.centralSetup(self)
		Dashboard_funcs.dashboardSetup(self)
		Apps_funcs.appsSetup(self)
		Leds_funcs.ledsSetup(self)
		Player_funcs.playerSetup(self)
		Settings_funcs.settingsSetup(self)


		# Page test func

	def toggle_musicStatus(self, setStatus=None):
		
		if self.BTController.checkConnectedDevices():
			status = str(self.BTController.get_player_data('Status'))
			print('Status: ', status)
			if setStatus: 
				if setStatus == 'playing': status = 'paused'
				elif setStatus == 'paused': status = 'playing'

			icon1 = QIcon()
			if status == 'playing':
				name = 'play-fill'
				self.BTController.playback_control('pause')
			elif status == 'paused':
				name = 'pause-fill'
				self.BTController.playback_control('play')
			icon1.addFile(u":/icons_red/Resources/Icons/png-red/{}.png".format(name), QSize(30, 30), QIcon.Normal, QIcon.Off)
			# Changing central and player icon
			self.GUI_Central.footerButton_2.setIcon(icon1)
			self.GUI_Player.playButton.setIcon(icon1)

	# The sync system updates with the slider value
	def sliderSyncVolume(self):
		def volThread():
			s = self.GUI_Central.slider_volume.value()
			self.BTController.set_local_volume(s, maxlevel=127)
		

		t1 = threading.Thread(target=volThread)
		t1.start()

	def mediaDataChanged(self, _, data, __):
		print('Data changed:')
		key = list(dict(data).keys())[0]
		values = list(dict(data).values())[0]
		print('key --> ', key)
		print('values --> ', values)


		if key == 'Status': 
			self.toggle_musicStatus(str(self.BTController.get_player_data('Status')))

		elif key == 'Volume':
			self.GUI_Central.slider_volume.setValue(int(values))
			
				
		
		elif key == 'Track':
			self.track = values
			if len(self.track) == 1:
				self.trackDuration = int(self.track['Duration'])
			else:	
				self.songTitle = str(self.track['Title'])
				try:
					self.songArtist = str(self.track['Artist'])
				except KeyError:
					e = self.track['Title'].split('•')
					self.songTitle = e[0].strip()
					self.songArtist = e[1].strip()
			
			# Updating labels on all pages
			Dashboard_funcs.changeMusicInfo(self)		
			Player_funcs.changeMusicInfo(self)



	def formatDuration(self, duration):
		duration = int(duration)
		duration = ceil(duration / 1000)
		mins = int(duration / 60)
		segs = int(((duration / 60) - mins) * 60)
		return str(mins) + ':' + f'{segs:02}'

	def setupConfig(self):
		with open('config.txt', 'r') as file:
			lines = file.readlines()

			if not lines: return None
			
			header = None
			for line in lines:
				line = line.strip() # Removing endliners
				
				if not line: continue # Continue for empty lines

				if re.match('\[\w+\]', line): # Looking for headers
					continue
				
				if line[0] == '#': continue # Looking for comments

				line = line.split('=') 
				try:
					self.config[line[0]] = line[1]
				except IndexError:
					raise IOError('"config.txt" file has wrong format, ex: key=value')

		return self.config

	def getConfig(self, x):
		try:
			out = self.config[x]
		except KeyError:
			return None

		if out == 'true': return True
		elif out == 'false': return False
		elif re.match('.', out): 
			try:
				return float(out)
			except ValueError:
				pass
		try:
			return int(out)
		except ValueError:
			pass

		return out

	def setConfig(self, key, value):
		self.config[key] = value
		with open('config.txt', 'w') as file:
			lines = []
			for line in self.config.items():
				lines.append(f'{line[0]}={line[1]}\n')

			file.writelines(lines)


				




	def startMediaPlayer(self):
		self.mediaPlayerThread = threading.Thread(target=self.mediaPlayerThreadFunc)
		self.mediaPlayerThread.start()


	def mediaPlayerThreadFunc(self):

		while 1:
			time.sleep((1/self.mainLoopHz))

			##################### CONNECTIONS MANAGER ###################################
			try:
				checkDevice = self.BTController.checkConnectedDevices()
			except dbus.exceptions.DBusException:
				try:
					self.BTController = BT_Control_Panel()
				except:
					print('No BT object available')

			print(checkDevice, ' - ',self.isConnectedDevice)
			# Check for connected devices
			# Setting BT status disconnected
			if self.isConnectedDevice == True and checkDevice == False:
				self.isConnectedDevice = False
				icon = QIcon()
				icon.addFile(u":/bt_icons/Resources/Icons/bt_states/bluetooth_gray.png", QSize(), QIcon.Normal, QIcon.Off)
				self.GUI_Central.bluetoothStatusButton.setIcon(icon)
				continue

			# Setup on new connection
			if self.isConnectedDevice == False and checkDevice == True:
				time.sleep(1)
				self.BTController.setupInterfaces()
				self.isConnectedDevice = True
				# BT status icon on
				icon = QIcon()
				icon.addFile(u":/bt_icons/Resources/Icons/bt_states/bluetooth_blue.png", QSize(), QIcon.Normal, QIcon.Off)
				self.GUI_Central.bluetoothStatusButton.setIcon(icon)
				self.GUI_Central.slider_volume.setValue(self.BTController.get_volume_data())
				if str(self.BTController.get_player_data('Status')) == 'playing':
					self.toggle_musicStatus(setStatus='playing')
					
				self.BTController.bus.add_signal_receiver(self.mediaDataChanged, 
											dbus_interface = "org.freedesktop.DBus.Properties",
            								signal_name = "PropertiesChanged",
            								 )
			###########################################################################

			# THREAD SETUP

			# Central clock
			self.GUI_Central.label_clock.setText(time.strftime('%H:%M'))

			# When device is connected
			if checkDevice:

				# Music current time
				if str(self.BTController.get_player_data('Status')) == 'playing':
					# Formatin time 
					self.currentMusicTime = self.BTController.get_player_data('Position')
					self.currentMusicTimeF =  self.formatDuration(self.currentMusicTime)
					
					# Dashboard player
					if self.GUI_Central.appsWidget.currentIndex() == 0:
						self.GUI_Dashboard.label_currentTime.setText(self.currentMusicTimeF)
						self.GUI_Dashboard.slider_duration.setValue(self.currentMusicTime)

					# Media player
					elif self.GUI_Central.appsWidget.currentIndex() == 1:
						self.GUI_Player.label_currentTime.setText(self.currentMusicTimeF)
						self.GUI_Player.slider_duration.setValue(self.currentMusicTime)

					print('Time elapsed --> ' + self.currentMusicTimeF)

				






#######################################################
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QMainWindow()
	main_gui = Main_GUI(win)
	win.show()
	sys.exit(app.exec_())


