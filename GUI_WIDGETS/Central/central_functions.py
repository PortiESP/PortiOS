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
		def sliderVolumeEvent():
			self.mediaPlayer.set_volume(str(self.frame.slider_volume.value()))
			self.mediaPlayer.volumeIface.Set('org.bluez.MediaTransport1', 'Volume', dbus.UInt16(self.frame.slider_volume.value()))
		self.frame.slider_volume.sliderMoved.connect(sliderVolumeEvent)

		# Setting time
		self.frame.timeThread = threading.Thread(target=self.setTime)
		self.frame.timeThread.start()

		mediaPlayer.bus.add_signal_receiver(self.mediaDataChanged, 
											dbus_interface = "org.freedesktop.DBus.Properties",
            								signal_name = "PropertiesChanged",
            								 )

	def mediaDataChanged(self, _, data, __):
		data = list(dict(data).items())[0]
		if data[0] == 'Status': self.toogle_musicStatus()



	def toogle_musicStatus(self):
		
		if self.mediaPlayer.checkConnectedDevices():
			icon1 = QIcon()
			if self.mediaPlayer.get_player_data('Status') == 'playing':
				name = 'play-fill'
				self.mediaPlayer.playback_control('pause')
			else: 
				name = 'pause-fill'
				self.mediaPlayer.playback_control('play')
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

	def setTime(self):
		while self.frame.timeThread:
			self.frame.label_clock.setText(time.strftime('%H:%M'))
			time.sleep(1)

	def setPage(self, index):
		print('Changing to page ',index)
		self.frame.stackedWidget.setCurrentIndex(index)


	def writeLog(self, msg):
		with open('/home/pi/Desktop/GUI_Log.txt', 'a') as log:
			log.write(msg + ' - ' + time.strftime('%H:%M:%S') + '\n')

	def pageTest(self):
		def hilo():
			while 1:
				page = int(input('Page: '))
				self.setPage(page)

		t1 = threading.Thread(target=hilo)
		t1.start()