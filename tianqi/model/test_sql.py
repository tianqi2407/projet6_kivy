#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('data.db')

print "Opened database successfully";

#EXAMPLE DE CREATION
cursor1 = conn.execute("INSERT INTO SCREEN (DISPLAYED_SIZE,HEIGHT,WIDTH) VALUES ('size_screen_example','60cm','60cm')");
screen_id = cursor1.lastrowid
print screen_id
conn.execute("INSERT INTO WALL (NAME) VALUES ('WALL1' )");
cursor2 = conn.execute("INSERT INTO WALL (NAME) VALUES ('WALL2' )");
wall_id = cursor2.lastrowid
print wall_id
	  
	  
conn.execute("INSERT INTO WALL_HAS_SCREEN (SCREEN_ID,WALL_ID,POSITION) VALUES (?,?,1 )",(screen_id,wall_id));

conn.commit()
print "Records created successfully";

cursor = conn.execute("SELECT id, name  from WALL")

for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1], "\n"

cursor3 = conn.execute("SELECT SCREEN_ID, WALL_ID, POSITION  from WALL_HAS_SCREEN")  

for row in cursor3:
   print "SCREEN_ID = ", row[0]
   print "WALL_ID = ", row[1]
   print "POSITION = ", row[2], "\n"
   
print "Operation done successfully";

conn.close()

