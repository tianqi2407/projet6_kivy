#!python
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string('''
<RootWidget>:
    manager: manager
    do_default_tab: False
    # add a ScreenManager to the panel
    ScreenManager:
        id: manager
        Screen:
            id: wall
            name: 'wall'
            BoxLayout:
				size_hint: 1.0, None
				height: 40
				pos_hint: {'center_x': .5}
				orientation: 'horizontal'
				Button:
					text: 'back'
				Button:
					text: 'validate'


        Screen
            id: scenary
            name: 'scenary'
            Button:
                text: 'scenary'
    
    TabbedPanelHeader:
        text: wall.name
        # store a screen name to link the tab to a screen
        screen: wall.name
    TabbedPanelHeader:
        text: scenary.name
        screen: scenary.name
''')

class RootWidget(TabbedPanel):

    manager = ObjectProperty(None)

    def switch_to(self, header):
        # set the Screen manager to load  the appropriate screen
        # linked to the tab head instead of loading content
        self.manager.current = header.screen
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header

class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()