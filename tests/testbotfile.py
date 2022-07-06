from pip import main
import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


bot.run("BOT_TOKEN")
