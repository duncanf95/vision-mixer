from kivy.uix.button import Button
import os
import time
#import pyautogui
import socket


class File_Button(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.directory = ""
        self.text = ""
        self.bind(on_press=lambda x: self.button_set())
        self.grid = object

    def button_set(self):
        print(self.directory)
        # os.system(r'"explorer "' +
        #           str(self.directory))
        os.chdir(self.directory)
        self.grid.clear_widgets()
        self.grid.build()

    def set_directory(self, directory):
        self.directory = directory

    def get_directory(self):
        return self.directory

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid


class Page_Button(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid = object
        self.direction = ''
        self.size_hint_y = None
        self.height = 75

    def button_set(self):
        self.grid.change_page(self.direction)
        self.grid.clear_widgets()
        self.grid.build()

    def set_direction(self, direction):
        self.direction = direction

    def bind_direction(self):
        self.bind(on_press=lambda x: self.button_set())

    def set_grid(self, grid):
        self.grid = grid


class Home_Button(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = object
        self.text = ''

    def button_set(self):
        self.grid.clear_widgets()
        self.grid.build()

    def button_set_2(self):
        self.grid.clear_widgets()
        self.grid.build_obs()

    def button_set_3(self):
        self.grid.clear_widgets()
        self.grid.build_programs()

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid

    def set_home(self, home):
        self.home = home

    def get_home(self):
        return self.home

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def bind_button(self, type):
        if type == 0:
            self.bind(on_press=lambda x: self.button_set())
        if type == 1:
            print('words')
            self.bind(on_press=lambda x: self.button_set_2())
        if type == 2:
            self.bind(on_press=lambda x: self.button_set_3())
        else:
            print('pass')


class Function_Button(Button):

    def __init__(self, input_socket, ID, **kwargs):
        super().__init__(**kwargs)
        self.grid = object
        self.text = ''
        self.function = ''
        self.bind(on_press=lambda x: self.button_set())
        self.s = input_socket
        self.ID = ID




    def button_set(self):
        print(self.function)
        # time.sleep(4)
        #pyautogui.keyDown(self.function)
        # time.sleep(1)
        #pyautogui.keyUp(self.function)
        message = self.ID

        while message != '':
            self.s.send(str.encode(str(message)))
            data = self.s.recv(1024)
            print('Recieved from server: '+data.decode('utf-8'))
            self.s.close
            message = ''

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function


class Program_Button(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = object
        self.program = ''
        self.text = self.program
        self.directory = ''
        self.bind(on_press=lambda x: self.button_set())

    def button_set(self):
        # time.sleep(4)
        os.chdir(self.directory)
        os.startfile(self.program)

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_program(self, directory):
        length = len(directory)
        print(directory)
        for i in range(len(directory)):
            print(r'\\')
            if ("\\" in r"%r" % directory[length-i:length]):
                self.program = directory[length-i+1:length]
                self.directory = directory[:length - i]
                self.set_text(self.program)
                break

    def get_program(self):
        return self.program
