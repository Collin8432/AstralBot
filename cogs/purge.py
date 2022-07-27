"""
Contains the purge command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake.ext import commands


 from utils.color import color


class Purge(commands.Cog):
   def __init__(self, bot):
      self.bot = bot


   @commands.slash_command(
      name="purge",
      description="purges all messages in a channel",
   )
   @commands.has_permissions(manage_messages=True)
   async def purge(interaction: disnake.CommandInteraction):  
      embed = disnake.Embed(
         title="Messages Purged!",
         description="**Purged All Messages In This Channel**",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      await interaction.send(embed=embed, ephemeral=True)
      await interaction.channel.purge(limit=200)