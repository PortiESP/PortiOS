import threading
from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Main_funcs:
	def main_funcs_setup(frame):
		frame.mediaPlayer = BT_Control_Panel()
		Main_funcs.centralSetup(frame)


	def centralSetup(frame):
		# Footer buttons events
		# frame.footerButton1.clicked.connect(lambda:frame.mediaPlayer.playback_control('previous'))
		# frame.footerButton2.clicked.connect(lambda:)
		# frame.footerButton3.clicked.connect(lambda:)
		# frame.footerButton4.clicked.connect(lambda:)
		# frame.footerButton5.clicked.connect(lambda:)
		# frame.footerButton6.clicked.connect(lambda:)
		pass
		



	def setPage(frame, index):
		frame.stackedWidget.setCurrentIndex(index)





	def pageTest(frame):
		def hilo():
			while 1:
				page = int(input('Page: '))
				Main_funcs.setPage(frame, page)

		t1 = threading.Thread(target=hilo)
		t1.start()