# Bluetooth controller with dbus bluez bus
# By Jaime Portillo (2021)(C)

# ---- bt_control_panel.py ---- #

[Imports] - dbus, re, subprocess, dbus.mainloop.glib.DBusMainLoop

[Class] - BT_Control_Panel #No params

	[Attributes]
	
	#General
	- objects # (dict) Gets a dict of all objects of org.bluez
	
	#Object paths
	- connectedDeviceObjPath # (str) Path of the device object

	- playerObjPath # (str) Path of the Media Player object

	- fdObjPath # (str) Path of the fd object
	
	#Interfaces DATA
	- adapterData # (dict) Data of the hci0 object

	- deviceData # (dict) Data of de root device object

	- mediaPlayerData # (dict) Data of the Media Player

	- volumeData # (str < int) Data of the remote volume

	#Object interfaces
	#(see introspect interface for more info)
	- deviceIface # (Interface) 'org.freedesktop.DBus.Properties'

	- playerIface # (interface) 'org.freedesktop.DBus.Properties'

	- controlsIface # (Interface) 'org.bluez.MediaPlayer1'

	- volumeIface # (Interface) 'org.freedesktop.DBus.Properties'

	#Volume attr
	- mute # (bool < int) # Mute status of the local device

	- localVolume (str < int) # Volume value of the local device


	[Methods]
	- update_data() # Updates the *Data Attributes (recomended loop)
		#No params
	- playback_control(command) # Manages the playback funcs
		+ command # (str) 
			#options = ['play', 'pause', 'next', 'previous', 'fastforward', 'rewind']

	- set_volume (level, maxlevel) # Sets the volume in the local device
		+ level # (str)	Volume level,
			#For mono input level=(str) ej. level='60'
			#For stereo input level=(str,str) ej. level='80,20'
		+ levelmax # (str) Maximum level in range (default = 100)
			#ej. levelmax=1000
	
	- get_player_data(data) # Gets some data from 'org.bluez.MediaPlayer1' interface
		+ data # (str) See introspect to show a list of all data
			#ej. data='Track'

    - get_device_data(data) # Gets some data from 'org.bluez.Device1' interface
            + data # (str) See introspect to show a list of all data  
                    #ej. data='Alias'
	
	- print_all_data() # Prints a list of all data

	- introspect(interface) # Prints a pretty xml formated file of all attributes and methods of an interface
		+ interface # (str) 
			#ej. interface='org.bluez.MediaPlayer1'

