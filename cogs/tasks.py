# Imports
import disnake
from disnake.ext import tasks, commands



import random



from helpers.database import memberchannel_search
from helpers.webhook import webhooksend



# Tasks and Special Events
@tasks.loop(minutes=1.0)
async def status_task(self) -> None:
   statuses = [f"Watching Over {len(self.bot.guilds)} Servers"]
   await self.bot.change_presence(activity=disnake.Game(random.choice(statuses)))
   for guild in self.bot.guilds:
      members = len(guild.members)
      id = guild.id
      ch = await memberchannel_search(f"{id}")
      if ch is not None:
            gd = await self.bot.fetch_guild(id)
            try:
               channel = await self.bot.fetch_channel(ch)
            except disnake.NotFound:
               pass
            try:
               await channel.edit(name=f"Members: {members}")
            except Exception as e:
               print(e)
      else:
            list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            s = random.choice(list)
            if s == "a":
               await webhooksend(f"Member Channel Updates!", "We Reccomend Adding A Memberchannel To Your Server!\nTo Do This, Type `/setmembervoicechannel` In Any Voice Channel In Your Server!", f"{id}")



# Class Tasks
class Tasks(commands.Cog, name="Tasks And Special Events"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
            
   

   @commands.Cog.listener()
   async def on_ready(self):
      await status_task.start(self)