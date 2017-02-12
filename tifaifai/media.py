import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import os

def selected(filename):
	print "selected: %s" % filename[0]

