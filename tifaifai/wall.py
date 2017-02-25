# coding=utf-8
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random
import sqlite3
import os

def get_all_wall_name():

	values = []
	conn = sqlite3.connect('./data/data.db')
	cursor = conn.execute("SELECT name FROM WALL")

	if not cursor:
		values = ''
	else:
		for row in cursor:
			values.append(row[0])
		print "Operation done successfully";

	conn.close()

	return values
		
def get_first_wall_name():

	values = []
	conn = sqlite3.connect('./data/data.db')
	cursor = conn.execute("SELECT name from WALL")

	if not cursor:
		values = ''
	else :
		for row in cursor:
			values.append( row[0] )
		print ("Operation done successfully")
	conn.close()
	return values[0]
