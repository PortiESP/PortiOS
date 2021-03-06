import RPi.GPIO as gp
import time, threading


class RGB_Controller:
	def __init__(self, rgb_pins):
		self.red_pin = rgb_pins[0]
		self.green_pin = rgb_pins[1]
		self.blue_pin = rgb_pins[2]
		
		gp.setmode(gp.BOARD)
		gp.setwarnings(False)
		gp.setup(self.red_pin, gp.OUT)
		gp.setup(self.green_pin, gp.OUT)
		gp.setup(self.blue_pin, gp.OUT)
		
		freq = 50
		
		self.RED = gp.PWM(self.red_pin, freq)
		self.GREEN = gp.PWM(self.green_pin, freq)
		self.BLUE = gp.PWM(self.blue_pin, freq)
		self.RED.start(0)
		self.GREEN.start(0)
		self.BLUE.start(0)
		
		self.loop_thread = None
		
		# ~ PROGRAMAS
		self.RAINBOW = [(i,j,k) for i in (0,255) for j in (0,255) for k in (0,255) if (i,j,k) != (0,0,0) and (i,j,k) != (255,255,255)]
		self.RAINBOW.append((255, 69, 0))
		self.POLICE = ((255,0,0), (0,0,255))
		self.FLASH = ((255,255,255),(0,0,0))
		self.FIRE = ((255,50,0),(229,70,0), (247,20,0))
		
	def new_thread(self, thread_target, thread_args):
		self.loop_thread = threading.Thread(target=thread_target, args=thread_args)
		self.loop_thread.start()
		return self.loop_thread
		
		
	def set_color(self, rgb):
		self.RED.ChangeDutyCycle(rgb[0]/255*100)
		self.GREEN.ChangeDutyCycle(rgb[1]/255*100)
		self.BLUE.ChangeDutyCycle(rgb[2]/255*100)
	
	def set_white(self):
		gp.output(sel.red_pin, 1)
		gp.output(sel.green_pin, 1)
		gp.output(sel.blue_pin, 1)
		
	def set_off(self):
		if self.loop_thread: self.loop_thread.join()
		self.set_color((0,0,0))
		
	def __color_jump(self, colors, hz):
		period = 1/hz
		color_time = period / len(colors)
		while self.loop_thread:
			for color in colors:
				# ~ print(f'Color: {color}')
				self.set_color(color)
				time.sleep(color_time)
				
	def __color_fade(self, colors, hz, method='normal'):
		if method == 'floor-red':
			colors = list(colors)
			for i in range(len(colors)):
				colors.insert(1+i*2, (0,0,0))
		
		period = 1/hz
		color_time = period / len(colors)
		n = len(colors)
		while self.loop_thread:
			for i in range(len(colors)):
				color = list(colors[i])
				if n-1 != i:nextcolor = colors[i+1]
				else: nextcolor = colors[0]
				nextcolor = list(nextcolor)
				iter_max = 0
				for c in range(3):
					x = abs(color[c] - nextcolor[c])
					if x > iter_max: iter_max = x
					
				
				while color != nextcolor:
					if method == 'normal':
						self.set_color(color)
						for c in range(3):
							# ~ print(f'Color: {color}, Next: {nextcolor}')
							if color[c] < nextcolor[c]: color[c] += 1
							elif color[c] > nextcolor[c]: color[c] -= 1
						time.sleep(color_time/iter_max)
					elif method == 'chromatic':
						#Algoritmo que ordena de mayor a menor los numeros y pasa su indice
						def algoritmo_colores(color):
							color_ord = list(color)
							color_ord.sort()
							color_ord.reverse()
							color_ord = [color.index(c) for c in color_ord]
							if len(set(color_ord)) == 1: color_ord = (0,1,2)
							if len(set(color_ord)) == 2:
								doble = [i for i in (0,1,2) if color_ord.count(i) == 2][0]
								miss = [i for i in (0,1,2) if color_ord.count(i) == 0][0]
								color_ord[color_ord.index(doble)] = miss			
								
							return color_ord
														
							
						color_ord = algoritmo_colores(color)
						for c in color_ord:
							while color[c] != nextcolor[c]:
								if color[c] < nextcolor[c]: color[c] += 1
								elif color[c] > nextcolor[c]: color[c] -= 1
								self.set_color(color)
								# print(f'Color: {color}, Next: {nextcolor}, Algoritmo: {color_ord}')
								time.sleep(color_time/iter_max/3)
						time.sleep(0.5)
					elif method == 'floor-red':
						self.set_color(color)
						for c in range(3):
							# print(f'Color: {color}, Next: {nextcolor}')
							if c != 0 and color[0] != nextcolor[0] and nextcolor[0] != 0: continue
							if color[c] > nextcolor[c]: color[c] -= 1
							elif color[c] < nextcolor[c]: color[c] += 1
						time.sleep(color_time/iter_max)
						if color == nextcolor and color != [0,0,0]: time.sleep(1)
						
					
				
		
	#Method parameter only for fade mode
	def set_program(self, program=None, hz=1, mode='jump', method=None):
		self.loop_thread = False
		if mode == 'jump':
			self.loop_thread = self.new_thread(self.__color_jump, (program, hz))
		elif mode == 'fade':
			if method:
				self.loop_thread = self.new_thread(self.__color_fade, (program, hz, method))
			else:
				self.loop_thread = self.new_thread(self.__color_fade, (program, hz))
		elif mode == 'random-jump':
			self.loop_thread = self.new_thread(self.__color_jump, (self.RAINBOW, hz))
		elif mode == 'random-fade':
			self.loop_thread = self.new_thread(self.__color_fade, (self.RAINBOW, hz, 'chromatic'))
		else:
			raise ValueError ('Inserte un modo valido')
	
		return self.loop_thread
		
		
			
	def program_stop(self, program='self'):
		if program == 'self': program = self.loop_thread
		program.join()
		self.loop_thread = None
		self.set_off()



# ~ if __name__ == '__main__':
	# ~ ct = RGB_Controller((40,38,36))
	# ~ ct.set_color((50,255, 100))
	# ~ ct.set_white()
	# ~ program = ct.set_program(program=((255,0,0),(0,255,0),(0,0,255)), hz=1, mode='fade')
	# ~ program = ct.set_program(program=ct.FIRE, hz=0.05, mode='fade', method='floor-red')
	# ~ while 1:
		# ~ if input() == 'q':
			# ~ ct.program_stop()
			# ~ break




	# ~ input('END')
	# ~ ct.set_off()
	
