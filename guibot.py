"""
Astral bot (GUI)
Using Kivy API
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
import asyncio
from threading import Thread
from typing import Optional


import disnake
from disnake.ext.commands import Bot
import tkinter as tk
from tkinter import ttk

if not os.path.isfile("./secret/config.json"):
    sys.exit("'/secret/config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)


intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents, case_insensitive=False, description="A Simple Discord Bot Coded by Astro", owner_ids=[config["owners"]], sync_commands=True)
token = config.get("token")
bot.remove_command("help")


async def runtime():
    bot.run(token)
    
    
def loadCogs(self):
    """
    Load Extentions Of The Bot
    """
    if os.path.isfile("cogs/__init__.py"):
        try:
            bot.load_extension(f"cogs/__init__")
            print("Loaded Cogs ✅")
        except Exception as e:
            print(e)
            

def run():
    bot.run(token)
    
    
def start():
    global control_thread
    control_thread = Thread(target=run, daemon=True)
    control_thread.start()

    Window()
    control_thread.join(1)


class Window():
    def __init__(
        self,
        title = "Astral Discord Bot",
        geometry = "1200x800",
    ):
        
        
        Window = tk.Tk()
        Window.title(title)
        Window.iconbitmap("img/astral.ico")
        Window.geometry(geometry)
        
        Astral_Main_Label = ttk.Label(Window, text=title)
        Astral_Main_Label.pack()
        
        
        Astral_Main_Frame = ttk.Frame(Window)
        Astral_Main_Frame.pack()
        
        Window.mainloop()
    
        

   
start()
