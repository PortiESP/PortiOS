# Import GUI Classes
from GUI_WIDGETS.Central.ui_central import Ui_Central
from GUI_WIDGETS.Apps_menu.ui_apps_menu import Ui_Apps_widget
from GUI_WIDGETS.Dashboard.ui_dashboard import Ui_Dashboard_widget
from GUI_WIDGETS.Leds.ui_leds import Ui_Leds_widget
from GUI_WIDGETS.Media_player.ui_design_player import Ui_Player_widget
from GUI_WIDGETS.Settings.ui_design_settings import Ui_Settings_widget

# Import GUI functions
from GUI_WIDGETS.Central.central_functions import Central_funcs
from GUI_WIDGETS.Apps_menu.apps_functions import Apps_funcs 
from GUI_WIDGETS.Settings.settings_functions import Settings_funcs 
from GUI_WIDGETS.Dashboard.dashboard_functions import Dashboard_funcs
from GUI_WIDGETS.Media_player.player_functions import Player_funcs

# Import controllers packages
from GUI_PACKAGES.bluetooth_controls.bt_control_panel import BT_Control_Panel

# Resources import
import resources_rc

# Program imports
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys, threading, time


