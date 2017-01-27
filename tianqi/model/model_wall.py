#!/usr/bin/python
import sqlite3

def get_all_wall_name():
	
	walls = []
	conn = sqlite3.connect('data.db')
	cursor = conn.execute("SELECT name from WALL")

	for row in cursor:
	   walls.append(row[0]) 
	   
	conn.close()
	return walls
   


liste = get_all_wall_name()

for x in liste: print x

print "Opened database successfully";\

