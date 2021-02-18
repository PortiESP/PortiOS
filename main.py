from portiOSEssentials import *

#######################################################
class Main_GUI:
	def __init__(self, main_win):
		# Setting window
		self.win = main_win

		# Getting central GUI
		GUI_Central = Ui_Central()
		GUI_Central.setupUi(self.win)

		# Getting widgets
		GUI_Dashboard = Ui_Dashboard_widget()
		GUI_Dashboard.setupUi(GUI_Central.page_dashboard)
		GUI_Apps = Ui_Apps_widget()
		GUI_Apps.setupUi(GUI_Central.page_apps)
		GUI_Leds = Ui_Leds_widget()
		GUI_Leds.setupUi(GUI_Central.page_leds)
		GUI_Player = Ui_Player_widget()
		GUI_Player.setupUi(GUI_Central.page_player)
		GUI_Settings = Ui_Settings_widget()
		GUI_Settings.setupUi(GUI_Central.page_settings)

		# Widget funcs setup
		Main_funcs.main_funcs_setup(GUI_Central)

		# Page test func
		Main_funcs.pageTest(GUI_Central)


#######################################################
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QMainWindow()
	main_gui = Main_GUI(win)
	win.show()
	sys.exit(app.exec_())


