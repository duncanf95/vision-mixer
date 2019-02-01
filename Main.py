from _01_Classes.Button_Grids import File_Explorer_Grid
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
# from kivy.app import runTouchApp

from kivy.app import App


# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button


class SimpleKivy(App):
    def build(self):
        Config.set('kivy', 'keyboard_mode', 'systemandmulti')
        self.button_grid = File_Explorer_Grid()
        # setup button grid
        self.scroll_grid = ScrollView(size_hint=(1, None),
                                      size=(self.button_grid.width,
                                      self.button_grid.height))
        # setup scroll grid (not working)

        return self.button_grid


if __name__ == "__main__":
    SimpleKivy().run()
    #run app
