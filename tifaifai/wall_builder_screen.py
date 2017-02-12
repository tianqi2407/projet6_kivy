from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
import random
import sqlite3
import os

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

conn = sqlite3.connect( './data/data.db' )

############################### Classes ###############################
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
    global conn
    cursor = conn.execute( "SELECT DISPLAYED_SIZE FROM SCREEN" )

    if not cursor:
        values = ''
    else:
        for row in cursor:
            values.append( row[0] )
        print ("Operation done successfully")
    return values


def get_first_screen_name():
    values = []
    global conn
    cursor = conn.execute( "SELECT DISPLAYED_SIZE FROM SCREEN" )

    if not cursor:
        values = ''
    else :
        for row in cursor:
            values.append( row[0] )
        print ("Operation done successfully")
    return values[0]


def get_height(name):
    global conn
    chaine = []
    cursor = conn.execute("SELECT height FROM SCREEN WHERE DISPLAYED_SIZE = '"+ name +"'")
    if not cursor:
        chaine = name
    else:
        for row in cursor:
            chaine.append(row[0])
    return str(chaine[0])


def get_width(name):
    global conn
    chaine = []
    cursor = conn.execute("SELECT width FROM SCREEN WHERE DISPLAYED_SIZE = '"+ name +"'")
    if not cursor:
        chaine = name
    else:
        for row in cursor:
            chaine.append(row[0])
    return str(chaine[0])


def delete_screen(name):
    global conn
    conn.execute("DELETE FROM SCREEN WHERE DISPLAYED_SIZE = '"+ name +"'")
    conn.commit()


def display_screen(self, name):
    global conn
    chaine = []
    cursor = conn.execute("SELECT height FROM SCREEN WHERE DISPLAYED_SIZE = '"+ name +"'")
    if not cursor:
        chaine = name
    else:
        for row in cursor:
            chaine.append(row[0])

    x = int(self.ids.ici.x + (random.randint(150, int(self.ids.ici.size[0] - 1)) - 150 ))
    y = int(self.ids.ici.y + (random.randint(100, int(self.ids.ici.size[1] - 1)) - 100 ))

    text = Label(text=str(chaine[0])).texture
    with self.canvas:
        Color(.5,.5,.5)
        Rectangle(size=(150.,100.), pos=(x, y), texture= text)


########################################################


def get_all_wall_name():
    values = []
    global conn
    cursor = conn.execute( "SELECT name from WALL" )

    for row in cursor:
        values.append( row[0] )
    conn.close( )
    print ("Operation done successfully")
    return values

def get_first_wall_name():
    values = []
    global conn
    cursor = conn.execute( "SELECT name from WALL" )

    for row in cursor:
        values.append( row[0] )
    conn.close( )
    print ("Operation done successfully")
    return values[0]

########################################################

def openDB():
    global conn
    print "Opened database successfully"

def closeDB():
    global conn
    conn.close()
    print "Closing database successfully"

def startDB():
    os.system('python ./data/sql.py')