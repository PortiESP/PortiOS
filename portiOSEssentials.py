
# Import GUI functions
from GUI_WIDGETS.Central.central_functions import Central_funcs
from GUI_WIDGETS.Apps_menu.apps_functions import Apps_funcs 
from GUI_WIDGETS.Settings.settings_functions import Settings_funcs 
from GUI_WIDGETS.Dashboard.dashboard_functions import Dashboard_funcs
from GUI_WIDGETS.Media_player.player_functions import Player_funcs
from GUI_WIDGETS.Leds.leds_functions import Leds_funcs

# Import controllers packages
from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel
from GUI_PACKAGES.navigator_google_maps.navegador import Navegador

# Resources import
import resources_rc

# Program imports
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys, threading, time
from math import ceil
from dbus.exceptions import *


