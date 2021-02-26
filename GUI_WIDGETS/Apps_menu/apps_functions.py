


class Apps_funcs:

	def appsSetup(self):
		# Apps buttons
		# frame.pushButton.clicked.connect(lambda:)
		# frame.pushButton_2.clicked.connect(lambda:)
		self.GUI_Apps.pushButton_3.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(4))
		self.GUI_Apps.pushButton_4.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(0))
		self.GUI_Apps.pushButton_5.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(1))
		self.GUI_Apps.pushButton_6.clicked.connect(lambda:self.GUI_Central.appsWidget.setCurrentIndex(2))