from .ui_maps import Ui_Map_widget
from GUI_PACKAGES.navigator_google_maps.navegador import Navegador

class Maps_funcs:
	
	def mapSetup(self):
		self.GUI_Maps = Ui_Maps_widget()
		self.GUI_Maps.setupUi(self.GUI_Central.page_maps)

		self.GUI_Maps.navigator = None
		self.GUI_Maps.navThread = None

		self.GUI_Maps.mapsSelectMapButton.clicked.connect(Maps_funcs.openNavigator)
		self.GUI_Maps.mapsSelectDirectionsButton.clicked.connect(self.GUI_Maps.stackedWidget.setCurrentIndex(0))
		self.GUI_Maps.mapsSelectHomeButton.clicked.connect(self.GUI_Maps.stackedWidget.setCurrentIndex(1))




	def openNavigator(self):
		if self.GUI_Maps.navigator: return
		print('Starting maps')
		self.GUI_Maps.navigator = Navegador()
		self.GUI_Maps.navigator.abrir_maps()
		Maps_funcs.startController()


	def endNavigation(self):
		if not self.GUI_Maps.navigator: return
		print('Ending maps')
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
		
