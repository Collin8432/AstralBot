import disnake
from disnake.ext import commands, tasks
from disnake import ApplicationCommandInteraction
from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb
from PIL import Image, ImageDraw, ImageFont
import os
import random
from helpers.database import on_join_insert, on_leave_remove


class Events(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot


   @tasks.loop(minutes=1.0)
   async def status_task(self) -> None:
      statuses = [f"Watching Over {len(self.bot.guilds)} Servers"]
      await self.bot.change_presence(activity=disnake.Game(random.choice(statuses)))
      channel = await self.bot.fetch_channel(975404941919260672)
      member = channel.guild.member_count
      await channel.edit(name=f"Members: {member}")

   @commands.Cog.listener()
   async def on_ready(self):
      print(f"Logged in as {self.bot.user.name}")
      


   @commands.Cog.listener()
   async def on_slash_command(self, interaction):
      await webhooksend(f"Command Executed", f"**<@{interaction.author.id}>** Executed /**{interaction.data.name}** in <#{interaction.channel.id}>", f"{interaction.guild.id}")

   @commands.Cog.listener()
   async def on_slash_command_error(self, interaction: ApplicationCommandInteraction, error: Exception) -> None:
      embed = disnake.Embed(
         title="Error",
         description=f"Error With Command:\n```py\n{error}```",
         color=0xDC143C,
         timestamp=disnake.utils.utcnow()
      )
      try:
         await interaction.response.defer()
         await interaction.edit_original_message(embed=embed, ephemeral=True)
      except:
         await interaction.send(embed=embed, ephemeral=True)
      else:
         pass

   @commands.Cog.listener("on_message")
   async def on_message(self, message):
      botids = [938579223780655145]
      if "nigger" in message.content and message.guild.id == 944297787779072020 and message.author.id not in botids:
         await message.reply("Please Don't Say That")
         await message.delete()
         await webhooksend("N-Word Logged", f"<@{message.author.id}> Sent An N-Word In <#{message.channel.id}>\n **Content:** \n{message.content}", f"{message.guild.id}")
      if message.channel.id == 970325969359503460 and message.author.id not in botids:
         await message.author.edit(nick=f"{message.content}")
         embed = disnake.Embed(
               title=f"Nickname Changed!",
               description=f"<@{message.author.id}> Changed Nickname To: {message.content}",
               color=0xDC143C,
               timestamp=disnake.utils.utcnow()
         )
         embed.set_image(url=message.author.display_avatar)
         await message.reply(embed=embed)

   @commands.Cog.listener()
   async def on_message_delete(self, message):
      await webhooksend("Message Deleted", f"Chat Deleted In <#{message.channel.id}>\n**Author:** \n<@{message.author.id}>\n**Content:** \n{message.content}", f"{message.guild.id}")

   @commands.Cog.listener()
   async def on_member_ban(self, guild, user):
      await webhooksend("Member Banned", f"<@{user.id}> Was Banned From Astral", f"{guild.id}")
      embed = disnake.Embed(
         title="You Were Banned From Astral",
         description=f"<@{user.id}> Was Banned From Astral",
         color=0xDC143C,
         timestamp=disnake.utils.utcnow()
      ) 
      await user.send(embed=embed)   

   @commands.Cog.listener()
   async def on_member_unban(self, guild, user):
      await webhooksend("Member Unbanned", f"<@{user.id}> Was Unbanned From Astral", f"{guild.guild.id}")
      embed = disnake.Embed(
         title="You Were Unbanned From Astral",
         description=f"<@{user.id}> Was Unbanned From Astral\nhttps://discord.gg/uNnJyjaG",
         color=0xDC143C,
         timestamp=disnake.utils.utcnow()
      )
      await user.send(embed=embed)

   @commands.Cog.listener()
   async def on_presence_update(self, before, after):
      if before.status != after.status and after.id != 935339228324311040:
         await webhooksend("Presence Changed", f"<@{after.id}> Changed Status \n**From:**\n{before.status}\n**To:**\n{after.status}", f"{after.guild.id}")
      if before.activity != after.activity and after.id != 935339228324311040:
         await webhooksend("Activity Changed", f"<@{after.id}> Changed Activity \n**From:**\n{before.activity}\n**To:**\n{after.activity}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_member_update(self, before, after):
      if before.display_name != after.display_name:
         await webhooksend("Display Name Changed", f"<@{after.id}> **Changed Name**\n**From:**\n{before.display_name}\n**To:**\n{after.display_name}", f"{after.guild.id}")
      if before.roles != after.roles:
         roles = [role.mention for role in before.roles]
         roles2 = [role.mention for role in after.roles]
         beforeroles = str(roles).replace("]", "").replace("[", "").replace("'", "")
         afterroles = str(roles2).replace("]", "").replace("[", "").replace("'", "")
         await webhooksend(f"Roles Changed", f"<@{after.id}> Roles Changed\n**Before:**\n{beforeroles}\n**After:**\n{afterroles}", f"{after.guild.id}")
      if before.current_timeout != after.current_timeout:
         await webhooksend(f"Timeout!", f"<@{after.id}> Timeout Changed\n**Before:**\n{before.current_timeout}\n**After:**\n{after.current_timeout}", f"{after.guild.id}")



   @commands.Cog.listener()
   async def on_user_update(self, before, after):
      if before.display_avatar != after.display_avatar:
         await webhooksend(f"Avatar Changed", f"<@{after.member.id}> Avatar Changed\n**Before:**\n{before.display_avatar}\n**After:**\n{after.display_avatar}", f"{after.guild.id}")
      if before.discriminator != after.discriminator:
         await webhooksend(f"Discriminator Changed", f"<@{after.member.id}> Discriminator Changed\n**Before:**\n{before.discriminator}\n**After:**\n{after.discriminator}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_member_join(self, member):
      guild = member.guild
      if guild.system_channel is not None:
            img = Image.open("./img/astral.png")
            image = ImageDraw.Draw(img)
            font = ImageFont.truetype("./font/MomB.ttf", 30)
            image.text((160, 275), f"Welcome,", font=font, fill=(43,22,197))
            image.text((160, 325), f"{member.name}", font=font, fill=(43,22,197))
            list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            randomnumber = ""
            for i in range(5, 15):
                  randomnumber += (random.choice(list))
                  continue
            img.save(f"./img/astral{randomnumber}.png")
            imgfile = disnake.File(f"./img/astral{randomnumber}.png") 
            await guild.system_channel.send(file=imgfile)
            await webhooksend("Member Joined", f"<@{member.id}> Joined Astral", f"{member.guild.id}")

   @commands.Cog.listener()
   async def on_member_remove(self, member):
      await webhooksend("Member Left", f"<@{member.id}> Left Astral", f"{member.guild.id}")
      embed = disnake.Embed(
         title=f"{member.name}, Sorry Too See You Go!",
         description=f"If you left on accident, please join back!\nhttps://discord.gg/uNnJyjaG",
         color=0xDC143C,
         timestamp=disnake.utils.utcnow()
      )
      try:
         await member.send(embed=embed)
      except disnake.Forebidden:
         pass

      
   @commands.Cog.listener()
   async def on_guild_join(self, guild):
      await on_join_insert(guild.name, guild.id)

   @commands.Cog.listener()
   async def on_guild_remove(self, guild):
      await on_leave_remove(guild.id)

   @commands.Cog.listener()
   async def on_guild_channel_delete(self, channel):
      await webhooksend("Channel Deleted", f"{channel.name} **Was Deleted**", f"{channel.guild.id}")

   @commands.Cog.listener()
   async def on_guild_channel_create(self, channel):
      await webhooksend("Channel Created", f"{channel.mention} **Was Created**", f"{channel.guild.id}")

   @commands.Cog.listener()
   async def on_guild_channel_update(self, before, after):
      if before.name != after.name:
         await webhooksend("Channel Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.mention}", f"{after.guild.id}")
      if before.changed_roles != after.changed_roles:

         await webhooksend("Channel Roles Changed", f"**From:**\n{before.changed_roles}\n**To:**\n{after.changed_roles}\n\n//idek what this does", f"{after.guild.id}")
      roles = after.guild.roles
      for role in roles:
         if dict(after.overwrites_for(role)) != dict(before.overwrites_for(role)):
               permissions = dict(after.overwrites_for(role))
               finalpermissions = (str(permissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
               await webhooksend("Channel Permissions Changed", f"\n**Channel Permissions Changed For** {role.mention} **In** {after.mention}\n```\n{finalpermissions}```", f"{after.guild.id}")
      members = after.guild.members  
      for member in members:
         if dict(after.overwrites_for(member)) != dict(before.overwrites_for(member)):
               permissions = dict(after.overwrites_for(member))
               finalpermissions = (str(permissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
               await webhooksend("Channel Permissions Changed", f"\n**Channel Permissions Changed For** {member.mention} **In** {after.mention}\n```\n{finalpermissions}```", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_guild_update(self, before, after):
      if before.name != after.name:
         await webhooksend("Guild Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}", f"{after.guild.id}")
      if before.afk_timeout != after.afk_timeout:
         await webhooksend("Guild AFK Timeout Changed", f"**From:**\n{before.afk_timeout}\n**To:**\n{after.afk_timeout}", f"{after.guild.id}")
      if before.afk_channel != after.afk_channel:
         await webhooksend("Guild AFK Channel Changed", f"**From:**\n{before.afk_channel}\n**To:**\n{after.afk_channel}", f"{after.guild.id}")
      if before.owner_id != after.owner_id:
         await webhooksend("Guild Owner Changed", f"**From:**\n{before.owner.mention}\n**To:**\n{after.owner.mention}", f"{after.guild.id}")
      if before.description != after.description:
         await webhooksend("Guild Description Changed", f"**From:**\n{before.description}\n**To:**\n{after.description}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_guild_role_create(self, role):
      await webhooksend("Role Created", f"{role.mention} **Was Created**", f"{role.guild.id}")

   @commands.Cog.listener()
   async def on_guild_role_delete(self, role):
      await webhooksend("Role Deleted", f"{role.name} **Was Deleted**", f"{role.guild.id}")

   @commands.Cog.listener()
   async def on_guild_role_update(self, before, after):
      if before.name != after.name:
         await webhooksend("Role Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}", f"{after.guild.id}")
      if before.color != after.color:
         await webhooksend("Role Color Changed", f"**From:**\n{before.color}\n**To:**\n{after.color}", f"{after.guild.id}")
      if before.hoist != after.hoist:
         await webhooksend("Role Hoist Changed", f"**From:**\n{before.hoist}\n**To:**\n{after.hoist}", f"{after.guild.id}")
      if before.mentionable != after.mentionable:
         await webhooksend("Role Mentionable Changed", f"**From:**\n{before.mentionable}\n**To:**\n{after.mentionable}", f"{after.guild.id}")
      if before.permissions != after.permissions:
         if dict(before.permissions) != dict(after.permissions):
               afterpermissions = dict(after.permissions)
               finalpermissions = (str(afterpermissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
               await webhooksend("Role Permissions Changed", f"{after.mention}'s **Permissions Updated To:**```\n{finalpermissions}```", f"{after.guild.id}")
      if before.position != after.position:
         await webhooksend("Role Position Changed", f"**From:**\n{before.position}\n**To:**\n{after.position}", f"{after.guild.id}")

   
   @commands.Cog.listener()
   async def on_guild_emojis_update(self, before, after):
      if before.name != after.name:
         await webhooksend("Emoji Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_voice_state_update(self, member, before, after):
      if before.channel != after.channel:
         if after.channel == None:
               await webhooksend("Member Left Voice Channel", f"{member.mention} **Left** {before.channel.mention}", f"{after.guild.id}")
         else:
               await webhooksend("Member Joined Voice Channel", f"{member.mention} **Joined** {after.channel.mention}", f"{after.guild.id}")
         if before.deaf != after.deaf:
               if after.deaf:
                  await webhooksend("Member Deafened", f"{member.mention} **Was Server Deafened**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Un-Deafened", f"{member.mention} **Was Server Un-Deafened**", f"{after.guild.id}")
         if before.mute != after.mute:
               if after.mute:
                  await webhooksend("Member Muted", f"{member.mention} **Was Server Muted**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Un-Muted", f"{member.mention} **Was Server Un-Muted**", f"{after.guild.id}")
         if before.self_deaf != after.self_deaf:
               if after.self_deaf:
                  await webhooksend("Member Self Deafened", f"{member.mention} **Has Self Deafened**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Self Un-Deafened", f"{member.mention} **Has Self Un-Deafened**", f"{after.guild.id}")
         if before.self_mute != after.self_mute:
               if after.self_mute:
                  await webhooksend("Member Self Muted", f"{member.mention} **Has Self Muted**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Self Un-Muted", f"{member.mention} **Has Self Un-Muted**", f"{after.guild.id}")
         if before.self_stream != after.self_stream:
               if after.self_stream:
                  await webhooksend("Member Streamed", f"{member.mention} **Is Streaming**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Stopped Streaming", f"{member.mention} **Stopped Streaming**", f"{after.guild.id}")
         if before.self_video != after.self_video:
               if after.self_video:
                  await webhooksend("Member Started Showing Video", f"{member.mention} **Started Showing Video**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Stopped Showing Video", f"{member.mention} **Stopped Showing Video**", f"{after.guild.id}")
         if before.suppress != after.suppress:
               if after.suppress:
                  await webhooksend("Member Suppressed", f"{member.mention} **Was Suppressed**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Un-Suppressed", f"{member.mention} **Has Been Un-Suppressed**", f"{after.guild.id}")
         if before.requested_to_speak_at != after.requested_to_speak_at:
               if after.requested_to_speak_at:
                  await webhooksend("Member Requested To Speak", f"{member.mention} **Requested To Speak**", f"{after.guild.id}")
               else:
                  await webhooksend("Member Stopped Requesting To Speak", f"{member.mention} **Stopped Requesting To Speak**", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_guild_scheduled_event_create(self, event):
      await webhooksend("Scheduled Event Created", f"**{event.name} Was Created**\n**Description:**\n{event.description}\n**Start:**\n{event.scheduled_start_time}\n**End:**\n{event.scheduled_end_time}\n**Event Channel:**\n{event.channel.mention}", f"{event.guild.id}")

   @commands.Cog.listener()
   async def on_guild_scheduled_event_delete(self, event):
      await webhooksend("Scheduled Event Deleted", f"**{event.name} Was Deleted**", f"{event.guild.id}")

   @commands.Cog.listener()
   async def on_guild_scheduled_event_update(self, before, after):
      if before.name != after.name:
         await webhooksend("Scheduled Event Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}", f"{after.guild.id}")
      if before.description != after.description:
         await webhooksend("Scheduled Event Description Changed", f"**From:**\n{before.description}\n**To:**\n{after.description}", f"{after.guild.id}")
      if before.scheduled_start_time != after.scheduled_start_time:
         await webhooksend("Scheduled Event Start Changed", f"**From:**\n{before.scheduled_start_time}\n**To:**\n{after.scheduled_start_time}", f"{after.guild.id}")
      if before.scheduled_end_time != after.scheduled_end_time:
         await webhooksend("Scheduled Event End Changed", f"**From:**\n{before.scheduled_end_time}\n**To:**\n{after.scheduled_end_time}", f"{after.guild.id}")
      if before.channel != after.channel:
         await webhooksend("Scheduled Event Channel Changed", f"**From:**\n{before.channel.mention}\n**To:**\n{after.channel.mention}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_stage_instance_create(self, stage_instance):
      await webhooksend("Stage Instance Created", f"**{stage_instance.name} Was Created**\n**Topic:**\n{stage_instance.Topic}\n**Stage Instance Channel:**\n{stage_instance.channel.mention}"), f"{stage_instance.guild.id}"

   @commands.Cog.listener()
   async def on_stage_instance_delete(self, stage_instance):
      await webhooksend("Stage Instance Deleted", f"**{stage_instance.name} Was Deleted**", f"{stage_instance.guild.id}")

   @commands.Cog.listener()
   async def on_stage_instance_update(self, before, after):
      if before.name != after.name:
         await webhooksend("Stage Instance Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}", f"{after.guild.id}")
      if before.topic != after.topic:
         await webhooksend("Stage Instance topic Changed", f"**From:**\n{before.topic}\n**To:**\n{after.topic}", f"{after.guild.id}")
      if before.channel != after.channel:
         await webhooksend("Stage Instance Channel Changed", f"**From:**\n{before.channel.mention}\n**To:**\n{after.channel.mention}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_invite_create(self, invite):
      if invite.max_age == 0:
         inviteage = "Never"
      else:
         inviteage = f"{invite.max_age}"
      if invite.max_uses == 0:
         inviteuses = "Unlimited"
      else:
         inviteuses = f"{invite.max_uses}"
      await webhooksend("Invite Created", f"**Invite Created By:**\n{invite.inviter.mention}\n**Invite Age:**\n{inviteage}\n**Possible Uses:**\n{inviteuses}\n**Invite Code:**\n{invite.code}\n**Temporary Membership?**\n{invite.temporary}\n**Invite Channel:**\n{invite.channel.mention}\n**Expires At:**\n{invite.expires_at}", f"{invite.guild.id}")

   @commands.Cog.listener()
   async def on_invite_delete(self, invite):
      await webhooksend("Invite Deleted", f"**Invite Created By:**\n{invite.inviter.mention}\n**Invite Code:**\n{invite.code}", f"{invite.guild.id}")

   @commands.Cog.listener()
   async def on_group_join(self, channel, user):
      await webhooksend("Group Joined", f"**{user.mention} **Joined** {channel.mention}**", f"{channel.guild.id}")

   @commands.Cog.listener()
   async def on_group_remove(self, channel, user):
      await webhooksend("Group Left", f"**{user.mention} **Left** {channel.mention}", f"{channel.guild.id}")



   @commands.Cog.listener()
   async def on_shard_connect(self, shard_id):
      pass

 
   async def on_shard_disconnect(self, shard_id):
      pass

   @commands.Cog.listener()
   async def on_shard_ready(self, shard_id):
      pass


   @commands.Cog.listener()
   async def on_shard_resumed(self, shard_id):
      pass


   @commands.Cog.listener()
   async def on_socket_event_type(self, event_type):
      pass

   @commands.Cog.listener()
   async def on_typing(self, channel, user, when):
      pass

   @commands.Cog.listener()
   async def on_bulk_message_delete(self, messages):
      await webhooksend("Messages Bulk Deleted/Purged", f"**Messages Bulk Deleted/Purged With A Total Of {len(messages)} Messages Deleted**", f"{self.bot.guild.id}")

   @commands.Cog.listener()
   async def on_message_edit(self, before, after):
      if before.content != after.content:
         await webhooksend("Message Edited", f"**From:**\n{before.content}\n**To:**\n{after.content}", f"{after.guild.id}")

   @commands.Cog.listener()
   async def on_reaction_add(self, reaction, user):
      await webhooksend("Reaction Added", f"{reaction.emoji} **Was Added To** {reaction.message.content} **In** {reaction.message.channel.mention} **By** {user.mention}", f"{user.guild.id}")

   @commands.Cog.listener()
   async def on_reaction_remove(self, reaction, user):
      await webhooksend("Reaction Removed", f"{reaction.emoji} **Was Removed From** {reaction.message.content} **In** {reaction.message.channel.mention} **By** {user.mention}", f"{user.guild.id}")



def setup(bot):
   bot.add_cog(Events(bot))