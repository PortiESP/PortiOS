
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
from GUI_PACKAGES.system_info.system_info import System_info
from GUI_PACKAGES.RGB_led.rgb_controller import  RGB_Controller
from GUI_PACKAGES.IRReceiver.IRReceiver import IRReceiver

# Resources import
import resources_rc

# Program imports
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys, threading, time, Adafruit_ADS1x15, dbus.exceptions, os, re
from math import ceil
import RPi.GPIO as gp

