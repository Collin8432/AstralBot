"""
Contains userinfo command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake.ext import commands


from utils.message import send
from utils.color import color



userinfo = """
**User Name:** `{username}`
**User Id:** `{userid}`
**Nickname?:** `{nickname}`
**Joined At:** `{joindate}`
**Account Created At:** `{accountcreatedat}`
**Is Boosting Guild?:** `{boostingguild}`

**Is Bot Account?:** `{isbotaccount}`
**Animated Avatar?:** `{animatedavatar}`
**Top Role:** {toprole}
**Roles:** \n{roles}

**Public Flags:**\n{flags}
"""


class Userinfo(commands.Cog):

   def __init__(self, bot: commands.Bot):
      self.bot = bot
      
   
      
   @commands.slash_command(
      name="userinfo",
      description="gets a user's information",
   )
   async def userinfo(self, interaction: disnake.ApplicationCommandInteraction,
                      user: disnake.User = None):
      if user.bot == True:
         bot = "Is Bot Account"
      else:
         bot = "Isn't Bot Account"
      roles = [role.mention for role in user.roles]
      roles = str(roles).replace("]", "").replace("[", "").replace("'", "")
      boosters = interaction.guild.premium_subscribers
      if interaction.author in boosters:
         boosting = True
      else:
         boosting = False
         
      flags = interaction.author.public_flags.all()
      flags = str(flags).replace("[", "").replace("]", "")
      embed = disnake.Embed(
         title="Userinfo!",
         description=userinfo.format(
            username=user.name,
            userid=user.id,
            nickname=user.nick or "None",
            joindate=user.joined_at.strftime("%A %b %d, %Y"),
            accountcreatedat=user.created_at.strftime("%A %B %d, %Y"),
            boostingguild=boosting,
            flags=flags,
            isbotaccount=bot,
            animatedavatar=user.avatar.is_animated(),
            toprole=user.top_role.mention,
            roles=roles,
         ),
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      embed.set_image(
         url=user.avatar.url
      )
      
      await send(interaction=interaction, embed=embed)