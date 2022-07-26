"""
Contains mute/unmute commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands


from utils.db import *
from utils.color import color
 

class Muteunmute(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   
   @commands.slash_command(
      name="mute",
      description="mutes a member",
   )
   @commands.has_permissions(manage_roles=True)
   async def mute(self, interaction: ApplicationCommandInteraction,
                  user: disnake.User
                  ) -> None:
      muterole = fetch_guild_information("guild_muterole", f"{interaction.guild.id}")
      muterole = interaction.guild.get_role(muterole)
      try:
         await user.add_roles(muterole)  
         embed = disnake.Embed(
               title="Member Muted!",
               description=f"**<@{user.id}> Was Muted By <@{interaction.author.id}>**",
               color=color,
               timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
               text="Requested by {}".format(interaction.author)
         )
         await send(interaction=interaction, embed=embed)
      except:
         embed = disnake.Embed(
               title="Error!",
               description=f"**Error While Muting Member, Make Sure Member Does Not Have Higher Roles Than Me**",
               color=color,
               timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
               text="Requested by {}".format(interaction.author)
         )


   @commands.slash_command(
      name="unmute",
      description="unmutes a member",

   )
   @commands.has_permissions(manage_roles=True)
   async def unmute(self, interaction: ApplicationCommandInteraction,
                  user: disnake.User):
      muterole = fetch_guild_information("guild_muterole", f"{interaction.guild.id}")  
      muterole = interaction.guild.get_role(muterole)
      try:
         await user.remove_roles(muterole)
         embed = disnake.Embed(
               title="Member Unmuted!",
               description=f"**{user.mention} was unmuted by {interaction.author.mention}**",
               color=color,
               timestamp=disnake.utils.utcnow(),
         )
         await send(interaction=interaction, embed=embed)
      except:
         embed = disnake.Embed(
               title="Error!",
               description=f"**Error While Unmuting Member, Make Sure Member Does Not Have Higher Roles Than Me**",
               color=color,
               timestamp=disnake.utils.utcnow(),
         )
         await send(interaction=interaction, embed=embed)
