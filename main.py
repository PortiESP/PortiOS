from portiOSEssentials import *

#######################################################
class Main_GUI:
	def __init__(self, main_win):
		# Setting window
		self.win = main_win

		# Setting fullscreen
		# self.win.showFullScreen()

		# Getting central GUI
		self.GUI_Central = Ui_Central()
		self.GUI_Central.setupUi(self.win)

		# Setting media player
		self.isConnectedDevice = False
		self.BTController = BT_Control_Panel()
		self.startMediaPlayer()


		# Getting widgets
		self.GUI_Dashboard = Ui_Dashboard_widget()
		self.GUI_Dashboard.setupUi(self.GUI_Central.page_dashboard)
		self.GUI_Apps = Ui_Apps_widget()
		self.GUI_Apps.setupUi(self.GUI_Central.page_apps)
		self.GUI_Leds = Ui_Leds_widget()
		self.GUI_Leds.setupUi(self.GUI_Central.page_leds)
		self.GUI_Player = Ui_Player_widget()
		self.GUI_Player.setupUi(self.GUI_Central.page_player)
		self.GUI_Settings = Ui_Settings_widget()
		self.GUI_Settings.setupUi(self.GUI_Central.page_settings)

		# Widget funcs setup
		Central_funcs.centralSetup(self)
		Apps_funcs.appsSetup(self)
		Settings_funcs.settingsSetup(self)
		Dashboard_funcs.dashboardSetup(self)


		# Page test func

	def toogle_musicStatus(self, setStatus=None):
		
		if self.BTController.checkConnectedDevices():
			status = str(self.BTController.get_player_data('Status'))
			print(status)
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
			self.GUI_Central.footerButton_2.setIcon(icon1)


	def mediaDataChanged(self, _, data, __):
		print('Data changed:')
		event = list(dict(data).items())
		print(event)
		data = event[0]
		if str(data[0]) == 'Status': 
			self.toogle_musicStatus(str(self.BTController.get_player_data('Status')))

		elif str(data[0]) == 'Volume':
			self.GUI_Central.slider_volume.setValue(int(data[1]))

		Dashboard_funcs.changeMusicInfo(self)

	def startMediaPlayer(self):
		self.mediaPlayerThread = threading.Thread(target=self.mediaPlayerThreadFunc)
		self.mediaPlayerThread.start()

	def mediaPlayerThreadFunc(self):

		while 1:
			time.sleep(1)

			##################### CONNECTIONS MANAGER ###################################
			checkDevice = self.BTController.checkConnectedDevices()
			# Check for connected devices
			# Setting BT status disconnected
			if self.isConnectedDevice == True and checkDevice == False:
				icon = QIcon()
				icon.addFile(u":/icons-gray/Resources/Icons/bt_states/bluetooth_gray.png", QSize(), QIcon.Normal, QIcon.Off)
				self.GUI_Central.bluetoothStatusButton.setIcon(icon)
				self.isConnectedDevice = False
				continue

			# Setup on new connection
			if self.isConnectedDevice == False and checkDevice == True:
				time.sleep(1)
				self.BTController.setupInterfaces()
				self.isConnectedDevice = True
				# BT status icon on
				icon = QIcon()
				icon.addFile(u":/icons-gray/Resources/Icons/bt_states/bluetooth_blue.png", QSize(), QIcon.Normal, QIcon.Off)
				self.GUI_Central.bluetoothStatusButton.setIcon(icon)
				self.GUI_Central.slider_volume.setValue(self.BTController.get_volume_data())
				if str(self.BTController.get_player_data('Status')) == 'playing':
					self.toogle_musicStatus(setStatus='playing')
					Dashboard_funcs.changeMusicInfo(self)
				self.BTController.bus.add_signal_receiver(self.mediaDataChanged, 
											dbus_interface = "org.freedesktop.DBus.Properties",
            								signal_name = "PropertiesChanged",
            								 )
			###########################################################################

			# THREAD SETUP

			# Central clock
			self.GUI_Central.label_clock.setText(time.strftime('%H:%M'))

			# Volume slider
			sliderValue = self.GUI_Central.slider_volume.value()
			if sliderValue != self.BTController.localVolume:
				self.BTController.localVolume = sliderValue
				self.BTController.set_volume(str(sliderValue), maxlevel=127)

			# Music current time
			if str(self.BTController.get_player_data('Status')) == 'playing':
				currentMusicTime = self.BTController.get_player_data('Position')
				currentMusicTime =  Dashboard_funcs.formatDuration(int(currentMusicTime))
				self.GUI_Dashboard.label_currentTime.setText(currentMusicTime)
				print('Time elapsed --> ' + currentMusicTime)


			





#######################################################
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QMainWindow()
	main_gui = Main_GUI(win)
	win.show()
	sys.exit(app.exec_())


