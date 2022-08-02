"""
Contains task and information for the bot
 
Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import tasks, commands


import random


from utils.db import *


class Tasks(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
      self.status_task.start()
      
      
   @tasks.loop(minutes=1.0)
   async def status_task(self) -> None:
      statuses = ["Astral GUI", "Creating Astral GUI", "Discord GUI Bot"]
      # statuses = [f"Watching Over {len(self.bot.guilds)} Servers!", "With You!", "With Astro!", "In Space!"]
      await self.bot.wait_until_ready()
      await self.bot.change_presence(activity=disnake.Game(random.choice(statuses)))
      try:
         for guild in self.bot.guilds:
            members = len(guild.members)
            ch = fetch_guild_information("guild_membercountvoicechannel", f"{guild.id}")
            if ch is not None:
                  try:
                     channel = await self.bot.fetch_channel(ch)
                  except disnake.NotFound:
                     pass
                  try:
                     await channel.edit(name=f"Members: {members}")
                  except Exception as e:
                     print(e)
      except Exception as e:
         print(e)
         