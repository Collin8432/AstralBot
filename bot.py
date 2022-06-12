# Imports
import json
import os
import sys
import traceback


import disnake
from disnake.ext.commands import Bot



# Setting Up Bot
if not os.path.isfile("./secret/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)



intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents)
token = config.get("token")



def load_commands(file: str) -> None:
    for file in os.listdir(f"./cogs/"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded ✅ {extension}.py")
            except disnake.ext.commands.errors.ExtensionAlreadyLoaded:
                pass
            except Exception as e:
                traceback.print_exc()
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension ❌ {extension}.py\n{exception}")



if __name__ == "__main__":
    load_commands("general")
    load_commands("moderation")
    load_commands("fun")
    load_commands("listeners")
    load_commands("setup")
    load_commands("tasks")
    load_commands("verification")

 

# Starting The Bot
bot.run(config["token"])
