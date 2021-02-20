from portiOSEssentials import *

#######################################################
class Main_GUI:
	def __init__(self, main_win):
		# Setting window
		self.win = main_win

		# Setting fullscreen
		self.win.showFullScreen()

		# Create log file
		log = open('/home/pi/Desktop/GUI_Log.txt', 'w')
		log.close()

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
		Central_funcs.centralSetup(self.GUI_Central, self.BTController)
		Apps_funcs.appsSetup(self.GUI_Apps, self.GUI_Central.stackedWidget)
		Settings_funcs.settingsSetup(self.GUI_Settings)

		# Page test func

	def startMediaPlayer(self):
		self.writeLog('Media Player Thread starting...')
		self.mediaPlayerThread = threading.Thread(target=self.mediaPlayerThreadFunc)
		self.mediaPlayerThread.start()

	def mediaPlayerThreadFunc(self):
		self.writeLog('Media Player Thread started...')

		while 1:
			time.sleep(0.1)
			checkDevice = self.BTController.checkConnectedDevices()
			self.writeLog('Connection status: ' + str(checkDevice))
			# Check for connected devices
			if checkDevice == False:
				self.isConnectedDevice = False
				self.writeLog('No bt connection...')
				time.sleep(0.4)
				continue
				exit

			# Setup on new connection
			if self.isConnectedDevice == False and checkDevice == True:
				self.BTController.setupInterfaces()
				self.isConnectedDevice = True
				self.writeLog('Connection success...')



			# Update data
			self.BTController.update_data()
			
			self.writeLog('Volume data: ' + self.BTController.volumeData)
			self.writeLog('Volume local: ' + self.BTController.localVolume)
			# Sincronize volume
			if self.BTController.localVolume != self.BTController.volumeData:
				self.writeLog('Volume changed to: ' + self.BTController.volumeData)
				self.BTController.set_volume(self.BTController.volumeData)

	def writeLog(self, msg):
		with open('/home/pi/Desktop/GUI_Log.txt', 'a') as log:
			log.write(msg + ' - ' + time.strftime('%H:%M:%S') + '\n')
			





#######################################################
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QMainWindow()
	main_gui = Main_GUI(win)
	win.show()
	sys.exit(app.exec_())


