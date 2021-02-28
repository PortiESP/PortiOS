



class Apps_funcs:

	def appsSetup(self):
		# Apps buttons
		self.GUI_Apps.pushButton.clicked.connect(lambda: Apps_funcs.openBrowser(self))
		self.GUI_Apps.pushButton_2.clicked.connect(lambda: Apps_funcs.openNavigator(self))
		self.GUI_Apps.pushButton_3.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(4))
		self.GUI_Apps.pushButton_4.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(0))
		self.GUI_Apps.pushButton_5.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(1))
		self.GUI_Apps.pushButton_6.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(2))

	def openBrowser(self):
		print('Starting browser ')
		self.GUI_Apps.chrome_options = Options()
		self.GUI_Apps.chrome_options.add_experimental_option("useAutomationExtension", False)
		self.GUI_Apps.chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
		self.GUI_Apps.chrome_options.add_argument("--start-maximized")
		self.GUI_Apps.driver = webdriver.Chrome(options=self.GUI_Apps.chrome_options)
		self.GUI_Apps.driver.get('https://www.google.es/')

	def openNavigator(self):
		nav = Navegador()

		navThread = threading.Thread(target=lambda: Apps_funcs.navInstruction(self))
		navThread.start()

	def navInstructions(self):
		nav.iniciar_viaje()
		nav.mini_nav()



		