


class Apps_funcs:

	def appsSetup(frame, widget):
		# Apps buttons
		# frame.pushButton.clicked.connect(lambda:)
		# frame.pushButton_2.clicked.connect(lambda:)
		frame.pushButton_3.clicked.connect(lambda:widget.setCurrentIndex(4))
		frame.pushButton_4.clicked.connect(lambda:widget.setCurrentIndex(0))
		frame.pushButton_5.clicked.connect(lambda:widget.setCurrentIndex(1))
		frame.pushButton_6.clicked.connect(lambda:widget.setCurrentIndex(2))