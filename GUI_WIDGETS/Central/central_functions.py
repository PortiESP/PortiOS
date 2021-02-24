import sys
sys.path.append("../../.")
from main import *
# from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Central_funcs(Main_GUI):
	def __init__(self, frame):
		self.centralSetup(frame)


	def centralSetup(self, frame):
		self.frame = frame
		# Flags
		self.frame.volumeVisivility = False
		self.frame.powerVisivility = False

		# Footer buttons events
		self.frame.footerButton_1.clicked.connect(lambda:self.BTController.playback_control('previous'))
		self.frame.footerButton_2.clicked.connect(self.toogle_musicStatus)
		self.frame.footerButton_3.clicked.connect(lambda:self.BTController.playback_control('next'))
		self.frame.footerButton_4.clicked.connect(lambda:self.setPage(3))
		self.frame.footerButton_5.clicked.connect(self.toogle_volume)
		self.frame.footerButton_6.clicked.connect(self.toogle_power)

		# Power menu
		self.frame.powerCloseButton.clicked.connect(self.toogle_power)
		self.frame.centralShutdownButton.clicked.connect(lambda:subprocess.run('shutdown -P now', shell=True))
		self.frame.centralRebootButton.clicked.connect(lambda:subprocess.run('reboot', shell=True))

		
		
	def toogle_volume(self):
		print('Toogleing volume')
		self.frame.volumeVisivility = (not self.frame.volumeVisivility)
		if self.frame.volumeVisivility:
			self.frame.frame_volume.raise_()
		else:
			self.frame.frame_volume.lower()

	def toogle_power(self):
		print('Toogleing power')
		self.frame.powerVisivility = (not self.frame.powerVisivility)
		if self.frame.powerVisivility:
			self.frame.frame_power.raise_()
		else:
			self.frame.frame_power.lower()

	def setPage(self, index):
		print('Changing to page ',index)
		self.frame.stackedWidget.setCurrentIndex(index)


