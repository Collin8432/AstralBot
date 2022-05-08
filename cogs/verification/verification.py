import json
import os
import random
import sys
import platform

import asyncio
import aiohttp
import datetime
import disnake
import random
from disnake.ext import commands
from disnake.ext.commands import Context
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks



class Verification(commands.Cog, name="Verification Cmds"):
    def __init__(self, bot):
      self.bot = bot
    from PIL import Image
    from PIL import ImageDraw
   
    img = Image.open('astral.png')
   
    I1 = ImageDraw.Draw(img)
   
    I1.text((200, 200), "nice Car", fill=(255, 0, 0))
   
    img.save("astral2.png")


def setup(bot):
    bot.add_cog(Verification(bot))