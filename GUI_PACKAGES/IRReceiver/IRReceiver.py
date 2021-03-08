import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback):
		self.pin = pin

		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)

		self.lastRead = 0
		self.total_bits = 32
		self.bool_limit = 0.001
		self.header_len = 16

		self.reading = False
		self.raise_time = 0
		self.bits_durations_list = []

		self.IRReceiverCallback = callback

	def startIRR(self):
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
				self.bits_durations_list = []
				return
			duration = fall_time - self.raise_time
			if duration < 0.0019:
				self.bits_durations_list.append(duration)
		
			if len(self.bits_durations_list) == self.total_bits:
				self.IRReceiverCallback(self.bits_durations_list)
				self.reading = False
				self.bits_durations_list = []
				self.lastRead = fall_time




	def timeToBin(self, durationsList):
		def formatDuration(duration):
			if duration > self.bool_limit: return 1
			else: return 0

		return tuple(map(formatDuration, durationsList[self.header_len:]))
		



if __name__ == '__main__':
	def cb(data):
		data = c.timeToBin(data)
		result = ''
		for i in data: result += str(i)
		print(result)
		
	c = IRReceiver(22, cb)
	c.startIRR()
	input()
