# Imports
import disnake
from disnake import Option, OptionType, ApplicationCommandInteraction
from disnake.ext import commands



from helpers.color import color
from helpers.message import interactionsend



appinfo = """
**App Name:** `{appname}`
**App Id:** `{appid}`
**Bot Name:** `{botname}`
**Bot Id:** `{botid}`
**Public Bot:** `{publicbot}`
**Requires Bot Code Grant:** `{codegrant}`
**Terms Of Service URL:** `{tosurl}`
**Privacy Policy URL:** `{ppurl}`
**Bot Invite URL: ** {inviteurl}

**App Flags:** \n`{appflags}`

**App Tags:** \n`{apptags}`
"""



userinfo = """
**User Name:** `{username}`
**User Id:** `{userid}`
**Nickname?:** `{nickname}`
**Joined At:** `{joindate}`
**Account Created At:** `{accountcreatedat}`
**Is Boosting Guild?:** `{boostingguild}`
**Public Flags:** `{publicflags}`

**Is Bot Account?:** `{isbotaccount}`
**Animated Avatar?:** `{animatedavatar}`
**Top Role:** {toprole}
**Roles:** \n{roles}
"""



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



# Class Info
class Info(commands.Cog, name="Info Cmds"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
   
   
   
   # Commands
   @commands.slash_command(
      name="appinfo",
      description="shows info about the bot",
   )
   async def appinfo(self, interaction):
      app = await self.bot.application_info()
      appflags=f"""Gateway Presence: {app.flags.gateway_presence}
Gateway Presence Limited: {app.flags.gateway_presence_limited}
Gateway Guild Members: {app.flags.gateway_guild_members}
Verificaiton Pending Guild Limit: {app.flags.verification_pending_guild_limit}
Embedded: {app.flags.embedded}
Gateway Message Content: {app.flags.gateway_message_content}
Gateway Message Content Limited: {app.flags.gateway_message_content_limited}"""
      apptag=str(app.tags)
      apptags=apptag.replace("[", "").replace("]", "").replace("'", "")
      embed = disnake.Embed(
         title="Appinfo",
         description=appinfo.format(
            appname=app.name,
            appid=app.id,
            botname=self.bot.user.name, 
            botid=self.bot.user.id,
            publicbot=app.bot_public,
            codegrant=app.bot_require_code_grant,
            tosurl=app.terms_of_service_url,
            ppurl=app.privacy_policy_url,
            inviteurl="[Invite](https://discord.com/api/oauth2/authorize?client_id=938579223780655145&permissions=8&scope=bot%20applications.commands)",
            appflags=appflags,
            apptags=apptags,
            ),
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author),
      )
      await interactionsend(interaction=interaction, embed=embed)
      
      
      
   @commands.slash_command(
      name="userinfo",
      description="gets a user's information",
      options=[
         Option(
            name="user",
            description="user to get info about",
            type=OptionType.user, 
            required=True,
         )
      ]
   )
   async def userinfo(self, interaction, user: disnake.User = None):
      if user.bot == True:
         bot = "Is Bot Account"
      else:
         bot = "Isn't Bot Account"
      roles = [role.mention for role in user.roles]
      roles = str(roles).replace("]", "").replace("[", "").replace("'", "")
      embed = disnake.Embed(
         title="Userinfo",
         description=userinfo.format(
            username=user.name,
            userid=user.id,
            nickname=user.nick or "None",
            joindate=user.joined_at.strftime("%A %b %d, %Y"),
            accountcreatedat=user.created_at.strftime("%A %B %d, %Y"),
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
      
      await interactionsend(interaction=interaction, embed=embed)


   
   @commands.slash_command(
      name="firstmessage",
      description="gets the first message in a channel",
   )
   async def firstmessage(self, interaction):
      first_message = (await interaction.channel.history(limit = 1, oldest_first = True).flatten())[0]
      
      embed = disnake.Embed(
         title="First Message",
         description=first_message.jump_url,
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      
      await interactionsend(interaction=interaction, embed=embed)
      
      
      
   @commands.slash_command(
      name="todo",
      description="See The Todo List For This Bot",
   )
   async def todo(self, interaction):
      with open("./todo.txt", "r") as f:
         todo = f.read()
      embed = disnake.Embed(
         title="Todo List",
         description=todo,
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      await interactionsend(interaction=interaction, embed=embed)
   
   
   
   @commands.slash_command(
      name="pfp",
      description="gets a user's profile picture",
      options=[
         Option(
            name="user",
            description="user to get pfp of",
            type=OptionType.user,
            required=False
         )
      ],
   )
   async def pfp(self, interaction, user: disnake.User = None):
      if user is None:
         url = interaction.author.avatar.url 
      if user is not None:
         url = user.avatar.url  
      embed = disnake.Embed(
         title="Profile Picture",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author)
      )
      embed.set_image(
         url=url
      )
      await interactionsend(interaction=interaction, embed=embed)
      
      
      
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
         title="Serverinfo",
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
      await interactionsend(interaction=interaction, embed=embed)
      
      
      
   @commands.slash_command(
      name="getauditlogs",
      description="gets the recent audit logs for a server",
   )
   @commands.has_permissions(administrator=True)
   async def getauditlogs(self, interaction: ApplicationCommandInteraction):
      embed = disnake.Embed(
            title="Logs",
            color=color,
            timestamp=disnake.utils.utcnow(),
         )
      async for entry in interaction.guild.audit_logs(limit=100):
         embed.add_field(
            inline=False, 
            name="Logs",
            value=f"```{entry.user} did {entry.action} to {entry.target}```",
         )
      await interactionsend(interaction=interaction, embed=embed)