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
from kivy.uix.behaviors import DragBehavior
import wall_builder_screen as wbs
import sqlite3
import kivy
kivy.require('1.8.0')
from kivy.core.window import Window

Window.size = (1120, 630)


class RootWidget(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''

    container = ObjectProperty(None)


class MainApp(App):

    '''This is the app itself'''

    def build(self):
        '''This method loads the root.kv file automatically

        :rtype: none
        '''
        # loading the content of root.kv
        
        self.root = Builder.load_file('kv/root.kv')
        self.wall = Builder.load_file('kv/wall_builder_screen.kv')
        self.screen = Builder.load_file('kv/screen_builder_screen.kv')
        self.media = Builder.load_file('kv/media.kv')
        self.addMedia = Builder.load_file('kv/add_media.kv')

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
    #wbs.startDB()
    #wbs.openDB()
    MainApp().run()
    wbs.closeDB()
