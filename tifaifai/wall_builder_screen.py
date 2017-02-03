from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
import sqlite3
import os

conn = sqlite3


class Wall(BoxLayout):
    def build(self, wall_name):
        self.wall_name = wall_name

    def save(self):
        global conn
        conn.execute("INSERT INTO WALL (NAME) VALUES ("+self.wall_name+")")
        conn.commit()


class Scenary(BoxLayout):
    def build(self, wall_id, scenary_name):
        self.wall_id = wall_id
        self.scenary_name = scenary_name

    def save(self):
        global conn
        conn.execute("INSERT INTO SCENARIO (WALL_ID,NAME) VALUES ("+self.wall_id+", "+self.scenary_name+")")
        conn.commit()


class Screen(BoxLayout):
    def build(self, displayed, height, width):
        self.displayed = displayed
        self.height = int(height)
        self.width = int(width)

    def save(self):
        global conn
        conn.execute("INSERT INTO SCREEN (DISPLAYED_SIZE,HEIGHT,WIDTH) VALUES ('"+str(self.displayed)+"', '"+str(self.height)+"', '"+str(self.width)+"')")
        conn.commit() # je t'aime commit <3


def display_all():
    global conn
    cursor = conn.execute("SELECT * FROM SCREEN")
    for ligne in cursor:
        print(ligne)


def save_screen(displayed, height, width):
    global conn
    screen = Screen()
    screen.build(displayed, height, width)
    screen.save()


########################################################

def get_all_screen_name():
    values = []
    conn = sqlite3.connect( 'data.db' )
    cursor = conn.execute( "SELECT DISPLAYED_SIZE FROM SCREEN" )

    for row in cursor:
        values.append(row[0])
    conn.close( )
    print ("Operation done successfully")
    return values


def get_first_screen_name():
    values = []
    conn = sqlite3.connect( 'data.db' )
    cursor = conn.execute( "SELECT DISPLAYED_SIZE FROM SCREEN" )

    for row in cursor:
        values.append( row[0] )
    conn.close( )
    print ("Operation done successfully")
    return values[0]

########################################################


def openDB():
    global conn
    conn = sqlite3.connect( 'data.db' )
    print "Opened database successfully"

def closeDB():
    global conn
    conn.close()
    print "Closing database successfully"

def startDB():
    os.system('python tifaifai/data/sql.py')