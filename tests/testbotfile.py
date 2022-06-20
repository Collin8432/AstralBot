import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext.commands import Bot


import os 
import sys
import json  



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

async def on_connect() -> None:
   print("ready")
   app = await bot.application_info()
   ciu = app.custom_install_url
   print(ciu)
   
   
# Starting The Bot
bot.run(config["token"])