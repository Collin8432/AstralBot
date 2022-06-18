# Imports
import json
import os
import sys



import disnake
from disnake.ext.commands import Bot


 
# Setting Up Bot
if not os.path.isfile("./secret/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)



intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents, case_insensitive=False, description="A Simple Discord Bot Coded by Astro", owner_ids=[config["owners"]], sync_commands=True)
token = config.get("token")
bot.remove_command("help")



def loadCogs():
    if os.path.isfile("./cogs/__init__.py"):
        try:
            bot.load_extension(f"cogs.__init__")
            print("Loaded Cogs ✅")
        except:
            pass



if __name__ == "__main__":
    loadCogs()



# Starting The Bot
bot.run(config["token"])