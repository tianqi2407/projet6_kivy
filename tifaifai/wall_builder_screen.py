from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.actionbar import ActionBar

__all__ = ('WallBuilderScreen', 'ScreenBuilderScreen')

from kivy.app import App
from kivy.lang import Builder

Builder.load_file('data/screens/wall_builder_screen.kv')
Builder.load_file('data/screens/screen_builder_screen.kv')


class ScreenBuilderScreen(Screen):
    title = "Screen Builder"


class WallBuilderScreen(Screen):
    title = "Wall Builder"


class RootWidget(BoxLayout):
    manager = ScreenManager()
    manager.add_widget(WallBuilderScreen(name='wallBuilder'))
    manager.add_widget(ScreenBuilderScreen(name='screenBuilder'))

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
        self.available_screens = sorted(['WallBuilderScreen', 'ScreenBuilderScreen'])
        return RootWidget().manager


if __name__ == '__main__':
    MainApp().run()
