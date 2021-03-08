import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback):
		self.pin = pin
		self.IRReceiverCallback = callback

		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)

		# Program vars
		self.lastRead = 0        
		self.reading = False
		self.raise_time = 0
		self.bits_durations_list = []


	def startIRR(self):
		gp.add_event_detect(self.pin, gp.BOTH, callback=self.__IREvent)

	def stopIRR(self):
		gp.remove_event_detect(self.pin)

	def __IREvent(self, pin):
		data = gp.input(self.pin)

		if data:
			if self.reading: 
				self.raise_time = time.time()
	
	
		else:

			fall_time = time.time()
			if not self.reading: 
				if fall_time - self.lastRead > 0.1:
					self.reading = True
				return
			duration = fall_time - self.raise_time
			if duration < 0.0019:
				self.bits_durations_list.append(duration)
		
			if len(self.bits_durations_list) == 32:
				self.IRReceiverCallback(self.__timeToBin(self.bits_durations_list))
				self.reading = False
				self.bits_durations_list = []
				self.lastRead = fall_time




	def __timeToBin(self, durationsList):
		def formatDuration(duration):
			if duration > 0.001: return 1
			else: return 0

		result = ''
		for i in tuple(map(formatDuration, durationsList[16:])): result += str(i)
		return result








