"""
Contains the sub commands of the bot containing the prefix astral

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction


from utils.color import color
 

global starttime
starttime = disnake.utils.utcnow()


class Astralsub(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot


   @commands.slash_command(
      name="astral",
      description="support, invite, uptime, credits"
   )
   async def astral(self, interaction):
      pass

   
   @astral.sub_command(
      name="support",
      description="gets invite link to astral's discord server",
   )
   async def link(self, interaction):
      embed = disnake.Embed(
         title="Invite Link!",
         description="https://discord.gg/NdwvUHCDcM",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await send(interaction=interaction, embed=embed)


   @astral.sub_command(
      name="invite",
      description="gets invite link to astral discord bot",
   )
   async def bot(self, interaction):
      embed = disnake.Embed(
         title="Bot Invite Link!",
         description="https://discord.com/api/oauth2/authorize?client_id=938579223780655145&permissions=8&scope=bot%20applications.commands",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await send(interaction=interaction, embed=embed)
      
   
   @astral.sub_command(
      name="uptime",
      description="shows the uptime of the bot",
   )
   async def uptime(self, interaction):
      end_time = disnake.utils.utcnow()
      diff = end_time - starttime
      seconds = diff.seconds % 60
      minutes = (diff.seconds // 60) % 60
      hours = (diff.seconds // 3600) % 24
      days = diff.days
      uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
      embed = disnake.Embed(
         title="Uptime!",
         description="**The Bot Has Been Online For: {}**".format(uptime_str),
         color=color,
         timestamp=disnake.utils.utcnow(),
      ) 
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await send(interaction=interaction, embed=embed)
      
   
   @astral.sub_command(
      name="credits",
      description="shows credits for the bot",
   )
   async def credits(self, interaction):
      embed = disnake.Embed(
         title="Credits!",
         description=f"**Astral Bot**\n[**Disnake - Discord API Wrapper**](https://disnake.dev)\n[**Original Template - Credits To kkrypt0nn**](https://github.com/kkrypt0nn/Python-Discord-Bot-Template)\n**Coded By <@935339228324311040>**",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await send(interaction=interaction, embed=embed)
      
      
   @astral.sub_command(
      name="suggest",
      description="suggest something to add to the bot"
   )
   async def suggestion(self,
                        interaction: ApplicationCommandInteraction,
                        suggestion: str = None):
      ch = self.bot.get_channel(992463726814974082)
      embed = disnake.Embed(
         title="New Suggestion!",
         description=f"**Suggestion:\n{suggestion}**",
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Sent by {name} • {id}".format(
               name=interaction.author,
               id = interaction.author.id
         )
      )
      await ch.send(embed=embed)
      await interaction.send(f"Suggestion sent successfully!\n{suggestion}", ephemeral=True)
      
      
   @astral.sub_command(
      name="probelm",
      description="report a problem to the bot"
   )
   async def problem(self,
                     interaction: ApplicationCommandInteraction,
                     problem: str = None):
      ch = self.bot.get_channel(992463768674119730)
      embed = disnake.Embed(
         title="New Problem!",
         description=f"**Problem:\n{problem}**",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Sent by {name} • {id}".format(
               name = interaction.author,
               id = interaction.author.id
         )
      )
      await ch.send(embed=embed)
      await interaction.send(f"Problem sent successfully!\n{problem}", ephemeral=True)
      
      
   @astral.sub_command(
        name="ping",
        description="pings bot latency",
   )
   async def ping(interaction):
      latency = interaction.bot.latency * 1000  
      pong = round(latency, 2)
      embed = disnake.Embed(
         title="Pong!",
         description="**Bot Latency:\n{} ms**".format(pong),
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await send(interaction=interaction, embed=embed)  