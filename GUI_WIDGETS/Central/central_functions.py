import threading, time
# from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Central_funcs:
	def centralSetup(frame, mediaPlayer):
		# Flags
		frame.volumeVisivility = False
		frame.powerVisivility = False

		# Footer buttons events
		# frame.footerButton_1.clicked.connect(lambda:mediaPlayer.playback_control('previous'))
		# frame.footerButton_2.clicked.connect(lambda:Central_funcs.toogle_musicStatus(frame))
		# frame.footerButton_3.clicked.connect(lambda:mediaPlayer.playback_control('previous'))
		frame.footerButton_4.clicked.connect(lambda:Central_funcs.setPage(frame, 3))
		frame.footerButton_5.clicked.connect(lambda:Central_funcs.toogle_volume(frame))
		frame.footerButton_6.clicked.connect(lambda:Central_funcs.toogle_power(frame))

		# Power menu
		frame.powerCloseButton.clicked.connect(lambda:Central_funcs.toogle_power(frame))

		# Setting time
		frame.timeThread = threading.Thread(target=Central_funcs.setTime)
		frame.timeThread.start()


	def toogle_musicStatus(frame):
		# Add icon toogle

		icon1 = QIcon()
		icon1.addFile(u":/icons_red/Resources/Icons/png-red/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
		frame.footerButton_2.setIcon(icon1)
		
		
	def toogle_volume(frame):
		print('Toogleing volume')
		frame.volumeVisivility = (not frame.volumeVisivility)
		if frame.volumeVisivility:
			frame.frame_volume.raise_()
		else:
			frame.frame_volume.lower()

	def toogle_power(frame):
		print('Toogleing power')
		frame.powerVisivility = (not frame.powerVisivility)
		if frame.powerVisivility:
			frame.frame_power.raise_()
		else:
			frame.frame_power.lower()

	def setTime(frame):
		while frame.timeThread:
			frame.label_clock.setText(time.strftime('%H:%M'))
			time.sleep(1)

	def setPage(frame, index):
		print('Changing to page ',index)
		frame.stackedWidget.setCurrentIndex(index)





	def pageTest(frame):
		def hilo():
			while 1:
				page = int(input('Page: '))
				Central_funcs.setPage(frame, page)

		t1 = threading.Thread(target=hilo)
		t1.start()