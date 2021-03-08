import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback):
		self.pin = pin

		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)

		self.lastRead = 0


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
		
			if len(self.bits_durations_list) == 32:
				data = self.__timeToBin(self.bits_durations_list[16:])
				self.IRReceiverCallback(data)
				self.reading = False
				self.bits_durations_list = []
				self.lastRead = fall_time




	def __timeToBin(self, durationsList):
		def formatDuration(duration):
			if duration > 0.001: return 1
			else: return 0

		return tuple(map(formatDuration, durationsList))
		



if __name__ == '__main__':
	def cb(data):
		result = ''
		for i in data: result += str(i)
		print(hex(int(result)))
		
	c = IRReceiver(22, cb)
	c.startIRR()
	input()