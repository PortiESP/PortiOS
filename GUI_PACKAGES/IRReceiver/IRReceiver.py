import RPi.GPIO as gp
import threading, time

class IRReceiver:
	def __init__(self, pin, callback, remoteBits=16):
		self.pin = pin
		self.remoteBits = remoteBits
		self.headerBits = self.remoteBits

		gp.setmode(gp.BOARD)
		gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)

		self.reading = False
		self.bit_start = 0

		self.bits_durations_list = []

		self.IRReceiverCallback = callback

	def startIRR(self):
		gp.add_event_detect(self.pin, gp.BOTH, callback=self.__IREvent)

	def stopIRR(self):
		gp.remove_event_detect(self.pin)

	def __IREvent(self, pin):

		data = gp.input(self.pin)

		if data == 1:
			self.reading = True
			self.bit_start = time.time()

		if data == 0:
			duration = time.time() - self.bit_start
			if duration < 0.005:
				self.bits_durations_list.append(duration)
			if len(self.bits_durations_list) == 32:
				self.IRReceiverCallback(self.bits_durations_list)




	def __formatData(self, dataList):
		print(dataList)
		def formatDuration(duration):
			if duration > 0.001: return 1
			else: return 0

		finalData = tuple(map(formatDuration, dataList))
		self.IRReceiverCallback(finalData)



if __name__ == '__main__':
	def cb(data):
		print(data)
	c = IRReceiver(22, cb)
	c.startIRR()
	input()