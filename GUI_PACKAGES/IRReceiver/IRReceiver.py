import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback):
		# Parameters
		self.pin = pin # IRR pin
		self.IRReceiverCallback = callback # User callback

		# GPIO setup
		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)

		# Remote parameters (format of the data)
		self.headers_len = 16
		self.data_len = 16
		self.total_data_len = None
		self.data_diference = 0.001

		# Program vars
		self.lastRead = 0 # Anti-bounce clock
		self.reading = False # Reading data
		self.raise_time = 0 # Bit start time
		self.bits_durations_list = [] # Bits readed 


	def startIRR(self):
		self.total_data_len = self.headers_len + self.data_len
		gp.add_event_detect(self.pin, gp.BOTH, callback=self.__IREvent)

	def stopIRR(self):
		gp.remove_event_detect(self.pin)

	def __IREvent(self, pin):
		data = gp.input(self.pin)

		if data == 1:
			if self.reading: 
				self.raise_time = time.time()
	
	
		if data == 0:

			fall_time = time.time()
			if not self.reading: 
				if fall_time - self.lastRead > 0.01:
					self.reading = True
				return

			duration = fall_time - self.raise_time
			
			self.bits_durations_list.append(duration)
		
			if len(self.bits_durations_list) == self.total_data_len:
				self.IRReceiverCallback(self.bits_durations_list)
				self.reading = False
				self.bits_durations_list = []
				self.lastRead = fall_time




	def timeToBin(self, durationsList):
		def formatDuration(duration):
			if duration > self.data_diference: return 1
			else: return 0

		return tuple(map(formatDuration, durationsList[self.headers_len:self.headers_len+self.data_len]))
		



if __name__ == '__main__':
	def cb(data):
		data = c.timeToBin(data)
		result = ''
		for i in data: result += str(i)
		print(result)
		
	c = IRReceiver(22, cb)
	c.startIRR()
	input()