from .ui_apps_menu import Ui_Apps_widget
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import threading


class Apps_funcs:

	def appsSetup(self):
		# Getting interface
		self.GUI_Apps = Ui_Apps_widget()
		self.GUI_Apps.setupUi(self.GUI_Central.page_apps)
		
		# Apps buttons
		self.GUI_Apps.pushButton.clicked.connect(lambda: Apps_funcs.openBrowser(self))
		self.GUI_Apps.pushButton_2.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(5))
		self.GUI_Apps.pushButton_3.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(4))
		self.GUI_Apps.pushButton_4.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(0))
		self.GUI_Apps.pushButton_5.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(1))
		self.GUI_Apps.pushButton_6.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(2))

	def openBrowser(self):
		self.GUI_Apps.chrome_options = Options()
		# self.GUI_Apps.chrome_options.add_argument("--kiosk")
		self.GUI_Apps.chrome_options.add_experimental_option("useAutomationExtension", False)
		self.GUI_Apps.chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
		self.GUI_Apps.chrome_options.add_argument("--start-maximized")
		self.GUI_Apps.driver = webdriver.Chrome(options=self.GUI_Apps.chrome_options)
		self.GUI_Apps.driver.get('https://www.google.es/')

	