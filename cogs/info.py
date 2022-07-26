"""
Contains all information commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
from typing import Optional


import disnake
from disnake.ext import commands


from utils.color import color
 



serverinfo = """
**Server Name:** `{servername}`
**Server Id:** `{serverid}`

**Description:** `{description}`

**Emojis:** `{emojis}`
**Stickers:** `{stickers}`
**AFK Timeout:** `{afktimeout}`
**AFK Channel:** `{afkchannel}`
**Owner:** {owner}
**Guild Unavailable?:** `{guildunavailable}`
**Max Presences:** `{maxpresences}`
**Max Members:** `{maxmembers}`
**Large Guild?:** `{largeguild}`
**Max Video Channel Users:** `{maxvideochannels}`
**Two Factor Authentication:** `{mfalevel}`
**Verification Level:** `{verification}`
**Explicit Content Filter:** `{explicitcontentfilter}`
**Default Notification:** `{defaultnotification}`
**Guild Features:** `{features}`
**Boost Progress Bar Enabled?**: `{boostprogressbar}`
**Guild Boost Tier:** `{boosttier}`
**Boosts:** `{boosts}`
**Preferred Language:** `{preferredlanguage}`
**NSFW Level:** `{nsfwlevel}`
**Widget Enabled?:** `{widgetenabled}`
**Vanity URL Code:** `{vanityurlcode}`

**Server Channel Info**
**Rules Channel:** `{ruleschannel}`
**Welcome Channel:** `{welcomechannel}`
**Total Categories:** `{totalcategories}`
**Total Channels (All):** `{totalchannels}`
**Total Text Channels:** `{totaltextchannels}`
**Total Voice Channels:** `{totalvoicechannels}`
**Total Thread Channels:** `{totalthreadchannels}`
**Total Announcement Channels:** `{totalannouncementchannels}`

**Server Role Info**
**Default Role:** `{defaultrole}`
**Total Roles:** `{totalroles}`
**Assignable Roles:** `{assignableroles}` 
**Bot Roles:** `{botroles}`
"""


class Info(commands.Cog, name="Info Cmds"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
   

   
   @commands.slash_command(
      name="firstmessage",
      description="gets the first message in a channel",
   )
   async def firstmessage(self, interaction):
      first_message = (await interaction.channel.history(limit = 1, oldest_first = True).flatten())[0]
      
      embed = disnake.Embed(
         title="First Message!",
         description=first_message.jump_url,
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      
      await send(interaction=interaction, embed=embed)
      
      
      
   @commands.slash_command(
      name="todo",
      description="See The Todo List For This Bot",
   )
   async def todo(self, interaction):
      with open("./todo.txt", "r") as f:
         todo = f.read()
      embed = disnake.Embed(
         title="Todo List!",
         description=todo,
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await send(interaction=interaction, embed=embed)
   
   
   
   @commands.slash_command(
      name="pfp",
      description="gets a user's profile picture",
   )
   async def pfp(self, interaction,
                 user: Optional[disnake.User] = None
                 ):
      if user is None:
         url = interaction.author.avatar.url 
      if user is not None:
         url = user.avatar.url  
      embed = disnake.Embed(
         title="Profile Picture!",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      embed.set_image(
         url=url
      )
      await send(interaction=interaction, embed=embed)
      
      
      
   @commands.slash_command(
      name="serverinfo",
      description="gets a server's information",
   )
   async def serverinfo(self, interaction):
      guild = await self.bot.fetch_guild(interaction.guild.id)
      maxmembers = guild.max_members
      
      twofacorauthentication=interaction.guild.mfa_level  
      explicitcontentfilter=interaction.guild.explicit_content_filter
      explicitcontentfilter=str(explicitcontentfilter).replace("all_members", "All Members").replace("disabled", "Disabled").replace("no_role", "No Role")
      nsfwlevel=interaction.guild.nsfw_level
      nsfwlevel=str(nsfwlevel).replace("NSFWLevel.", "").replace("default", "Default").replace("explicit", "Explicit").replace("safe", "Safe").replace("age_restricted", "Age Restricted")
      features=interaction.guild.features
      features=str(features).replace("]", "").replace("[", "").replace("'", "")
      
      newschannels = 0
      for channel in interaction.guild.text_channels:
         channelnews = channel.is_news()
         if channelnews == True:
            newschannels += 1
      
      assignableroles = 0
      botroles = 0
      for roles in interaction.guild.roles:
         rolesassignable = roles.is_assignable()
         if rolesassignable == True:
            assignableroles += 1
         else:
            botroles += 1
      
      embed = disnake.Embed(
         title="Serverinfo!",
         description=serverinfo.format(
            servername=interaction.guild.name, 
            serverid=interaction.guild.id, 
            description=interaction.guild.description,
            emojis=len(interaction.guild.emojis),
            stickers=len(interaction.guild.stickers),
            afktimeout=interaction.guild.afk_timeout,
            afkchannel=interaction.guild.afk_channel,
            owner=interaction.guild.owner.mention,
            guildunavailable=interaction.guild.unavailable,
            maxpresences=guild.max_presences,
            maxmembers=maxmembers,
            largeguild=interaction.guild.large,
            maxvideochannels=guild.max_video_channel_users,
            mfalevel=twofacorauthentication,
            verification=interaction.guild.verification_level,
            explicitcontentfilter=explicitcontentfilter,
            defaultnotification=interaction.guild.default_notifications,
            features=features,
            boostprogressbar=interaction.guild.premium_progress_bar_enabled,
            boosttier=interaction.guild.premium_tier,
            boosts=interaction.guild.premium_subscription_count,
            preferredlanguage=interaction.guild.preferred_locale,
            nsfwlevel=nsfwlevel,
            widgetenabled=interaction.guild.widget_enabled,
            vanityurlcode=interaction.guild.vanity_url_code,
            ruleschannel=interaction.guild.rules_channel or "No Rules Channel",
            welcomechannel=interaction.guild.system_channel.mention or "No Welcome Channel",
            totalcategories=len(interaction.guild.categories),
            totalchannels=len(interaction.guild.channels),
            totaltextchannels=len(interaction.guild.text_channels),
            totalvoicechannels=len(interaction.guild.voice_channels),
            totalthreadchannels=len(interaction.guild.threads),
            totalannouncementchannels=newschannels,
            defaultrole=interaction.guild.default_role.mention,
            totalroles=len(interaction.guild.roles),
            assignableroles=assignableroles,
            botroles=botroles,
         ),
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await send(interaction=interaction, embed=embed)
      
      
      
   @commands.slash_command(
      name="getauditlogs",
      description="gets the recent audit logs for a server",
   )
   @commands.has_permissions(administrator=True)
   async def getauditlogs(self, interaction: disnake.ApplicationCommandInteraction):
      embed = disnake.Embed(
            title="Logs!",
            color=color,
            timestamp=disnake.utils.utcnow(),
         )
      async for entry in interaction.guild.audit_logs(limit=100):
         embed.add_field(
            inline=False, 
            name="Logs",
            value=f"```{entry.user} did {entry.action} to {entry.target}```",
         )
      await send(interaction=interaction, embed=embed)