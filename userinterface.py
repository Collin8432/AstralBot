"""
Astral (GUI)
Using PyQt5 API
~~~~~~~~~~~~~~~~~~~~~~~~~

Contains initailization of the GUI and classes containing elements of the GUI

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import json
import os
import sys
from typing import Optional

import disnake
from disnake.ext.commands import Bot
from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *


if not os.path.isfile("./secret/config.json"):
    sys.exit("'/secret/config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)


intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents, case_insensitive=False, description="A Simple Discord Bot Coded by Astro", owner_ids=[config["owners"]], sync_commands=True)
token = config.get("token")
bot.remove_command("help")
# TODO: fix this all

def runtime(self):
    bot.run(token, app=self)
class Window(QMainWindow):
    def __init__(self,
                    app: QtGui.QGuiApplication,
                    *,
                    window_title: str = "Astral",
                    geometry: tuple = (800, 800),
                    
                    ):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setFixedSize(QSize(geometry[0], geometry[1]))
        self.app = app
        self.show()
        
        self.button1 = QPushButton(self)
        self.button1.setText("Start Bot")
        self.button1.move(256,32)      
        self.button1.clicked.connect(self.startbot)
        self.button1.show()
        
        self.button2 = QPushButton(self)
        self.button2.setText("Stop Bot")
        self.button2.move(64,32)
        self.button2.clicked.connect(self.stopbot)
        # self.label = QLabel("Enter a guild id to begin messaging")
        # self.setCentralWidget(self.button1)
        self.app.exec()
    
    
    def editlabel(self, text: str):
        self.label.setText(text)
        
    def loadCogs():
        """
        Load Extentions Of The Bot
        """
        if os.path.isfile("./cogs/__init__.py"):
            try:
                bot.load_extension(f"cogs.__init__")
                print("Loaded Cogs ✅")
            except Exception as e:
                print(e)
    def startbot(self):
        self.button2.show()
        self.button1.hide()
        runtime
    def stopbot(self):
        sys.exit()
def __init__():
   app = QApplication(sys.argv)
   Window(app)
   
__init__()
