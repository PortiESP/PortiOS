import RPi.GPIO as gp
import threading, time, subprocess

class GPIO_Controller():
	def __init__(self, mode=gp.BOARD):
		gp.setmode(gp.BOARD)
		gp.setwarnings(False)
		self.listenersList = []
		self.threadsHz = 5
		self.i2cHz = 40
	
	def setPinSetup(self, pin, setup='out', initial=False):
		if setup == 'out':
			gp.setup(pin, gp.OUT, initial=initial)
		elif setup == 'in':
			gp.setup(pin, gp.IN)
		else:
			return False
	
	def getPinSetup(self, pin):
		subprocess.run(f'echo {str(pin)} > /sys/class/gpio/export', capture_output=True, shell=True)
		out = subprocess.run(f'cat /sys/class/gpio/gpio{str(pin)}/direction', capture_output=True, text=True, shell=True).stdout
		print('Pin: ',pin, ' setup: ',out)
		subprocess.run('gpio unexportall', capture_output=True,shell=True)
		return out
		
	def setPinValue(self, pin, value):
		self.setPinSetup(pin)
		gp.output(pin, value)
		
	def getPinVale(self, pin):
		return gp.input(pin)
		
	def pinEventListener(self, pin, callback):
		# ~ Event listener
		def listener(pin, callback):
			laststatus = gp.input(pin)
			while listenerThread in self.listenersList:
				status = gp.input(pin)
				if status != laststatus:
					laststatus = status
					callback(pin, status)
				time.sleep(1/self.threadsHz)
			
		self.setPinSetup(pin, 'in')
		# ~ Thread create
		listenerThread = threading.Thread(target=listener, args=(pin, callback))
		self.listenersList.append(listenerThread)
		listenerThread.start()
		return listenerThread
		
	def destroyListener(self, listener):
		self.listenersList.pop(self.listenersList.index(listener))
		return self.listenersList

		
	def inputTest(self, pin, Hz=5):
		self.setPinSetup(pin, 'in')
		while 1:
			print(gp.input(pin))
			time.sleep(1/Hz)
			
	def createPWM(self, pin, Hz):
		self.setPinSetup(pin, 'out')
		pwm = gp.PWM(pin, Hz)
		pwm.start(0)
		
		return pwm
		
	def setPWM(self, obj, value, mapVal=False):
		if mapVal:
			value = (value / mapVal)*100
		print(value)
		obj.ChangeDutyCycle(value)
		
	def i2cEvent(self, pinSDA, pinCLK, callback, bits=4):
		self.setPinSetup(pinSDA, 'in')
		self.setPinSetup(pinCLK, 'in')
		self.i2cData = []
		def i2cEventBit(p, status):
			if status == 1:
				bit = gp.input(pinSDA)
				self.i2cData.append(bit)
				print('CLK: ', status, ' - data: ', self.i2cData)
				if len(self.i2cData) == bits:
					callback(self.i2cData)
					self.i2cData = []
			
					
				
		def listener(pin):
			laststatus = gp.input(pin)
			while listenerThread in self.listenersList:
				status = gp.input(pin)
				if status != laststatus:
					laststatus = status
					i2cEventBit(pin, status)
				time.sleep(1/self.i2cHz)
			
		self.setPinSetup(pinCLK, 'in')
		# ~ Thread create
		listenerThread = threading.Thread(target=listener, args=(pinCLK,))
		self.listenersList.append(listenerThread)
		listenerThread.start()
		return listenerThread
		
		






if __name__ == '__main__':
	c = GPIO_Controller()
	
	# ~ c.setPinValue(40, 0)
	
	# ~ c.inputTest(40, 100)	
	
	# ~ def events(p, status):
		# ~ print('Pin ', p, ': ', status)
	# ~ e = c.pinEventListener(40, events)

	# ~ p = c.createPWM(40, 50)
	# ~ while 1:
		# ~ c.setPWM(p, 100)
		
	def i2cCallback(data):
		print('I2C Data: ', data)
	c.i2cEvent(40, 38, i2cCallback)
	
		
	pass
