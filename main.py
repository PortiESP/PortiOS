from portiOSEssentials import *

#######################################################
class Main_GUI:
	def __init__(self, main_win):
		# Setting window
		self.win = main_win

		# Setting fullscreen
		self.win.showFullScreen()

		# Setting media player
		self.startMediaPlayer()

		# Getting central GUI
		GUI_Central = Ui_Central()
		GUI_Central.setupUi(self.win)


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
		self.Central_funcs.centralSetup(self.GUI_Central, self.BTController)
		self.Apps_funcs.appsSetup(self.GUI_Apps, self.GUI_Central.stackedWidget)
		self.Settings_funcs.settingsSetup(self.GUI_Settings)

		# Page test func

	def startMediaPlayer(self):
		self.BTController = BT_Control_Panel()
		self.mediaPlayerThread = threading.Thread(target=self.mediaPlayerThreadFunc)

	def mediaPlayerThreadFunc(self):
		while self.mediaPlayerThread:
			self.BTController.update_data()
			if self.BTController.localVolume != self.BTController.volumeData:
				self.BTController.set_volume(self.BTController.volumeData)

			time.sleep(0.1)
			





#######################################################
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QMainWindow()
	main_gui = Main_GUI(win)
	win.show()
	sys.exit(app.exec_())


