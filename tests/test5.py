# Imports
from tinydb import TinyDB, Query
import disnake
from disnake.ext import tasks
import os



# Setting DB Up
db = TinyDB("database.json")
Query = Query()


async def add_guild(guild_id):
   db.update({"guild_id": guild_id}, Query.guild_id == guild_id)
   

async def add_guild_message(guild_id, message_id):
   db.update({"db_guild_message": message_id}, Query.guild_id == guild_id)
   
   
async def idsearch(guild_id):
   results = db.search(Query.guild_id == guild_id)
   for result in results:
      return result["guild_id"]
   
@tasks.loop(seconds=30)
async def checkmessage(self):
   guilds = self.bot.guilds
   for guild in guilds:
      try:
         await add_guild(f"{guild.id}")
      except:
         pass
      try:
         await idsearch(f"{guild.id}")
         ids=True
      except:
         ids=False   
      while ids == True:
         pass
      while ids == False:
         for channel in guild.text_channels:
            ch = await self.bot.get_channel(channel.id)
            await ch.send("message")