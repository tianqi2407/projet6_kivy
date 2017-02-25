# coding=utf-8
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random
import sqlite3
import os

conn = sqlite3.connect('./data/data.db')
wall = None


############################### Classes ###############################
class Wall(BoxLayout):
	def __init__(self, wall_name, **kwargs):
		super(Wall, self).__init__(**kwargs)
		self.wall_name = wall_name
		self.screenList = []

	def save(self):
		global conn
		conn.execute("INSERT INTO WALL (NAME) VALUES ('" + self.wall_name + "')")
		conn.commit()

	def disableButton(self, bouton):
		i = 0
		for b in self.screenList:
			if b.text == bouton.text and b.pos == bouton.pos:
				print b.text
				print b.pos
				self.remove_widget(self.screenList[i])
			i += 1

	def addScreen(self, bouton, name):
		self.screenList.append(name)
		for screen in self.screenList:
			print(screen)
		bouton.bind(on_press=self.disableButton)


class Scenary(BoxLayout):
	def build(self, wall_id, scenary_name):
		self.wall_id = wall_id
		self.scenary_name = scenary_name

	def save(self):
		global conn
		conn.execute("INSERT INTO SCENARIO (WALL_ID,NAME) VALUES (" + self.wall_id + ", " + self.scenary_name + ")")
		conn.commit()


class Screen(BoxLayout):
	def build(self, displayed, height, width):
		self.displayed = displayed
		self.height = int(height)
		self.width = int(width)

	def save(self):
		global conn
		conn.execute("INSERT INTO SCREEN (DISPLAYED_SIZE,HEIGHT,WIDTH) VALUES ('" + str(self.displayed) + "', '" + str(
			self.height) + "', '" + str(self.width) + "')")
		conn.commit()  # je t'aime commit <3


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
	cursor = conn.execute("SELECT DISPLAYED_SIZE FROM SCREEN")

	if not cursor:
		values = ''
	else:
		for row in cursor:
			values.append(row[0])
		print ("Operation done successfully")
	return values


def get_first_screen_name():
	values = []
	global conn
	cursor = conn.execute("SELECT DISPLAYED_SIZE FROM SCREEN")

	if not cursor:
		values = ''
	else:
		for row in cursor:
			values.append(row[0])
		print ("Operation done successfully")
	return values[0]


def get_height(name):
	global conn
	chaine = []
	cursor = conn.execute("SELECT height FROM SCREEN WHERE DISPLAYED_SIZE = '" + name + "'")
	if not cursor:
		chaine = name
	else:
		for row in cursor:
			chaine.append(row[0])
	return str(chaine[0])


def get_width(name):
	global conn
	chaine = []
	cursor = conn.execute("SELECT width FROM SCREEN WHERE DISPLAYED_SIZE = '" + name + "'")
	if not cursor:
		chaine = name
	else:
		for row in cursor:
			chaine.append(row[0])
	return str(chaine[0])


def delete_screen(name):
	global conn
	conn.execute("DELETE FROM SCREEN WHERE DISPLAYED_SIZE = '" + name + "'")
	conn.commit()


def display_screen(self, name):
	global conn
	global wall
	chaine = []
	cursor = conn.execute("SELECT height FROM SCREEN WHERE DISPLAYED_SIZE = '" + name + "'")
	if not cursor:
		chaine = name
	else:
		for row in cursor:
			chaine.append(row[0])

	x = int(self.ids.ici.x + (random.randint(150, int(self.ids.ici.size[0] - 1)) - 150))
	y = int(self.ids.ici.y + (random.randint(100, int(self.ids.ici.size[1] - 1)) - 100))

	btn = Button(id=name, text=name, width=150, size_hint=(None, 0.20), pos=(x, y))
	self.ids.ici.add_widget(btn)
	#wall.addScreen(btn)
	wall.addScreen(btn,name)
	
