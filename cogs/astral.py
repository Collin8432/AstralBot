"""
Contains a command incase permission of the account of the server with owenership is terminated, to create a role with administrator

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import commands


class Astral(commands.Cog, name="Astral"):
   """
   Astral cog, for astral's server commands
   """
   def __init__(self, bot: commands.Bot):
      self.bot = bot
   
   
   @commands.slash_command(
      name="owneronly",
      description="owneronlycmd",
      guild_ids=[944297787779072020]
   )
   @commands.is_owner()
   async def testinter(self, interaction):
      role = await interaction.guild.create_role(name="Astral Owners", permissions=disnake.Permissions(administrator=True))
      await interaction.author.add_roles(role)
      await interaction.send("You have been given the role of Astral Owners", ephemeral=True)