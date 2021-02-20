import dbus, re, subprocess
from dbus.mainloop.glib import DBusGMainLoop

class BT_Control_Panel:
	def __init__(self):
		DBusGMainLoop(set_as_default=True)

				
		self.bus = dbus.SystemBus()
		self.rootObj = self.bus.get_object('org.bluez', '/')

		self.mgrInterface = dbus.Interface(self.rootObj, 'org.freedesktop.DBus.ObjectManager')
		#diccionario con todos los objetos 
		self.objects = self.mgrInterface.GetManagedObjects()

		
		#Lista con (str) de los objetos de los dispositivos guardados
		self.devicesList = []
		
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
			elif re.findall('Master Playback Switch', i):
				self.muteid = i.split(',')[0][-1]
		self.mute = 1
		self.localVolume = subprocess.run([f'amixer cget numid={self.numid}'], capture_output=True, text=True, shell=True).stdout.split('=')[-1].strip().split(',')
		
		
		
		#Setting up Paths, Data and Ifaces
		for objPath, interfaces in self.objects.items():
			#Get BT adapter
			if objPath == '/org/bluez/hci0':
				self.adapterData = self.objects[objPath]['org.bluez.Adapter1']
				
			#Listing device paired and setting paths and data
			if re.match('/org/bluez/hci0/dev_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}_[0-9A-Z]{2}$', objPath):
				#List device
				if not objPath in self.devicesList:
					self.devicesList.append(objPath)
					
				# -
				
				# -
					
				#Getting data dicts from connected device if object is actualy a devive
				if self.objects[objPath]['org.bluez.Device1']['Connected'] == 1:
					# Device PAth, Iface, Data
					self.connectedDeviceObjPath = objPath
					self.deviceIface = dbus.Interface(self.bus.get_object('org.bluez', self.connectedDeviceObjPath), 'org.freedesktop.DBus.Properties')
					self.deviceData = dict(self.deviceIface.GetAll('org.bluez.Device1'))
					# Media player Path, Iface, methodsIface, Data
					self.playerObjPath = self.deviceIface.Get('org.bluez.MediaControl1', 'Player')
					self.playerIface = dbus.Interface(self.bus.get_object('org.bluez', self.playerObjPath), 'org.freedesktop.DBus.Properties')
					self.controlsIface = dbus.Interface(self.bus.get_object('org.bluez', self.playerObjPath), 'org.bluez.MediaPlayer1')
					self.mediaPlayerData = dict(self.playerIface.GetAll('org.bluez.MediaPlayer1'))
			# Check if object is /fd
			if self.connectedDeviceObjPath: 
				fd_regex = re.match(self.connectedDeviceObjPath+'/fd\d$', objPath)
				if fd_regex:					
					self.fdObjPath = fd_regex[0]
					self.volumeIface = dbus.Interface(self.bus.get_object('org.bluez', self.fdObjPath), 'org.freedesktop.DBus.Properties')
					self.volumeData = self.volumeIface.Get('org.bluez.MediaTransport1', 'Volume')
			
		
	
	def update_data(self):
		try:
			self.deviceData.update(self.deviceIface.GetAll('org.bluez.Device1'))
			self.mediaPlayerData.update(self.playerIface.GetAll('org.bluez.MediaPlayer1'))
			for key, value in self.playerIface.GetAll('org.bluez.MediaPlayer1').items():
				if isinstance(value, dbus.Dictionary):
					self.mediaPlayerData[key].update(value)
				else: self.mediaPlayerData[key] = value
			self.volumeData = self.volumeIface.Get('org.bluez.MediaTransport1', 'Volume')
		except AttributeError:
			return False

	
	# Play,Stop,Next...
	def playback_control(self, cmd):
		if cmd == 'next': self.controlsIface.Next()
		elif cmd == 'previous': self.controlsIface.Previous()
		elif cmd == 'play': self.controlsIface.Play()
		elif cmd == 'pause': self.controlsIface.Pause()
		elif cmd == 'stop': self.controlsIface.Stop()
		elif cmd == 'fastforward': self.controlsIface.FastForward(); self.controlsIface.Play()
		elif cmd == 'rewind': self.controlsIface.Rewind(); self.controlsIface.Play()
		else: return False
					
					
	#Set volume value for RPi
	#The max value parameter indicates the max value you are using, default = 100
	def set_volume(self, level, maxlevel=100):
		stereo = bool(re.findall(',', level))

		#Format the level to base 65536
		if level != 'mute':
			if stereo:
				level = level.split(',')
				level = list(map(lambda lvl:str(int(lvl) /  maxlevel*65536), level))
				level = ','.join(level)
				self.localVolume = level
			else: 
				levelr = lambda lvl:str(int(lvl) /  maxlevel*65536)
				self.localVolume = levelr(level)
				
		
		#Get mute status
		self.mute = subprocess.run((f'amixer cget numid={self.muteid}'), capture_output=True, text=True, shell=True).stdout.strip()[-1]	
		if self.mute == 'n': 
			self.mute = 1 
		elif self.mute == 'f': 
			self.mute = 0
		
		#Sets the volume
		if level == 'mute':
			self.mute = int(not self.mute)
			subprocess.run([f'amixer cset numid={self.muteid} {self.mute}'], capture_output=True, text=True, shell=True)
		else:
			output = subprocess.run([f'amixer cset numid={self.numid} {str(self.localVolume)}'], capture_output=True, text=True, shell=True)
			if self.mute == 0:
				subprocess.run([f'amixer cset numid={self.muteid} 1'], capture_output=True, text=True, shell=True)
	
	
	def get_player_data(self, data):
		try:
			return self.mediaPlayerData[data]
		except KeyError:
			return False
	
	def get_device_data(self, data):
		try:	
			return self.deviceData[data]
		except KeyError:
			return False
	
	
		
	# DEBUGING METHODS #	
		
	
	#Imprime todos los datos de todos los objetos
	def printAllData(self):
		print('---------------- ADAPTER DATA ---------------')
		for key, value in self.adapterData.items():
			print(f'\t{key}: {value}')
		print('---------------- DEVICES LIST ---------------')
		for i in self.devicesList:
			print(i)
		print("----------- CONNECTED DEVICE DATA -----------")
		print()
		print('DEVICE DATA')
		for key, value in self.deviceData.items():
			print(f'\t{key}: {value}')
		print()
		print('MEDIA PLAYER DATA')
		for key, value in self.mediaPlayerData.items():
			if key == 'Track':
				print(f'\t{key}:')
				for key, value in value.items():
					print(f'\t    |---- {key}: {value}')
				continue
			print(f'\t{key}: {value}')
		print('\tPlayer iface path: ',self.playerObjPath)
		print()
		print('VOLUME DATA')
		print(f'\tVolume: {self.volumeData}')
		print(f'\tlocalVolume: {self.localVolume}')
		print()
		

		
		
	#Funcion Poliformica para testear otras funciones
	def test(self, func, *val):
		return func(*val)
		
		
		
	# Get introspect info about an object
	def introspect(self, iface):
		from xml.dom.minidom import parseString as parse
		
		intros = dbus.Interface(self.bus.get_object('org.bluez', iface), 'org.freedesktop.DBus.Introspectable')
		dom = parse(intros.Introspect())
		dom = dom.toprettyxml()
		print(dom)
		






