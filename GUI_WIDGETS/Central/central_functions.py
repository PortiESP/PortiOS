import threading, time, subprocess, os, dbus
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
# from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Frame will be GUI_Central object
class Central_funcs:
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

		# Slider volume
		self.frame.slider_volume.valueChanged.connect(lambda:self.mediaPlayer.set_volume(str(self.frame.slider_volume.value()), maxlevel=127))

		mediaPlayer.bus.add_signal_receiver(self.mediaDataChanged, 
											dbus_interface = "org.freedesktop.DBus.Properties",
            								signal_name = "PropertiesChanged",
            								 )

	def mediaDataChanged(self, _, data, __):
		print('Data changed:')
		print(list(dict(data).items()))
		data = list(dict(data).items())[0]
		if str(data[0]) == 'Status': 
			self.toogle_musicStatus()

		if str(data[0]) == 'Volume':
				self.mediaPlayer.set_volume(str(data[1]), maxlevel=127)
				



	def toogle_musicStatus(self):
		
		if self.mediaPlayer.checkConnectedDevices():
			status = self.mediaPlayer.playerIface.Get('org.bluez.MediaPlayer1', 'Status')
			
			icon1 = QIcon()
			if status == 'playing':
				name = 'pause-fill'
				self.mediaPlayer.playback_control('pause')
			elif status == 'paused':
				name = 'play-fill'
				self.mediaPlayer.playback_control('pause')
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


