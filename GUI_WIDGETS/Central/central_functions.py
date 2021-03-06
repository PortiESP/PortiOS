from .ui_central import Ui_Central
import subprocess, threading

class Central_funcs:
	def centralSetup(self):
		# Getting interface
		self.GUI_Central = Ui_Central()
		self.GUI_Central.setupUi(self.win)

		# Flags
		self.GUI_Central.volumeVisivility = False
		self.GUI_Central.powerVisivility = False

		# Footer buttons events
		self.GUI_Central.footerButton_1.clicked.connect(lambda:self.BTController.playback_control('previous'))
		self.GUI_Central.footerButton_2.clicked.connect(self.toggle_musicStatus)
		self.GUI_Central.footerButton_3.clicked.connect(lambda:self.BTController.playback_control('next'))
		self.GUI_Central.footerButton_4.clicked.connect(lambda:Central_funcs.setPage(self, 3))
		self.GUI_Central.footerButton_5.clicked.connect(lambda:Central_funcs.toggle_volume(self))
		self.GUI_Central.footerButton_6.clicked.connect(lambda:Central_funcs.toggle_power(self))

		# Power menu
		self.GUI_Central.powerCloseButton.clicked.connect(lambda:Central_funcs.toggle_power(self))
		self.GUI_Central.centralShutdownButton.clicked.connect(lambda:subprocess.run('shutdown -P now', shell=True))
		self.GUI_Central.centralRebootButton.clicked.connect(lambda:subprocess.run('reboot', shell=True))
		# self.GUI_Central.centralExitButton.clicked.connect(lambda: self.app.exit())

		self.GUI_Central.slider_volume.valueChanged.connect(self.sliderSyncVolume)
		
	def toggle_volume(self):
		self.GUI_Central.volumeVisivility = (not self.GUI_Central.volumeVisivility)
		if self.GUI_Central.volumeVisivility:
			self.GUI_Central.frame_volume.raise_()
		else:
			self.GUI_Central.frame_volume.lower()

	def toggle_power(self):
		self.GUI_Central.powerVisivility = (not self.GUI_Central.powerVisivility)
		if self.GUI_Central.powerVisivility:
			self.GUI_Central.frame_power.raise_()
		else:
			self.GUI_Central.frame_power.lower()

	def setPage(self, index):
		self.GUI_Central.appsWidget.setCurrentIndex(index)

	


