import os 

class system_info:
	def __init__(self):
		self.cpu_temp = self.getCPUtemperature()
		self.ram_info = self.getRAMinfo()
		self.cpu_use = self.getCPUuse()
		self.disk_space = self.getDiskSpace()
		
		
	# Return CPU temperature as a character string                                      
	def getCPUtemperature(self):
		res = os.popen('vcgencmd measure_temp').readline()
		return(res.replace("temp=","").replace("'C\n",""))

	# Return RAM information (unit=kb) in a list                                        
	# Index 0: total RAM                                                                
	# Index 1: used RAM                                                                 
	# Index 2: free RAM                                                                 
	def getRAMinfo(self):
		p = os.popen('free')
		i = 0
		while 1:
			i = i + 1
			line = p.readline()
			if i==2:
				return(line.split()[1:4])

	# Return % of CPU used by user as a character string                                
	def getCPUuse(self):
		return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
	)))

	# Return information about disk space as a list (unit included)                     
	# Index 0: total disk space                                                         
	# Index 1: used disk space                                                          
	# Index 2: remaining disk space                                                     
	# Index 3: percentage of disk used                                                  
	def getDiskSpace(self):
		p = os.popen("df -h /")
		i = 0
		while 1:
			i = i +1
			line = p.readline()
			if i==2:
				return(line.split()[1:5])



