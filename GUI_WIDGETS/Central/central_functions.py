import threading, time, subprocess, os
# from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Central_funcs:
	def centralSetup(frame, mediaPlayer):
		# Flags
		frame.volumeVisivility = False
		frame.powerVisivility = False

		# Footer buttons events

		frame.footerButton_1.clicked.connect(lambda:mediaPlayer.playback_control('previous'))
		frame.footerButton_2.clicked.connect(lambda:Central_funcs.toogle_musicStatus(frame, mediaPlayer))
		frame.footerButton_3.clicked.connect(lambda:mediaPlayer.playback_control('next'))
		frame.footerButton_4.clicked.connect(lambda:Central_funcs.setPage(frame, 3))
		frame.footerButton_5.clicked.connect(lambda:Central_funcs.toogle_volume(frame))
		frame.footerButton_6.clicked.connect(lambda:Central_funcs.toogle_power(frame))

		# Power menu
		frame.powerCloseButton.clicked.connect(lambda:Central_funcs.toogle_power(frame))
		frame.centralShutdownButton.clicked.connect(lambda:subprocess.run('shutdown -P now', shell=True))
		frame.centralRebootButton.clicked.connect(lambda:subprocess.run('reboot', shell=True))

		# Setting time
		frame.timeThread = threading.Thread(target=Central_funcs.setTime, args=(frame,))
		frame.timeThread.start()

		


	def toogle_musicStatus(frame, mediaPlayer):
		
		if mediaPlayer.get_device_data('Connected'):
			icon1 = QIcon()
			if mediaPlayer.get_player_data('Status') == 'playing':
				name = 'play-button'
				mediaPlayer.playback_control('pause')
			else: 
				name = 'pause-fill'
				mediaPlayer.playback_control('play')
			icon1.addFile(u":/icons_red/Resources/Icons/png-red/{}.png".format(name), QSize(), QIcon.Normal, QIcon.Off)
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


	def writeLog(msg):
		with open('/home/pi/Desktop/GUI_Log.txt', 'a') as log:
			log.write(msg + ' - ' + time.strftime('%H:%M:%S') + '\n')

	def pageTest(frame):
		def hilo():
			while 1:
				page = int(input('Page: '))
				Central_funcs.setPage(frame, page)

		t1 = threading.Thread(target=hilo)
		t1.start()