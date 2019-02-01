from kivy.app import App
from _01_Classes.Button_Functions import File_Button
from _01_Classes.Button_Functions import Page_Button
from _01_Classes.Button_Functions import Home_Button
from _01_Classes.Button_Functions import Function_Button
from _01_Classes.Button_Functions import Program_Button
# call buttons from buttons class


from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# call kivy dependencies

import os
import kivy
import time
#import pyautogui
import copy
import math
import socket


# call regular python libraries


class File_Explorer_Grid(GridLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        print(os.getcwd())
        # prints directory for changing
        # self.bind(minimum_height=self.setter('height'))

        #os.chdir(r"C:\Users\Duncan")
        # change directory to user directory
        print(os.getcwd())

        self.cols = 4
        self.button_amount = 0
        self.buttons = []
        self.home_buttons = []
        self.page = 0
        self.directories = []
        self.paths = []
        self.host = '10.162.202.172'
        self.port = 5000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))

        # initalize variables

        self.build_obs()
        # build home screen

    def __getitem__(self, index):
        return self.function[index]

    def __setitem__(self, index, value):
        self.function[index] = value

    # functions to be able to have an array of the object

    def get_button_amount(self):
        return self.button_amount

    def set_button_amount(self, amount):
        self.button_amount = amount

    def get_buttons(self):
        return self.buttons

    def set_buttons(self, new_buttons):
        self.buttons = new_buttons

    def set_directories(self):
        # self.directories = directories
        for (dirpath, dirnames, filenames) in os.walk("."):
            self.directories.extend(dirnames)
            break

    def get_directories(self):
        return self.directories

    def set_paths(self):
        for i in range(len(self.directories)):
            self.paths.append(os.getcwd() + chr(92)
                              + self.directories[i])
            # find the directories and add create paths out of them

    def get_paths(self):
        return self.paths

    def set_pages(self):

        self.division = math.ceil(self.button_amount / 12)

        for i in self.division:
            self.pages = self.division

            # figure out number of pages based on number of buttons

    def change_page(self, direction):

        if direction == 'f':
            self.page += 1
        if direction == 'b':
            self.page -= 1

        # function to change the page of buttons you are on

    def set_home_buttons(self, buttons):
        for i in range(len(buttons)):
            self.home_buttons.append(buttons[i])
            buttons[i].set_text('file explorer')

    def build(self):
        # builds the file buttons

        print('build')

        self.button_amount = 0
        self.buttons = []
        self.home_buttons = []
        self.directories = []
        self.paths = []

        # clear all needed variables

        self.set_directories()
        self.set_paths()
        self.set_button_amount(len(self.directories))

        # update variables to correct amount

        for i in range(12):
            self.buttons.append(File_Button())
            # add file button to button array

            if i + (11 * self.page) >= len(self.directories):
                break

                # error checking to make sure that directory is not
                # out of range of the index

            self.buttons[i].set_directory(self.paths[i + (11 * self.page)])
            self.buttons[i].set_text(self.directories[i + (11 * self.page)])
            self.buttons[i].set_grid(self)

            # set path and text of the buttons and set the grib to current
            # grid
            print(self.buttons[i])

            # self.add_widget(self.buttons[i])

        for i in range(12 - len(self.buttons)):
            self.buttons.append(File_Button())

            # fill empty button slots with functionless buttons

            # self.add_widget(self.buttons[i + (12 - excess_space)])

        for i in range(4):
            self.buttons.append(Page_Button())

            # add buttons for switching page

        self.buttons[12].set_direction('f')
        self.buttons[13].set_direction('b')
        # set page direction for buttons

        self.buttons[12].text = "forward"
        self.buttons[13].text = "back"
        # set text for page change buttons

        self.buttons[12].bind_direction()
        self.buttons[13].bind_direction()
        # bind the direction button function

        self.buttons[12].set_grid(self)
        self.buttons[13].set_grid(self)
        # set grid of buttons to current grid

        for i in range(len(self.buttons)):
            self.add_widget(self.buttons[i])

        # add widgets to grid

    def build_home(self):
        # builds home screen

        self.home_buttons = []
        # clear all needed variables

        for i in range(12):
            self.home_buttons.append(Home_Button())
            self.home_buttons[i].set_grid(self)
            self.home_buttons[i].set_text(str(i))
            self.home_buttons[i].bind_button(i)
            # set functions and text for home buttons and set grid to current
            # grid

        for i in range(12):
            self.add_widget(self.home_buttons[i])

            # add widgets to grid

    def build_obs(self):
        # builds obs screen
        self.buttons = []
        function_key = []

        names = ['\n\n\n\n\n Record', '\n\n\n\n\nStudio Mode',
                 '\n\n\n\n\nHide/Show Capture', '\n\n\n\n\nHide/Show Image',
                 '\n\n\n\n\nscene 1', '\n\n\n\n\nscene 2',
                 '\n\n\n\n\nMute Desktop', '\n\n\n\n\nMute Mic',
                 '\n\n\n\n\nopen obs', '\n\n\n\n\ndesktop folder']
        # set names for button text

        for i in range(12):
            function_key.append("f" + str(i+13))
            # set function keys

            if i < 10:
                print(i)
                self.buttons.append(Function_Button(self.s, i + 1))
                self.buttons[i].set_text(names[i])
                self.buttons[i].set_function(function_key[i])
                # set functions for obs buttons

            if i > 9:
                print(i)
                self.buttons.append(Function_Button(self.s, 64))
                self.buttons[i].set_text(function_key[i])
                self.buttons[i].set_function(function_key[i])
                # give other buttons respective function keys and set text
                # to the text of the function key

            self.add_widget(self.buttons[i])
            # add widgets to grid

    def build_programs(self):
        # builds buttons for programs
        self.buttons = []
        directories = [r'C:\Program Files (x86)\obs-studio\bin\64bit\obs64.exe',
                       r"C:\Program Files\PuTTY\putty.exe"]
        # set directories to the location of programs to be opened

        for i in range(12-(12 - len(directories))):
            self.buttons.append(Program_Button())
            self.buttons[i].set_grid(self)
            print(directories[i])
            self.buttons[i].set_program(directories[i])
            # add buttons to array, set grid to current grid and set the
            # program to the function

        for i in range(12-len(directories)):
            self.buttons.append(Button())
            # fill empty futton slots

        for i in range(12):
            self.add_widget(self.buttons[i])

            # add widgets to grid
