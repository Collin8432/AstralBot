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
import requests
from threading import Thread


import disnake
from disnake.ext.commands import Bot
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import showinfo



if not os.path.isfile("./secret/config.json"):
    sys.exit("'/secret/config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)


intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents, case_insensitive=False, description="A Simple Discord Bot Coded by Astro", owner_ids=[config["owners"]], sync_commands=True)
token = config.get("token")
bot.remove_command("help")


auth = requests.get("https://astralsb.ga/authsadj214912090784102.json").text
auth = json.loads(auth)


whitelistedusernames = auth["whitelistedusernames"]
whitelistedpasswords = auth["whitelistedpasswords"]


async def runtime():
    bot.run(token)
    
    
def loadCogs(self):
    """
    Load Extentions Of The Bot
    """
    print("Loading Extentions Of The Bot")
    if os.path.isfile("cogs/__init__.py"):
        try:
            print("Attempting to load cogs")
            bot.load_extension(f"cogs.__init__")
            print("Loaded Cogs ✅")
        except Exception as e:
            print(e)
            print(self)


def run():
    bot.run(token)
    
    
def start():
    global control_thread
    control_thread = Thread(target=run, daemon=True)
    control_thread.start()

    Window()
    control_thread.join(1)

# TODO: Add a way too fetch the username and pwd
class Login:
    username = Window().username.get()
    password = Window().password.get()
    if username in whitelistedpasswords:
        if password in whitelistedpasswords:
            pass
    else:
        showinfo("Login Failed", "Username or Password is incorrect")
        sys.exit()
    showinfo(
        title="Logged In!",
        message=f"Successfully logged in",
    )


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

        username = tk.StringVar()
        password = tk.StringVar()
        

        Astral_Login_Frame = ttk.Frame(Window)
        Astral_Login_Frame.pack(padx=10, pady=10, fill='x', expand=True)
        
        email_label = ttk.Label(Astral_Login_Frame, text="Username:")
        email_label.pack(fill='x', expand=True)

        email_entry = ttk.Entry(Astral_Login_Frame, textvariable=username)
        email_entry.pack(fill='x', expand=True)
        email_entry.focus()

        password_label = ttk.Label(Astral_Login_Frame, text="Password:")
        password_label.pack(fill='x', expand=True)

        password_entry = ttk.Entry(Astral_Login_Frame, textvariable=password, show="*")
        password_entry.pack(fill='x', expand=True)

        login_button = ttk.Button(Astral_Login_Frame, text="Login", command=Login)
        login_button.pack(fill='x', expand=True, pady=10)

    
        loadCogs(self)
        Window.mainloop()


start()