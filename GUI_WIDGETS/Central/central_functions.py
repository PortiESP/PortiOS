import threading, time, sys, subprocess, os, dbus
sys.path.append("../../.")
from main import *
# from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Central_funcs(Main_GUI):
	def centralSetup(self, frame, mediaPlayer):
		self.frame = frame
		self.mediaPlayer = mediaPlayer
		# Flags
		self.frame.volumeVisivility = False
		self.frame.powerVisivility = False

		# Footer buttons events
		self.frame.footerButton_1.clicked.connect(lambda:mediaPlayer.playback_control('previous'))
		self.frame.footerButton_2.clicked.connect(self.toogle_musicStatus)
		self.frame.footerButton_3.clicked.connect(lambda:mediaPlayer.playback_control('next'))
		self.frame.footerButton_4.clicked.connect(lambda:self.setPage(3))
		self.frame.footerButton_5.clicked.connect(self.toogle_volume)
		self.frame.footerButton_6.clicked.connect(self.toogle_power)

		# Power menu
		self.frame.powerCloseButton.clicked.connect(self.toogle_power)
		self.frame.centralShutdownButton.clicked.connect(lambda:subprocess.run('shutdown -P now', shell=True))
		self.frame.centralRebootButton.clicked.connect(lambda:subprocess.run('reboot', shell=True))

		# Slider default
		self.frame.slider_volume.setValue(100)	



	def toogle_musicStatus(self, setStatus=None):
		
		if self.BTController.checkConnectedDevices():
			status = self.BTController.playerIface.Get('org.bluez.MediaPlayer1', 'Status')
			print(status)
			if setStatus: 
				if setStatus == 'playing': status = 'paused'
				elif setStatus == 'paused': status = 'playing'

			icon1 = QIcon()
			if status == 'playing':
				name = 'play-fill'
				self.BTController.playback_control('pause')
			elif status == 'paused':
				name = 'pause-fill'
				self.BTController.playback_control('play')
			icon1.addFile(u":/icons_red/Resources/Icons/png-red/{}.png".format(name), QSize(30, 30), QIcon.Normal, QIcon.Off)
			self.frame.footerButton_2.setIcon(icon1)
		
		
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


