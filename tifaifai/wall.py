import sqlite3
import os


def get_all_wall_name():

	values = []
	conn = sqlite3.connect('./data/data.db')
	cursor = conn.execute("SELECT name from WALL")

	for row in cursor:
		values.append(row[0]) 
	conn.close()

	print "Operation done successfully";

	return values
		
def get_first_wall_name():

	values = []
	conn = sqlite3.connect('data.db')
	cursor = conn.execute("SELECT name from WALL")

	for row in cursor:
		values.append(row[0]) 
	conn.close()

	print "Operation done successfully";
	return values[0]	
