############################################ IRReceiver ############################################

	Jaime Portillo, 2021 (c)
	Madrid, Spain 

####################################################################################################

The module works capturing the duration os the pulse and translating to binary [0/1] 

It is necesary to set up some parameter once the module is instanced, 
after (myVar = IRReciver(myPin, myCallback))
	
	- total_bits		--> (default = 32)		# Nº of bits sended by remote (header included)
	- bool_limit		--> (default = 0.001)	# Limit where bits duration are considered as [1]
	- header_len		--> (default = 16)		# Nº of bits of the header
	- bit_max_duration 	--> (default = 0.0019)	# Limit where is not considered as data
	- bounce 			--> (default = 0.01)	# Time needed from last data to start to read
	- read_on			--> (default = 1)		# Read bits on reverse logic [1/0]

	*bounce*
	Recomended to add an extra filter for some buttons you want more bounce

	*read_on* 
	Some remote has inverse logic so bits need to be readed when data goes low


======================== HOW TO START ========================

# When the device captures new data it will be sended to the callback function
# Receiving data in the callback
def myCallback(data):
	print(data)

# Instance the module 
myVar = IRReceiver(myPin, myCallback)

# Setting some parameters
myVar.total_bits = 12 
myVar.header_len = 0
myVar.read_on = 0
myVar.bounce = 0.2 
myVar.bool_limit = 0.0012 # *Recomended default 
myVar.bit_max_duration = 0.0018 # *Recomended default

# Start event reader
myVar.startIRR()

# This keeps alive the program if there is no mainloop
input()

# Stops the event reader
myVar.stopIRR()





