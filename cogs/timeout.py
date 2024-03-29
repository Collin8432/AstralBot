"""
Contains the timeout command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands


from typing import Optional, Literal


from utils.color import color
from utils.DeleteButton import DeleteButton


class Timeout(commands.Cog):

   def __init__(self, bot):
      self.bot = bot


   @commands.slash_command(
      name="timeout",
      description="timeouts a member",
   )
   @commands.has_permissions(manage_roles=True)
   async def timeout(self, interaction: ApplicationCommandInteraction,
                     user: disnake.Member,
                     time: str,
                     reason: Optional[str] = None):
      await user.timeout(user, duration=time)  
      embed = disnake.Embed(
         title="Member Timed Out!",
         description=f"**<@{user.id}> Was Timeout By <@{interaction.author.id}>\n**Time:**\n{time}\n**Reason:**\n{reason}**",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      await interaction.send(embed=embed, view=DeleteButton())
