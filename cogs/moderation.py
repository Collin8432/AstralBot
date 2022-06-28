# Imports
from re import M
import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, OptionType



 
from helpers import checks
from helpers.webhook import webhooksend
from helpers.db import *
from helpers.color import color
from helpers.message import interactionsend



# Moderator Application Modal
class ModApp(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="What Are You Applying For?",
                placeholder="Ex. Mod, Moderator, etc...",
                custom_id="ApplyingFor",
                style=disnake.TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="What Are You Experienced In?",
                placeholder="Ex. Discord",
                custom_id="Experience",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50
            ),
            disnake.ui.TextInput(
                label="Why Are You Better Than Others?",
                placeholder="Ex. I have a lot of experience in this role, I know how to do this, etc...",
                custom_id="BR",
                style=disnake.TextInputStyle.paragraph,
                min_length=20,
                max_length=500
            )
        ]
        super().__init__(title="Moderator Application", custom_id="ModApp", components=components)



    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        ApplyingFor = interaction.text_values["ApplyingFor"]
        Experience = interaction.text_values["Experience"]
        BR = interaction.text_values["BR"]
        await webhooksend("New Application", f"<@{interaction.author.id}> Submitted This Application \n**Appplying For:**\n{ApplyingFor}\n**Experience:**\n{Experience}\n**Why Are You Better Than Others For Your Role:**\n{BR}", f"{interaction.guild.id}")  
        await interactionsend(interaction=interaction, msg="Application Submitted Successfully!", ephemeral=True)
        
        
        
    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        await interactionsend(interaction=inter, msg=f"Error In Modal Interaction, {error}", ephemeral=True)



