from .ui_maps import Ui_Maps_widget
import threading
from GUI_PACKAGES.navigator_google_maps.navegador import Navegador

class Maps_funcs:
	
	def mapSetup(self):
		self.GUI_Maps = Ui_Maps_widget()
		self.GUI_Maps.setupUi(self.GUI_Central.page_maps)

		self.GUI_Maps.navigator = None
		self.GUI_Maps.navThread = None
		
		self.GUI_Maps.mapsTitleCloseButton.clicked.connect(lambda: self.GUI_Maps.stackedWidget.setCurrentIndex(0))

		# Main
		self.GUI_Maps.mapsSelectMapButton.clicked.connect(lambda: Maps_funcs.openNavigator(self))
		self.GUI_Maps.mapsSelectDirectionsButton.clicked.connect(lambda: self.GUI_Maps.stackedWidget.setCurrentIndex(1))
		self.GUI_Maps.mapsSelectHomeButton.clicked.connect(lambda: self.GUI_Maps.stackedWidget.setCurrentIndex(2))

		# Directions
		self.GUI_Maps.mapsDirectionsHomeButton.clicked.connect(lambda: self.GUI_Maps.mapsDirectionFromInput.setText(self.getConfig('home')))
		self.GUI_Maps.mapsDirectionsGoButton.clicked.connect(lambda: Maps_funcs.openNavigator(self, setMap='directions'))

		# Home
		self.GUI_Maps.mapsHomeGoButton.clicked.connect(lambda: Maps_funcs.openNavigator(self, setMap='home'))


	def openNavigator(self, setMap='go'):
		if self.GUI_Maps.navigator: return
		self.GUI_Maps.navigator = Navegador(fullScreen=False)
		if setMap == 'go':
			self.GUI_Maps.navigator.abrir_maps()
		elif setMap == 'directions':
			self.GUI_Maps.navigator.direccion(self.GUI_Maps.mapsDirectionFromInput.text(), self.GUI_Maps.mapsDirectionToInput.text())
		elif setMap == 'home':
			self.GUI_Maps.navigator.direccion(self.GUI_Maps.mapsHomeUbicationInput.text(), self.getConfig('home'))

		Maps_funcs.startController(self)


	def endNavigation(self):
		if not self.GUI_Maps.navigator: return
		self.GUI_Maps.navigator.exit()
		self.GUI_Maps.navigator = None

	def startController(self):
		def controls():
			try:		
				self.GUI_Maps.navigator.iniciar_viaje()

				# Control function
				self.GUI_Maps.navigator.mini_nav()
				# ~~~~~~~~~~~~~~~~
			except:
				Maps_funcs.endNavigation(self)

		self.GUI_Maps.navThread = threading.Thread(controls)
		self.GUI_Maps.navThread.start()
		
