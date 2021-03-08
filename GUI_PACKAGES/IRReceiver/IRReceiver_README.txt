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


*read_on* 
Some remote has inverse logic so bits need to be readed when data goes low
