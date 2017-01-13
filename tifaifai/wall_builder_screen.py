from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel

__all__ = ('WallBuilderScreen', 'ScreenBuilderScreen')

from kivy.app import App
from kivy.lang import Builder

Builder.load_file('data/screens/wall_builder_screen.kv')
Builder.load_file('data/screens/screen_builder_screen.kv')

# Builder.load_string('''
# <RootWidget>
#     manager: manager
#     do_default_tab: False
#
#     ScreenManager:
#         id: manager
#         Screen:
#             id: wallBuilder
#             name: 'wallBuilder'
#             BoxLayout:
#                 Button:
#                     text: "POMME DE PIN"
#         Screen:
#             id: screenBuilder
#             name: 'screenBuilder'
#             BoxLayout:
#                 Button:
#                     text: "Screen Builder"
#     TabbedPanelHeader:
#         text: wallBuilder.name
#         screen: wallBuilder.name
#     TabbedPanelHeader:
#         text: screenBuilder.name
#         screen: screenBuilder.name
# ''')


class ScreenBuilderScreen(Screen):
    title = "Screen Builder"


class WallBuilderScreen(Screen):
    title = "Wall Builder"


class RootWidget(TabbedPanel):
    manager = ScreenManager()
    manager.add_widget(WallBuilderScreen(name='wallBuilder'))
    manager.add_widget(ScreenBuilderScreen(name='screenBuilder'))

    # def switch_to(self, header):
    #     self.manager.current = header.screen
    #     self.current_tab.state = "normal"
    #     header.state = 'down'
    #     self._current_tab = header

    def showcase_anchorlayout(self, layout):

        def change_anchor(self, *l):
            if not layout.get_parent_window():
                return
            anchor_x = ('left', 'center', 'right')
            anchor_y = ('top', 'center', 'bottom')
            if layout.anchor_x == 'left':
                layout.anchor_y = anchor_y[anchor_y.index(layout.anchor_y) - 1]
            layout.anchor_x = anchor_x[anchor_x.index(layout.anchor_x) - 1]


class MainApp(App):
    def build(self):
        self.available_screens = sorted([
            'WallBuilderScreen', 'ScreenBuilderScreen'])
        return RootWidget().manager


if __name__ == '__main__':
    MainApp().run()
