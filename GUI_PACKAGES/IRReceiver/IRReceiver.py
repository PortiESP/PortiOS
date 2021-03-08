import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback):
		self.pin = pin
		self.IRReceiverCallback = callback

		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)


		# --- Parameters ----------------------------------------+
		self.total_bits = 32 			# Remote controll format |
		self.bool_limit = 0.001 		# Limit between 0 & 1    |
		self.header_len = 16			# Nº of bit in header    |
		self.bit_max_duration = 0.0019  # Maximum value for bit  |
		self.bounce = 0.01				# Anti-bounce time 		 |
		self.read_on = 1				# Inverse logic
		# -------------------------------------------------------+

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

		if data == self.read_on:
			if self.reading: 
				self.raise_time = time.time()
	
	
		if data != self.read_on:

			fall_time = time.time()
			if not self.reading: 
				if fall_time - self.lastRead > self.bounce:
					self.reading = True
				else:
					self.lastRead = fall_time
				return
			duration = fall_time - self.raise_time
			if duration < self.bit_max_duration:
				self.bits_durations_list.append(duration)
		
			if len(self.bits_durations_list) == self.total_bits:
				self.IRReceiverCallback(self.bits_durations_list)
				self.reading = False
				self.bits_durations_list = []
				self.lastRead = fall_time




	def timeToBinList(self, durationsList):
		def formatDuration(duration):
			if duration > self.bool_limit: return 1
			else: return 0

		return tuple(map(formatDuration, durationsList[self.header_len:]))

	def binListToBinStr(self, binList):
		result = ''
		for i in binList: result += str(i)
		return result

	def timeToBinStr(self, durationsList):
		return self.binListToBinStr(self.timeToBinList(durationsList))




if __name__ == '__main__':
	def cb(data):
		data = c.timeToBinStr(data)
		print(data)
		
	c = IRReceiver(22, cb)
	c.startIRR()
	input()
