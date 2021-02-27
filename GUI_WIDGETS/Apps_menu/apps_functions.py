from selenium.webdriver.chrome.options import Options
from selenium import webdriver



class Apps_funcs:

	def appsSetup(self):
		# Apps buttons
		self.GUI_Apps.pushButton.clicked.connect(lambda: Apps_funcs.openBrowser(self))
		# frame.pushButton_2.clicked.connect(lambda:)
		self.GUI_Apps.pushButton_3.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(4))
		self.GUI_Apps.pushButton_4.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(0))
		self.GUI_Apps.pushButton_5.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(1))
		self.GUI_Apps.pushButton_6.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(2))

	def openBrowser(self):
		self.GUI_Apps.chrome_options = Options()
		self.GUI_Apps.chrome_options.add_argument("--start-maximizef")
		self.GUI_Apps.driver = webdriver.Chrome(options=self.GUI_Apps.chrome_options, executable_path='GUI_PACKAGES/navigator_google_maps/chromedriver.exe')
		self.GUI_Apps.drive.get('https://www.google.es/')