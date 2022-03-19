import json
import os
import random
import sys
import platform

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands

from helpers import checks

class Moderation(commands.Cog, name="Mod Cmds"):
   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(
      name="Kick",
      description="Kicks A User From A Server",
      options=[
         Option(
               name="Member",
               description="Select The Member To Kick",
               type=OptionType.user,
               required=True
         ),
         Option(
               name="Reason",
               description="Reason To Kick User",
               type=OptionType.string,
               required=False
         )
      ]
   )
   @commands.has_permissions(kick_members=True)
   @checks.not_blacklisted()
   async def kick(interaction: ApplicationCommandInteraction, Reason: str, user: disnake.User):
      member = await interaction.guild.get_or_fetch_member(user.id)
      if member.guild.permissions.administrator:
         embed = disnake.Embed(
            title="Error Kicking Member!",
            description="Member Has Administrator Permissons!",
            color = 0xDC143C
         )
         await interaction.send(embed=embed)
      else:
         try:
            embed = disnake.Embed(
               title = "Member Kicked!", 
               description = f"**{member}** Was Kicked By **{interaction.author}**\n**Reason: {Reason}",
               color = 0xDC143C
            )
            await interaction.send(embed=embed)
            await member.kick(reason=Reason)

         except:
            embed = disnake.Embed(
               title = "Error!",
               description = "Error Kicking Member",
               color = 0xDC143C
            )
            await interaction.send(embed=embed)



   


def setup(bot):
    bot.add_cog(Moderation(bot))