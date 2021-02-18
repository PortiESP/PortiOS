import threading
# from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Central_funcs:
	def centralSetup(frame):
		frame.volumeVisivility = False

		# frame.mediaPlayer = BT_Control_Panel()
		# Footer buttons events
		# frame.footerButton_1.clicked.connect(lambda:frame.mediaPlayer.playback_control('previous'))
		# frame.footerButton_2.clicked.connect(lambda:)
		# frame.footerButton_3.clicked.connect(lambda:)
		frame.footerButton_4.clicked.connect(lambda:Central_funcs.setPage(frame, 3))
		frame.footerButton_5.clicked.connect(lambda:Central_funcs.toogle_volume(frame))
		# frame.footerButton_6.clicked.connect(lambda:)
		pass
		
	def toogle_volume(frame):
		frame.volumeVisivility = (not frame.volumeVisivility)
		if frame.volumeVisivility:
			frame.frame_volume.raise_()
		else:
			frame.frame_volume.lower()


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