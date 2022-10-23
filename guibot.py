"""
Astral bot (GUI)
Using Tkinter Package, For GUI
~~~~~~~~~~~~~~~~~~~~~~~~~

Contains initailization of the GUI and classes containing elements of the GUI

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """

import json
import os
import sys
import tkinter as tk
from threading import Thread
from tkinter import ttk, Tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Label
from typing import Optional

import disnake
import requests
from disnake.ext.commands import Bot

if not os.path.isfile("./secret/config.json"):
    sys.exit("'/secret/config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)

intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents, case_insensitive=False,
          description="A Simple Discord Bot\nCoded In Python\nPackage: Disnake\nOwner: collin#8694",
          owner_ids=[config["owners"]], sync_commands=True)
token = config.get("token")
bot.remove_command("help")

auth = requests.get("https://astralsb.ga/authsadj214912090784102.json").text
auth = json.loads(auth)

whitelistedusernames = auth["whitelistedusernames"]
whitelistedpasswords = auth["whitelistedpasswords"]


def log_or_print(content, ttkwidget: Optional[ttk.Widget], tkwidget: Optional[tk.Widget]):
    try:
        if ttkwidget is not None:
            tkwidget.update()
        else:
            ttkwidget.update()
    except:
        print(content)
    finally:
        print(Exception)


async def runtime():
    bot.run(token)


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


loadCogs()


def run():
    bot.run(token)


logged_in = True


def start():
    global control_thread
    control_thread = Thread(target=run, daemon=True)
    control_thread.start()

    if logged_in:
        import time
        time.sleep(2)
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
            title="Astral Discord Bot",
            geometry="1200x800",
    ):
        Window: Tk = tk.Tk()
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

        USERNAME: Label = ttk.Label(__LOGINFRAME__, text="Username:")
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

        Window.mainloop()


class MainWindow(tk.Tk):
    def __init__(
            self
    ):
        super().__init__()
        style = ttk.Style()
        style.theme_use('vista')
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

        guilds = [guild for guild in bot.guilds]
        guilds.append("12345678998765432112345678900987")
        guilds.append("12345678998765432112345678900987")
        guilds.append("12345678998765432112345678900987")
        variable = tk.StringVar(self)
        variable.set(guilds[1])
        self.Dropdown = ttk.OptionMenu(self, variable, *guilds)
        self.Dropdown.place(x=0, y=0)

        self.MainGuildInfo = ttk.Frame(self)
        self.MainGuildInfo.place(in_=self, x=225, y=0)
        self.MainGuildInfo.configure(height=100, width=100)

        self.mainloop()


start()
