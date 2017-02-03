from kivy.uix.boxlayout import BoxLayout
import sqlite3

class Wall(BoxLayout):
    def build(self, wall_name):
        self.wall_name = wall_name

    def save(self,conn):
        conn.execute("INSERT INTO WALL (NAME) VALUES ("+self.wall_name+")")


class Scenary(BoxLayout):
    def build(self, wall_id, scenary_name):
        self.wall_id = wall_id
        self.scenary_name = scenary_name

    def save(self, conn):
        conn.execute("INSERT INTO SCENARIO (WALL_ID,NAME) VALUES ("+self.wall_id+", "+self.scenary_name+")")


class Screen(BoxLayout):
    def build(self, displayed, height, width):
        self.displayed = displayed
        self.height = height
        self.width = width

    def save(self, conn):
        conn.execute("INSERT INTO SCREEN (DISPLAYED_SIZE,HEIGHT,WIDTH) VALUES ('"+str(self.displayed)+"', '"+str(self.height)+"', '"+str(self.width)+"')")

    @staticmethod
    def display_all(conn):
        conn.execute("SELECT * FROM SCREEN")