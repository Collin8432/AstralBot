"""
Astral Bot
Disnake API Wrapper
Coded by Asrto
"""
# Imports
import json
import os
import sys
import asyncio



import disnake
from disnake.ext.commands import Bot
from helpers.webhook import webhooksend


 
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
        except Exception as e:
            print(e)
            

try:
    loadCogs()
except Exception as e:
    asyncio.run(webhooksend("err", f"{e}", 944297787779072020))


@bot.user_command(name="test")
async def usercmd(interaction):
    embed=disnake.Embed(description="test")
    await interaction.send(embed=embed)
    
    

@bot.message_command(name="test")
async def msgcmd(interaction):
    embed=disnake.Embed(description="test")
    await interaction.send(embed=embed)



# Starting The Bot
bot.run(config["token"])