# Moderation Cog
class Moderation(commands.Cog, name="Mod Cmds"):
    def __init__(self, bot):
      self.bot = bot



    # Commands
    @commands.slash_command(
        name="kick",
        description="kicks a member from the server",
        options=[
            Option(
                name="user",
                description="the member you want to kick",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="reason to kick member",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(kick_members=True)
    @checks.not_blacklisted()
    async def kick(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                   reason: str = "Not specified") -> None:
        member = await interaction.guild.get_or_fetch_member(user.id)  
        if member.guild_permissions.administrator:  
            embed = disnake.Embed(
                title="Error!",
                description="User has Admin permissions.",
                color=0xE02B2B,
                timestamp=disnake.utils.utcnow()
            )
            await interactionsend(interaction=interaction, embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Member Kicked",
                    description=f"<@{member.id}> Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}",  
                    color=color,
                    timestamp=disnake.utils.utcnow()
                )
                await interactionsend(interaction=interaction, embed=embed)
                try:
                    embed = disnake.Embed(
                    title="You Were Kicked!",
                    description=f"<@{member.id}> Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}",  
                    color=color,
                    timestamp=disnake.utils.utcnow()
                    )
                    await member.send(embed=embed)  
                except disnake.Forbidden:
                    pass
                await member.kick(reason=reason)  
            except:
                embed = disnake.Embed(
                    title="Error",
                    description="Error While Kicking Member, Make Sure Member Does Not Have Higher Roles Than Me",
                    color=color,
                    timestamp=disnake.utils.utcnow()
                )
                await interactionsend(interaction=interaction, embed=embed)



    @commands.slash_command(
        name="ban",
        description="bans a member from the server",
        options=[
            Option(
                name="user",
                description="the member you want to ban",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="reason to ban member",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(ban_members=True)
    @checks.not_blacklisted()
    async def ban(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                  reason: str = "Not specified") -> None:
                  member = await interaction.guild.get_or_fetch_member(user.id)  
                  if member.guild_permissions.administrator:  
                      embed = disnake.Embed(
                          title="Error!",
                          description="User Has Administrator Permissions",
                          color=color,
                          timestamp=disnake.utils.utcnow()
                      )
                      await interactionsend(interaction=interaction, embed=embed)
                  else:
                      try:
                        embed = disnake.Embed(
                            title="Member Banned",
                            description=f"<@{member.id}> Was Banned By <@{interaction.author.id}>\n**Reason:**\n{reason}",  
                            color=color,
                            timestamp=disnake.utils.utcnow()
                        )
                        await interactionsend(interaction=interaction, embed=embed)
                        await member.ban(reason=reason)  
                      except:
                          embed = disnake.Embed(
                              title="Error!",
                              description="Error While Banning Member, Make Sure Member Does Not Have Higher Roles Than Me",
                              color=color,
                              timestamp=disnake.utils.utcnow()
                          )



    @commands.slash_command(
       name="moderatorapplication",
       description="sends a moderator appliction"
    )
    async def Appliction(interaction: disnake.CommandInteraction):  
      await interactionsend(interaction=interaction, modal=ModApp())



    @commands.slash_command(
        name="purge",
        description="purges all messages in a channel",
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(interaction: disnake.CommandInteraction):  
        embed = disnake.Embed(
            title="Messages Purged",
            description="Purged All Messages In This Channel",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        await interactionsend(interaction=interaction, embed=embed, ephemeral=True)
        await interaction.channel.purge(limit=200)



    @commands.slash_command(
        name="rules",
        description="sends basic rules",
    )
    @commands.has_permissions(administrator=True)
    async def rules(interaction):
        embed = disnake.Embed(
            title="Rules",
            description="1. Dont Be Annoying\n2. Dont Ask For Free Shit/Mod\n3. Be Smart With What You Say And Do\n4. Please Be Kind And Follow Discord TOS",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        await interactionsend(interaction=interaction, embed=embed)  



    @commands.slash_command(
        name="mute",
        description="mutes a member",
        options=[
            Option(
                name="user",
                description="the member you want to mute",
                type=OptionType.user,
                required=True
            ),
        ]
    )
    @commands.has_permissions(manage_roles=True)
    @checks.not_blacklisted()
    async def mute(self, interaction: ApplicationCommandInteraction, user: disnake.User) -> None:
        muterole = fetch_guild_information("guild_muterole", f"{interaction.guild.id}")
        muterole = interaction.guild.get_role(muterole)
        try:
            await user.add_roles(muterole)  
            embed = disnake.Embed(
                title="Member Muted",
                description=f"<@{user.id}> Was Muted By <@{interaction.author.id}>",
                color=color,
                timestamp=disnake.utils.utcnow()
            )
            embed.set_footer(
                text="Requested by {}".format(interaction.author)
            )
            await interactionsend(interaction=interaction, embed=embed)
        except Exception as e:
            embed = disnake.Embed(
                title="Error!",
                description=f"Error While Muting Member, Make Sure Member Does Not Have Higher Roles Than Me\n{e}",
                color=color,
                timestamp=disnake.utils.utcnow()
            )
            embed.set_footer(
                text="Requested by {}".format(interaction.author)
            )



    @commands.slash_command(
        name="unmute",
        description="unmutes a member",
        options=[
            Option(
                name="user",
                description="the member you want to unmute",
                type=OptionType.user,
                required=True
            ),
        ]
    )
    @commands.has_permissions(manage_roles=True)
    @checks.not_blacklisted()
    async def unmute(self, interaction: ApplicationCommandInteraction, user: disnake.User):
        muterole = fetch_guild_information("guild_muterole", f"{interaction.guild.id}")  
        muterole = interaction.guild.get_role(muterole)
        try:
            await user.remove_roles(muterole)
            embed = disnake.Embed(
                title="Member Unmuted",
                description=f"{user.mention} was unmuted by {interaction.author.mention}",
                color=color,
                timestamp=disnake.utils.utcnow(),
            )
            await interactionsend(interaction=interaction, embed=embed)
        except Exception as e:
            embed = disnake.Embed(
                title="Error!",
                description=f"Error While Unmuting Member, Make Sure Member Does Not Have Higher Roles Than Me\n{e}",
                color=color,
                timestamp=disnake.utils.utcnow(),
            )
            await interactionsend(interaction=interaction, embed=embed)
   

   
    @commands.slash_command(
        name="timeout",
        description="timeouts a member",
        options=[
            Option(
                name="user",
                description="The Member You Want To Timeout",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="time",
                description="The Timeout Time",
                type=OptionType.integer,
                required=True
            ),
            Option(
                name="reason",
                description="The Reason For Timeout",
                type=OptionType.string,
                required=False
            ),
        ]
    )
    @commands.has_permissions(manage_roles=True)
    @checks.not_blacklisted()
    async def timeout(self, interaction: ApplicationCommandInteraction, user: disnake.User, time: int, reason: str = None):
        await user.timeout(user, time=time)  
        embed = disnake.Embed(
            title="Member Timeout",
            description=f"<@{user.id}> Was Timeout By <@{interaction.author.id}>\n**Time:**\n{time}\n**Reason:**\n{reason}",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        await interactionsend(interaction=interaction, embed=embed)
        
        
    
    @commands.slash_command(
        name="editguild",
        description="edits the guild",
        options= [
            Option(
            name="reason",
            description="reason to edit the guild",
            type=OptionType.string,
            required=False
            ),
            Option(
                name="name",
                description="edits the guild's name",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="description",
                description="edits the guild's description",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="icon",
                description="edits the guild's icon",
                type=OptionType.attachment,
                required=False
            ),
            Option(
                name="banner",
                description="edits the guild's banner",
                type=OptionType.attachment,
                required=False
            ),
            Option(
                name="splash",
                description="edits the guild's splash",
                type=OptionType.attachment,
                required=False   
            ),
            Option(
                name="discovery_splash",
                description="edits the guild's discovery splash",
                type=OptionType.attachment,
                required=False
            ),
            Option(
                name="community",
                description="edits thew guild's community status",
                type=OptionType.boolean,
                required=False
            ),
            Option(
                name="afk_channel",
                description="edits the guild's afk channel",
                type=OptionType.channel,
                required=False
            ),
            Option(
                name="owner",
                description="edits the guild's owner",
                type=OptionType.user,
                required=False
            ),
            Option(
                name="afk_timeout",
                description="edits the guild's afk timeout",
                type=OptionType.integer,
                required=False
            ),
            Option(
                name="default_notifications",
                description="edits the guild's default notifications\nHint: all_messages, or only_mentions",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="verification_level",
                description="edits the guild's verification level\nHint: None, Low, Medium, High, Or Highest",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="explicit_content_filter",
                description="edits the guild's explicit content filter\nHint: disable, no_role, or all_members",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="vanity_code",
                description="edits the guild's vanity url",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="system_channel",
                description="edits the guild's system channel",
                type=OptionType.channel,
                required=False
            ),
            Option(
                name="preferred_locale",
                description="edits the guild's preferred locale\nHint: https://docs.disnake.dev/en/stable/api.html?highlight=edit#disnake.Locale",
                type=OptionType.string,
                required=False
            ),
            Option(
                name="rules_channel",
                description="edits the guild's rules channel",
                type=OptionType.channel,
                required=False
            ),
            Option(
                name="public_updates_channel",
                description="edits the guild's public updates channel",
                type=OptionType.channel,
                required=False
            ),
            Option(
                name="premium_progress_bar_enabled",
                description="edits the guild's premium progress bar status",
                type=OptionType.bool,
                required=False
            ),
        ]
    )
    @commands.has_permissions(Administrator=True)
    async def editguild(self, interaction: ApplicationCommandInteraction, reason: str = None, name: str = None, description: str = None, icon: bytes = None, banner: bytes = None, splash: bytes = None, discovery_splash: bytes = None, community: bool = None, afk_channel: disnake.TextChannel = None, owner: disnake.User = None, afk_timeout: int = None, default_notifications: disnake.NotificationLevel = None, verification_level: disnake.VerificationLevel = None, explicit_content_filter: disnake.ContentFilter = None, vanity_code: str = None, system_channel: disnake.TextChannel = None, preferred_locale: disnake.Locale = None, rules_channel: disnake.TextChannel = None, public_updates_channel: disnake.TextChannel = None, premium_progress_bar_enabled: bool = None):
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
            # system_channel_flags=..., 
            preferred_locale=preferred_locale, 
            rules_channel=rules_channel, 
            public_updates_channel=public_updates_channel, 
            premium_progress_bar_enabled=premium_progress_bar_enabled
            )
        await interactionsend(interaction=interaction, msg="Edited Guild", ephemeral=True)