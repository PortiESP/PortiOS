import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback, remoteBits=16):
		self.pin = pin
		self.remoteBits = remoteBits
		self.headerBits = self.remoteBits

		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)

		self.readingData = False
		self.header_count = 0
		self.start_time = None
		self.readingBit = False

		self.bits_durations = []
		
		self.IRReceiverCallback = callback

	def startIRR(self):
		gp.add_event_detect(self.pin, gp.BOTH, callback=self.__IREvent)

	def stopIRR(self):
		gp.remove_event_detect(self.pin)

	def __IREvent(self, pin):


		data = gp.input(self.pin)

		if data == 1:														# Bit start
			if not self.readingData: return

			if self.header_count < self.remoteBits:								 # Headers
				self.header_count += 1
				return 
			else:																 # Data
				self.start_time = time.time()	
				self.readingBit = True

		elif data == 0:														# Bit end
			if not self.readingData: self.readingData = True

			if self.readingBit:
				self.bits_durations.append(time.time() - self.start_time)
				self.readingBit = False
				if len(self.bits_durations) == self.remoteBits:				# Data completed
					self.__formatData(self.bits_durations)
					self.header_count = 0
					self.bits_durations = []
					self.readingData = False



	def __formatData(self, dataList):
		print(dataList)
		def formatDuration(duration):
			if duration > 0.001: return 1
			else: return 0

		finalData = tuple(map(formatDuration, dataList))
		self.IRReceiverCallback(finalData)



