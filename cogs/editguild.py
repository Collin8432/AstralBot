"""
Contains edit guild command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands


from typing import Optional


from utils.message import send


class Editguild(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
      
      
   @commands.slash_command(
      name="editguild",
      description="edits the guild",
   )
   @commands.has_permissions(administrator=True)
   async def editguild(self, 
      interaction: ApplicationCommandInteraction,
      name: Optional[str] = None, 
      reason: Optional[str] = None, 
      description: Optional[str] = None, 
      icon: Optional[disnake.Attachment] = None, 
      banner: Optional[disnake.Attachment] = None, 
      splash: Optional[disnake.Attachment] = None, 
      discovery_splash: Optional[disnake.Attachment] = None, 
      community: Optional[bool] = None, 
      afk_channel: Optional[disnake.TextChannel] = None, 
      owner: Optional[disnake.User] = None, 
      afk_timeout: Optional[int] = None, 
      default_notifications: Optional[disnake.NotificationLevel] = None, 
      verification_level: Optional[disnake.VerificationLevel] = None, 
      explicit_content_filter: Optional[disnake.ContentFilter] = None, 
      vanity_code: Optional[str] = None, 
      system_channel: Optional[disnake.TextChannel] = None,
      # system_channel_flags: Optional[disnake.SystemChannelFlags] = None, 
      # preferred_locale: Optional[disnake.Locale] = None, 
      rules_channel: Optional[disnake.TextChannel] = None, 
      public_updates_channel: Optional[disnake.TextChannel] = None, 
      premium_progress_bar_enabled: Optional[bool] = None
      ):
      """_summary_

      Args:
         interaction (ApplicationCommandInteraction): _description_
         name (Optional[str], optional): _description_. Defaults to None.
         reason (Optional[str], optional): _description_. Defaults to None.
         description (Optional[str], optional): _description_. Defaults to None.
         icon (Optional[disnake.Attachment], optional): _description_. Defaults to None.
         banner (Optional[disnake.Attachment], optional): _description_. Defaults to None.
         splash (Optional[disnake.Attachment], optional): _description_. Defaults to None.
         discovery_splash (Optional[disnake.Attachment], optional): _description_. Defaults to None.
         community (Optional[bool], optional): _description_. Defaults to None.
         afk_channel (Optional[disnake.TextChannel], optional): _description_. Defaults to None.
         owner (Optional[disnake.User], optional): _description_. Defaults to None.
         afk_timeout (Optional[int], optional): _description_. Defaults to None.
         default_notifications (Optional[disnake.NotificationLevel], optional): _description_. Defaults to None.
         verification_level (Optional[disnake.VerificationLevel], optional): _description_. Defaults to None.
         explicit_content_filter (Optional[disnake.ContentFilter], optional): _description_. Defaults to None.
         vanity_code (Optional[str], optional): _description_. Defaults to None.
         system_channel (Optional[disnake.TextChannel], optional): _description_. Defaults to None.
         # system_channel_flags (Optional[disnake.SystemChannelFlags], optional): _description_. Defaults to None.
         # preferred_locale (Optional[disnake.Locale], optional): _description_. Defaults to None.
         rules_channel (Optional[disnake.TextChannel], optional): _description_. Defaults to None.
         public_updates_channel (Optional[disnake.TextChannel], optional): _description_. Defaults to None.
         premium_progress_bar_enabled (Optional[bool], optional): _description_. Defaults to None.
      """
      await interaction.guild.edit(
         reason=reason,
         name=name, 
         description=description, 
         icon=icon, 
         banner=banner, 
         splash=splash, 
         discovery_splash=discovery_splash, 
         community=community, 
         afk_channel=afk_channel, 
         owner=owner, 
         afk_timeout=afk_timeout, 
         default_notifications=default_notifications, 
         verification_level=verification_level, 
         explicit_content_filter=explicit_content_filter, 
         vanity_code=vanity_code, 
         system_channel=system_channel, 
         # system_channel_flags=system_channel_flags, 
         # preferred_locale=preferred_locale, 
         rules_channel=rules_channel, 
         public_updates_channel=public_updates_channel, 
         premium_progress_bar_enabled=premium_progress_bar_enabled
         )
      await send(interaction=interaction, msg="Edited Guild", ephemeral=True)