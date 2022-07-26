"""
Astral bot (GUI)
Using Tkinter Package, For GUI
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
from tkinter.messagebox import showinfo



if not os.path.isfile("./secret/config.json"):
    sys.exit("'/secret/config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)


intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents, case_insensitive=False, description="A Simple Discord Bot\nCoded In Python\nPackage: Disnake\nOwner: collin#8694", owner_ids=[config["owners"]], sync_commands=True)
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
    
logged_in = True
def start():
    global control_thread
    control_thread = Thread(target=run, daemon=True)
    control_thread.start()

    if logged_in:
        MainWindow()
    else:
        LoginWindow()
    control_thread.join(1)


class Login:
    def __init__(
        self,
        username: str,
        password: str
        ):
        if username in whitelistedusernames and password in whitelistedpasswords:
            showinfo(
                title="Logged In!",
                message=f"Successfully logged in",
            )
            MainWindow()
        else:
            showinfo("Login Failed", f"Username or Password is incorrect {username}, {password}")
            sys.exit()



class LoginWindow:
    def __init__(
        self,
        title = "Astral Discord Bot",
        geometry = "1200x800",
    ):                
        Window = tk.Tk()
        Window.title(title)
        Window.iconbitmap("img/astral.ico")
        Window.geometry(geometry)
        Window.configure(
            bg="#2f2f2f"
        )
        username = tk.StringVar()
        password = tk.StringVar()
        

        __LOGINFRAME__ = ttk.Frame(Window)
        __LOGINFRAME__.pack(padx=10, pady=10, fill='x', expand=True)
        
        
        USERNAME = ttk.Label(__LOGINFRAME__, text="Username:")
        USERNAME.pack(fill='x', expand=True)

        USERNAME_ENTRY = ttk.Entry(__LOGINFRAME__, textvariable=username)
        USERNAME_ENTRY.pack(fill='x', expand=True)
        USERNAME_ENTRY.focus()

        PASSWORD = ttk.Label(__LOGINFRAME__, text="Password:")
        PASSWORD.pack(fill='x', expand=True)

        PASSWORD_ENTRY = ttk.Entry(__LOGINFRAME__, textvariable=password, show="*")
        PASSWORD_ENTRY.pack(fill='x', expand=True)
        
        
        LOGIN_BUTTON = ttk.Button(__LOGINFRAME__, text="Login", command=lambda: Login(username.get(), password.get()))
        LOGIN_BUTTON.pack(fill='x', expand=True)
    
        loadCogs(self)
        Window.mainloop()
        
        
class MainWindow(tk.Tk):
    def __init__(
        self
    ):
        super().__init__()
        
        
        self.title("Astral Discord Bot")
        self.geometry("1200x800")
        self.iconbitmap("img/astral.ico")
        self.MAINCOLOR = "#2f2f2f"
        self.TEXTCOLOR = "#0072B5"
        self.MAINFONT = ("Arial")
        self.MAINFONTSIZE = 12
        self.configure(
            bg=self.MAINCOLOR,
            highlightcolor=self.MAINCOLOR,
            background=self.MAINCOLOR,
        )
        
        self.__MAINLABEL__ = ttk.Label(self, text="Astral Discord Bot", foreground=self.TEXTCOLOR, font=(self.MAINFONT, self.MAINFONTSIZE), background=self.MAINCOLOR)
        self.__MAINLABEL__.pack()
        
        # page.hide page.lift make clases for every page include discord chat for every server create a dropdown menu (tkinter.OptionMenu), create a invite for the server, ect (maybe even clone server) add some cool panels and yeah have fun
        # ref: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
        
        
        
        
        self.mainloop()

start()