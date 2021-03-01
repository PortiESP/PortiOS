import dbus, re, subprocess
from dbus.mainloop.glib import DBusGMainLoop

class BT_Control_Panel:
	def __init__(self):
		DBusGMainLoop(set_as_default=True)

				
		self.bus = dbus.SystemBus()
		self.rootObj = self.bus.get_object('org.bluez', '/')

		self.mgrInterface = dbus.Interface(self.rootObj, 'org.freedesktop.DBus.ObjectManager')
		
		#Str de los objetos creados con la conexion bt
		self.connectedDeviceObjPath = None
		self.playerObjPath = None
		self.fdObjPath = None
				
		#Diccionarios con datos de la conexion
		self.adapterData = None
		self.deviceData = None
		self.mediaPlayerData = None
		self.volumeData = None
				

		#Device, Player, Control and volume interfaces
		self.deviceIface = None #Device data
		self.playerIface = None #Media data
		self.controlsIface = None #Media methods
		self.volumeIface = None #Volume data
		
		#Sound variable
		for i in subprocess.run(['amixer controls'], capture_output=True, text=True, shell=True).stdout.split('\n'):
			if re.findall('Master Playback Volume', i):
				self.numid = i.split(',')[0][-1]
				print('Volulume id: ', self.numid)

		self.AMIXER_MAX = 65536
				
	def setupInterfaces(self):
		#diccionario con todos los objetos 
		self.objects = self.mgrInterface.GetManagedObjects()

		#Setting up Paths, Data and Ifaces
		for objPath, interfaces in self.objects.items():
			#Get BT adapter
			if objPath == '/org/bluez/hci0':
				self.adapterData = self.objects[objPath]['org.bluez.Adapter1']
				
			#Listing device paired and setting paths and data
			if re.match('/org/bluez/hci0/dev_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}$', objPath):
				
				#Getting data dicts from connected device if object is actualy a devive
				if self.objects[objPath]['org.bluez.Device1']['Connected'] == 1:
					# Path, Iface
					self.connectedDeviceObjPath = objPath
					self.deviceIface = dbus.Interface(self.bus.get_object('org.bluez', self.connectedDeviceObjPath), 'org.freedesktop.DBus.Properties')
					self.playerObjPath = self.deviceIface.Get('org.bluez.MediaControl1', 'Player')
					self.playerIface = dbus.Interface(self.bus.get_object('org.bluez', self.playerObjPath), 'org.freedesktop.DBus.Properties')
					self.controlsIface = dbus.Interface(self.bus.get_object('org.bluez', self.playerObjPath), 'org.bluez.MediaPlayer1')
			# Check if object is /fd
			if self.connectedDeviceObjPath: 
				fd_regex = re.match(self.connectedDeviceObjPath+'/fd\d$', objPath)
				if fd_regex:					
					self.fdObjPath = fd_regex[0]
					self.volumeIface = dbus.Interface(self.bus.get_object('org.bluez', self.fdObjPath), 'org.freedesktop.DBus.Properties')
					self.volumeData = self.volumeIface.Get('org.bluez.MediaTransport1', 'Volume')
			
	def checkConnectedDevices(self):
		self.objects = self.mgrInterface.GetManagedObjects()
		for objPath, interfaces in self.objects.items():
			if re.match('/org/bluez/hci0/dev_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}$', objPath):
				if self.objects[objPath]['org.bluez.Device1']['Connected'] == 1:
					return True
		return False

	
	# Play,Stop,Next...
	def playback_control(self, cmd):
		try:
			if cmd == 'next': self.controlsIface.Next()
			elif cmd == 'previous': self.controlsIface.Previous()
			elif cmd == 'play': self.controlsIface.Play()
			elif cmd == 'pause': self.controlsIface.Pause()
			elif cmd == 'stop': self.controlsIface.Stop()
			elif cmd == 'fastforward': self.controlsIface.FastForward(); self.controlsIface.Play()
			elif cmd == 'rewind': self.controlsIface.Rewind(); self.controlsIface.Play()
			else: return False
		except:
			print('Playback_control error catched...!')	
					
	#Set volume value for RPi
	#The max value parameter indicates the max value you are using, default = 100
	def set_local_volume(self, level, maxlevel=100):
		#Format the level to base 65536
		levelf = str(self.formatBase(level, maxlevel, self.AMIXER_MAX))
		subprocess.run([f'amixer cset numid={self.numid} {str(levelf)}'], capture_output=True, text=True, shell=True)
		
	def set_remote_volume(self, level, maxlevel=100):
		level = dbus.UInt16(self.formatBase(level, maxlevel, 127))
		self.volumeIface.Set('org.bluez.MediaTransport1', 'Volume', level)

	def get_local_volume(self):
		return int(subprocess.run([f'amixer cget numid={self.numid}'], capture_output=True, text=True, shell=True).stdout.split('=')[-1].strip().split(',')[0])
	
	def get_player_data(self, data):
		try:
			return self.playerIface.Get('org.bluez.MediaPlayer1', data)
		except: return False
	
	def get_device_data(self, data):
		try:
			return self.deviceIface.Get('org.bluez.Device1', data)
		except: return False

	def get_volume_data(self):
		try:
			return int(self.volumeIface.Get('org.bluez.MediaTransport1', 'Volume'))
		except: return False

	def get_adapter_data(self, data):
		try:
			return self.adapterData[data]
		except: return False

	def formatBase(self, value, base1, base2):
		result = int((value /  base1) * base2)
		return result