def display_screen_wall(self, name):
	global conn
	global wall
	chaine = []
	cursor = conn.execute("SELECT height FROM SCREEN WHERE DISPLAYED_SIZE = '" + name + "'")
	if not cursor:
		chaine = name
	else:
		for row in cursor:
			chaine.append(row[0])

	x = int(self.ids.ici.x + (random.randint(150, int(self.ids.ici.size[0] - 1)) - 150))
	y = int(self.ids.ici.y + (random.randint(100, int(self.ids.ici.size[1] - 1)) - 100))

	btn = Button(id=name, text=name, width=150, size_hint=(None, 0.20), pos=(x, y))
	self.ids.ici.add_widget(btn)
########################################################


def get_all_wall_name():
	values = []
	global conn
	cursor = conn.execute("SELECT name from WALL")

	for row in cursor:
		values.append(row[0])
	conn.close()
	print ("Operation done successfully")
	return values


def get_first_wall_name():
	values = []
	global conn
	cursor = conn.execute("SELECT name from WALL")

	for row in cursor:
		values.append(row[0])
	conn.close()
	print ("Operation done successfully")
	return values[0]


def newWall(name):
	global wall
	global conn
	wall = Wall(name)
	conn.execute("INSERT INTO WALL (NAME) VALUES ('" + name + "')")
	conn.commit()
	print name
	


#def save_wall(self):
	#print "validation"
	#avec = False
	#if wall.screenList != []:
		#avec = True
	#wall.save(avec)
	
def save_screen_list(self):
	save_screens_with_wall(wall)

def save_screens_with_wall(wall):
	print "validation save_screen_with_wall"
	for screen in wall.screenList:
		print(screen)
	global conn
	if wall.wall_name != None:
		cursor = conn.execute("SELECT ID FROM WALL WHERE NAME = '" + wall.wall_name + "'")
		if cursor != None:
			for row in cursor:
				wall_id = row[0]
				print wall.wall_name
				print wall_id
	position = 0
	if wall.screenList != []:
		for screen in wall.screenList:
			cursor = conn.execute("SELECT ID FROM SCREEN WHERE DISPLAYED_SIZE = '" + screen + "'")
			if cursor != None:
				for row in cursor:
					screen_id = row[0]
					print screen_id
					comm = "INSERT INTO WALL_HAS_SCREEN (SCREEN_ID,WALL_ID,POSITION) VALUES (" + str(screen_id) + ", " + str(wall_id) +  ", " + str(position) + ")"
					print comm
					cursor = conn.execute(comm)
					conn.commit()
				position += 1
				
def getWallName(name):
	global wall
	global conn
	wall = Wall(name)
	
	
def getScreensByWall():
	global conn
	if wall.wall_name != None:
		cursor = conn.execute("SELECT ID FROM WALL WHERE NAME = '" + wall.wall_name + "'")
		if cursor != None:
			for row in cursor:
				wall_id = row[0]
				print wall.wall_name
				print wall_id
				comm = "SELECT SCREEN_ID,POSITION FROM WALL_HAS_SCREEN WHERE WALL_ID = " + str(wall_id)
				print comm
				cursor = conn.execute(comm)
				if cursor != None:
					for row in cursor:
						screen_id = row[0]
						position = row[1]
						print screen_id
						print position
						if screen_id != None:
							cursor2 = conn.execute("SELECT DISPLAYED_SIZE FROM SCREEN WHERE ID =  " + str(screen_id))
							if cursor2 != None:
								for row in cursor2:
									print row[0]
									wall.screenList.insert(position,row[0])
						print "les ecrans avec " + wall.wall_name
						for screen in wall.screenList:
							print(screen)
########################################################

def setScreens(self):
	if wall.screenList != []:
		for screen in wall.screenList:
			display_screen_wall(self, screen)
	
def openDB():
	global conn
	print "Opened database successfully"


def closeDB():
	global conn
	conn.close()
	print "Closing database successfully"


def startDB():
	os.system('python ./data/sql.py')
