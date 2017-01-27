# -*- coding: utf-8 -*-
'''
Container Example
==============

This example shows how to add a container to our screen.
A container is simply an empty place on the screen which
could be filled with any other content from a .kv file.
'''
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import sqlite3


import os
import kivy
kivy.require('1.8.0')
from kivy.core.window import Window

Window.size = (1120, 630)


class Wall(BoxLayout):
    def build(self, wall_name):
        self.wall_name = wall_name

    def save(self):
        conn.execute("INSERT INTO WALL (NAME) VALUES ("+self.wall_name+")")


class Scenary(BoxLayout):
    def build(self, wall_id, scenary_name):
        self.wall_id = wall_id
        self.scenary_name = scenary_name

    def save(self):
        conn.execute("INSERT INTO SCENARIO (WALL_ID,NAME) VALUES ("+self.wall_id+", "+self.scenary_name+")")


class Screen(BoxLayout):
    def build(self, displayed, height, width):
        self.displayed = displayed
        self.height = height
        self.width = width

    def save(self):
        conn.execute("INSERT INTO SCREEN (DISPLAYED_SIZE,HEIGHT,WIDTH) VALUES ("+self.displayed+", "+self.height+", "+self.width+")")


class RootWidget(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''

    container = ObjectProperty(None)


def save_screen(displayed, height, width):
    screen = Screen()
    screen.build(displayed, height, width)
    screen.save()


class MainApp(App):

    '''This is the app itself'''

    def build(self):
        '''This method loads the root.kv file automatically

        :rtype: none
        '''
        # loading the content of root.kv
        
        self.root = Builder.load_file('kv/root.kv')
        Builder.load_file('kv/wall_builder_screen.kv')
        Builder.load_file('kv/screen_builder_screen.kv')
        Builder.load_file('kv/media.kv')
        Builder.load_file('kv/add_media.kv')

    def next_screen(self, screen):
        '''Clear container and load the given screen object from file in kv
        folder.

        :param screen: name of the screen object made from the loaded .kv file
        :type screen: str
        :rtype: none
    '''

        filename = screen + '.kv'
        # unload the content of the .kv file
        # reason: it could have data from previous calls
        Builder.unload_file('kv/' + filename)
        # clear the container
        self.root.container.clear_widgets()
        # load the content of the .kv file
        screen = Builder.load_file('kv/' + filename)
        # add the content of the .kv file to the container
        self.root.container.add_widget(screen)


if __name__ == '__main__':
    '''Start the application'''

    conn = sqlite3.connect('data.db')
    print "Opened database successfully"
    MainApp().run()
    conn.close()
    print "Closing database successfully"
