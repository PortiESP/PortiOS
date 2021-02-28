from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class Navegador:
	def __init__(self):
		# Setting chrome
		self.chrome_options = Options()
		self.chrome_options.add_argument("--kiosk")
		self.chrome_options.add_experimental_option("useAutomationExtension", False)
		self.chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
		self.driver = webdriver.Chrome(options=self.chrome_options)
		# Declarating variables
		self.instruccion_index = 0
		self.instrucciones_viaje = []
		self.instrucciones_titles = []
		self.cookie_accepted = False

		# Declarating and incializating variables
		self.groups_class_name = 'directions-mode-group'
		self.instructions_class_name = 'directions-mode-step-container'
		self.instructionsTitle_class_name = 'numbered-step-content'
		self.selectedItemStyles =  {'background' : 'rgb(200,200,200)',
									'border' : '5px solid #4285F4'}
		self.resetItemStyles =  {'background' : 'none',
									'border' : 'none'}


		# Starting maps on chrome
		self.driver.get('https://www.google.es/maps/dir/')

		# Get window sizes
		self.windowHeight = self.driver.get_window_size()['height']
		# Accept Gmaps cookies
		if not self.cookie_accepted:
			if self.__aceptar_privacidad(): self.cookie_accepted = True


	# SETTING UP
	def __aceptar_privacidad(self):
		wh = self.driver.current_window_handle
		WebDriverWait(self.driver, 20).until(lambda x: self.driver.find_element_by_tag_name('iframe'))
		caja_privacidad = self.driver.find_element_by_tag_name('iframe')
		self.driver.switch_to.frame(caja_privacidad)
		self.driver.find_element_by_id('introAgreeButton').click()
		self.driver.switch_to.window(wh)

	def __obtener_instrucciones(self):
		time.sleep(0.5)
		WebDriverWait(self.driver, 120).until(lambda x: self.driver.find_elements_by_class_name('directions-mode-group'))
		self.bloques_direcciones = self.driver.find_elements_by_class_name(self.groups_class_name)
		self.instrucciones_viaje = self.driver.find_elements_by_class_name(self.instructions_class_name)
		self.instrucciones_titles = self.driver.find_elements_by_class_name(self.instructionsTitle_class_name)

		print('****************** Instructions list ******************')
		for i in self.instrucciones_viaje:
			print(i)
		print('*******************************************************')


	# STARTING
	def direccion(self, origen, destino):
		origen = origen.replace(' ','+')
		destino = destino.replace(' ','+')
		url_map = 'https://www.google.es/maps/dir/'+origen+'/'+destino
		self.driver.get(url_map)

	def iniciar_viaje(self):

		self.__obtener_instrucciones()
		self.instruccion_index = 0
		for bloque in self.bloques_direcciones:
			bloque.click()
			time.sleep(0.1)
		time.sleep(0.1)
		self.select_instruccion(0)
		self.scroll(-500)


		
	# CONTROL
	def siguiente_instruccion(self):
		if self.instruccion_index < len(self.instrucciones_viaje)-1:
			self.__style(self.resetItemStyles)
			self.instruccion_index += 1
			self.__style(self.selectedItemStyles)
			self.actual_point =  self.instrucciones_viaje[self.instruccion_index]
			self.actual_point.click()
			if self.actual_point.location['y'] > (self.windowHeight - self.actual_point.size['height'] - 20):
				print(self.actual_point.location['y'])
				print((self.windowHeight - self.actual_point.size['height']- 30))
				self.scroll(self.actual_point.size['height'] - 20)	
		
	def anterior_instruccion(self):
		if self.instruccion_index > 0:
			self.__style(self.resetItemStyles)
			self.instruccion_index -= 1
			self.__style(self.selectedItemStyles)
			self.actual_point = self.instrucciones_viaje[self.instruccion_index]
			self.actual_point.click()
			

	def select_instruccion(self, index):
		self.__style(self.resetItemStyles)
		self.instruccion_index = index
		self.__style(self.selectedItemStyles)
		self.actual_point = self.instrucciones_viaje[self.instruccion_index]
		self.actual_point.click()

	def toggle_map(self):
		self.instrucciones_titles[self.instruccion_index].click()		

	# VISUAL
	def zoom_in(self):
		self.driver.find_element_by_id('widget-zoom-in').click()

	def zoom_out(self):
		self.driver.find_element_by_id('widget-zoom-out').click()		

	def scroll(self, value):
		self.driver.execute_script(f'document.evaluate("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollBy(0,{value})')

	def __style(self, sty):
		for key, value in sty.items():
			self.driver.execute_script(f"item = document.getElementsByClassName('{self.instructions_class_name}')[{self.instruccion_index}]; item.style.background = '{sty['background']}'; item.style.borderRight = '{sty['border']}';  ")
	

	# TESTINGS
	def select_instrucciones(self):
		for i in self.instrucciones_viaje:
			self.siguiente_instruccion()
			time.sleep(4)

	def mini_nav(self):
		while 1:
			q = input('--> ')
			if q == 'next': self.siguiente_instruccion()
			elif q == 'prev': self.anterior_instruccion()
			elif q == 'toggle': self.toggle_map()
			elif q == '+': self.zoom_in()
			elif q == '-': self.zoom_out()
			elif q[0] == 's': self.scroll(int(q[2:]))

			elif q == 'exit': self.exit()


	# EXIT
	def exit(self):
		self.driver.quit()






if __name__ == '__main__':
	# nav = Navegador()
	# nav.direccion('Boadilla del monte', 'Madrid')
	
	# nav.iniciar_viaje()
	# nav.pruebas()
	# nav.select_instrucciones()
	# nav.mini_nav()
	pass

