
import json
import os
import random
import sys
from time import time
import datetime
from typing import final
from colorama import Fore
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio
from disnake import Webhook
import aiohttp
from helpers.webhook import webhooksend
from helpers.uptime import uptimesend
from helpers import checks
import exceptions
import arrow
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents)
token = config.get("token")


@tasks.loop(minutes=1.0)
async def status_task() -> None:
    statuses = ["astralsb.ga", "astral on top", "with you"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))
    channel = await bot.fetch_channel(975404941919260672)
    member = channel.guild.member_count
    await channel.edit(name=f"Members: {member}")

@tasks.loop(minutes=10.0)
async def uptime_task() -> None:
    end_time = datetime.datetime.now()
    diff = end_time - start_time
    seconds = diff.seconds % 60
    minutes = (diff.seconds // 60) % 60
    hours = (diff.seconds // 3600) % 24
    days = diff.days
    uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    await uptimesend(f"Uptime Update", f"{uptime_str}")


def load_commands(command_type: str) -> None:
    for file in os.listdir(f"./cogs/{command_type}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Loaded (/) {extension} Commands")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


if __name__ == "__main__":
    load_commands("general")
    load_commands("moderation")
    load_commands("fun")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ")
    status_task.start()
    uptime_task.start()

@bot.event
async def on_slash_command(interaction):
    await webhooksend(f"Command Executed", f"**<@{interaction.author.id}>** Executed /**{interaction.data.name}** {interaction.application_command.qualified_name} in <#{interaction.channel.id}>")

@bot.event
async def on_slash_command_error(interaction: ApplicationCommandInteraction, error: Exception) -> None:
    embed = disnake.Embed(
        title="Error",
        description=f"Error With Command:\n```py\n{error}```",
        color=0xDC143C,
        timestamp=datetime.datetime.now()
    )
    try:
        await interaction.edit_original_message(embed=embed, ephemeral=True)
    except:
        await interaction.send(embed=embed, ephemeral=True)

botids = [938579223780655145]
@bot.listen('on_message')
async def on_message(message):
    if "nigger" in message.content and message.guild.id == 944297787779072020 and message.author.id not in botids:
        await message.reply("Please Don't Say That")
        await message.delete()
        await webhooksend("N-Word Logged", f"<@{message.author.id}> Sent An N-Word In <#{message.channel.id}>\n **Content:** \n{message.content}")
    if message.channel.id == 970325969359503460 and message.author.id not in botids:
        await message.author.edit(nick=f"{message.content}")
        embed = disnake.Embed(
            title=f"Nickname Changed!",
            description=f"<@{message.author.id}> Changed Nickname To: {message.content}",
            color=0xDC143C,
            timestamp=datetime.datetime.now()
        )
        embed.set_image(url=message.author.display_avatar)
        await message.reply(embed=embed)

@bot.event
async def on_message_delete(message):
    await webhooksend("Message Deleted", f"Chat Deleted In <#{message.channel.id}>\n**Author:** \n<@{message.author.id}>\n**Content:** \n{message.content}")

@bot.event
async def on_member_ban(guild, user):
    await webhooksend("Member Banned", f"<@{user.id}> Was Banned From Astral")
    embed = disnake.Embed(
        title="You Were Banned From Astral",
        description=f"<@{user.id}> Was Banned From Astral",
        color=0xDC143C,
        timestamp=datetime.datetime.now()
    )
    await user.send(embed=embed)   

@bot.event
async def on_member_unban(guild, user):
    await webhooksend("Member Unbanned", f"<@{user.id}> Was Unbanned From Astral")
    embed = disnake.Embed(
        title="You Were Unbanned From Astral",
        description=f"<@{user.id}> Was Unbanned From Astral\nhttps://discord.gg/uNnJyjaG",
        color=0xDC143C,
        timestamp=datetime.datetime.now()
    )
    await user.send(embed=embed)

@bot.event
async def on_presence_update(before, after):
    if before.status != after.status and after.id != 935339228324311040:
        await webhooksend("Presence Changed", f"<@{after.id}> Changed Status \n**From:**\n{before.status}\n**To:**\n{after.status}")
    if before.activity != after.activity and after.id != 935339228324311040:
        await webhooksend("Activity Changed", f"<@{after.id}> Changed Activity \n**From:**\n{before.activity}\n**To:**\n{after.activity}")

@bot.event
async def on_member_update(before, after):
    if before.display_name != after.display_name:
        print(f"{before.display_name} -> {after.display_name}")
    if before.roles != after.roles:
        roles = [role.mention for role in before.roles]
        roles2 = [role.mention for role in after.roles]
        beforeroles = str(roles).replace("]", "").replace("[", "").replace("'", "")
        afterroles = str(roles2).replace("]", "").replace("[", "").replace("'", "")
        await webhooksend(f"Roles Changed", f"<@{after.id}> Roles Changed\n**Before:**\n{beforeroles}\n**After:**\n{afterroles}")
    if before.current_timeout != after.current_timeout:
        await webhooksend(f"Timeout!", f"<@{after.id}> Timeout Changed\n**Before:**\n{before.current_timeout}\n**After:**\n{after.current_timeout}")

 

@bot.event
async def on_user_update(before, after):
    if before.display_avatar != after.display_avatar:
        await webhooksend(f"Avatar Changed", f"<@{after.member.id}> Avatar Changed\n**Before:**\n{before.display_avatar}\n**After:**\n{after.display_avatar}")
    if before.discriminator != after.discriminator:
        await webhooksend(f"Discriminator Changed", f"<@{after.member.id}> Discriminator Changed\n**Before:**\n{before.discriminator}\n**After:**\n{after.discriminator}")

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        img = Image.open("astral.png")
        image = ImageDraw.Draw(img)
        font = ImageFont.truetype("MomB.ttf", 30)
        image.text((160, 275), f"Welcome,", font=font, fill=(43,22,197))
        image.text((160, 325), f"{member.name}", font=font, fill=(43,22,197))
        list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        randomnumber = ""
        for i in range(5, 15):
            randomnumber += (random.choice(list))
            continue
        img.save(f"astral{randomnumber}.png")
        imgfile = disnake.File(f"astral{randomnumber}.png") 
        await guild.system_channel.send(file=imgfile)
        await webhooksend("Member Joined", f"<@{member.id}> Joined Astral")

@bot.event
async def on_member_remove(member):
    await webhooksend("Member Left", f"<@{member.id}> Left Astral")
    embed = disnake.Embed(
        title=f"{member.name}, Sorry Too See You Go!",
        description=f"If you left on accident, please join back!\nhttps://discord.gg/uNnJyjaG",
        color=0xDC143C,
        timestamp=datetime.datetime.now()
    )
    try:
        await member.send(embed=embed)
    except disnake.Forebidden:
        pass

    
async def Checker(filename):
    def check(message):
        return message.content == filename.upper() or message.content == filename.lower()
    await bot.wait_for("message", check=check)
    
verifychannel = [972679418763935794]
@bot.slash_command(
    name="Verify",
    description="Verify yourself to gain access to the server"
)
async def verify(interaction):
    if interaction.channel.id not in verifychannel:
        await interaction.send("You can only use this command in <#972679418763935794>")
    else:
        list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        FileName = ""
        for i in range(5, 15):
            FileName += (random.choice(list))
            continue
        print(f"{FileName}")
        img = Image.open('astral.png')

        I1 = ImageDraw.Draw(img)
        
        font = ImageFont.truetype("MomB.ttf", 30)
        I1.text((150, 275), f"{FileName}", fill=(32,22,197), font=font)
        I1.text((125, 300), f"Please enter the", fill=(43,22,197), font=font)
        I1.text((125, 325), f"letters/numbers", fill=(43,22,197), font=font)
        I1.text((75, 350), f"above to gain access", fill=(43,22,197), font=font)
        I1.text((150, 375), f"to Astral", fill=(43,22,197), font=font)
        img.save(f"astral{FileName}.png")
        await interaction.send(file=disnake.File(f"astral{FileName}.png"))
        try:
            await Checker(f"{FileName}")
        except:
            print("fail")

        await interaction.author.add_roles(disnake.Object(972988909573242881))
        await webhooksend("Member Verified", f"Verified <@{interaction.author.id}>")
        if interaction.channel.id == 972679418763935794:
            await interaction.channel.purge(limit=9999999)
            embed = disnake.Embed(
                title=f"How To Verify!",
                description=f"To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive",
                color=0xDC143C,
                timestamp=datetime.datetime.now()
            )
            await interaction.send(embed=embed)

@bot.event
async def on_guild_channel_delete(channel):
    await webhooksend("Channel Deleted", f"{channel.name} Was Deleted")

@bot.event
async def on_guild_channel_create(channel):
    await webhooksend("Channel Created", f"#{channel.mention} Was Created")

@bot.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        await webhooksend("Channel Name Changed", f"**From:**\n<#{before.id}>\n**To:**\n<#{after.id}>")
    if before.changed_roles != after.changed_roles:
        print(f"{before.changed_roles} -> {after.changed_roles}")
    roles = after.guild.roles
    for role in roles:
        if dict(after.overwrites_for(role)) != dict(before.overwrites_for(role)):
            permissions = dict(after.overwrites_for(role))
            finalpermissions = (str(permissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
            await webhooksend("Channel Permissions Changed", f"\nChannel Permissions Changed For {role.mention} In {after.mention}\n```\n{finalpermissions}```")
    members = after.guild.members  
    for member in members:
        if dict(after.overwrites_for(member)) != dict(before.overwrites_for(member)):
            permissions = dict(after.overwrites_for(member))
            finalpermissions = (str(permissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
            await webhooksend("Channel Permissions Changed", f"\nChannel Permissions Changed For {member.mention} In {after.mention}\n```\n{finalpermissions}```")

@bot.event
async def on_guild_update(before, after):
    if before.name != after.name:
        await webhooksend("Guild Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}")
    if before.afk_timeout != after.afk_timeout:
        await webhooksend("Guild AFK Timeout Changed", f"**From:**\n{before.afk_timeout}\n**To:**\n{after.afk_timeout}")
    if before.afk_channel != after.afk_channel:
        await webhooksend("Guild AFK Channel Changed", f"**From:**\n{before.afk_channel}\n**To:**\n{after.afk_channel}")
    if before.owner_id != after.owner_id:
        await webhooksend("Guild Owner Changed", f"**From:**\n{before.owner.mention}\n**To:**\n{after.owner.mention}")
    if before.description != after.description:
        await webhooksend("Guild Description Changed", f"**From:**\n{before.description}\n**To:**\n{after.description}")

@bot.event
async def on_guild_role_create(role):
    await webhooksend("Role Created", f"{role.mention} Was Created")

@bot.event
async def on_guild_role_delete(role):
    await webhooksend("Role Deleted", f"{role.name} Was Deleted")

@bot.event
async def on_guild_role_update(before, after):
    if before.name != after.name:
        await webhooksend("Role Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}")
    if before.color != after.color:
        await webhooksend("Role Color Changed", f"**From:**\n{before.color}\n**To:**\n{after.color}")
    if before.hoist != after.hoist:
        await webhooksend("Role Hoist Changed", f"**From:**\n{before.hoist}\n**To:**\n{after.hoist}")
    if before.mentionable != after.mentionable:
        await webhooksend("Role Mentionable Changed", f"**From:**\n{before.mentionable}\n**To:**\n{after.mentionable}")
    if before.permissions != after.permissions:
        if dict(before.permissions) != dict(after.permissions):
            afterpermissions = dict(after.permissions)
            finalpermissions = (str(afterpermissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
            await webhooksend("Role Permissions Changed", f"{after.mention}'s Permissions Updated To:```\n{finalpermissions}```")
    if before.position != after.position:
        await webhooksend("Role Position Changed", f"**From:**\n{before.position}\n**To:**\n{after.position}")


@bot.event
async def on_guild_emojis_update(before, after):
    if before.name != after.name:
        await webhooksend("Emoji Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}")

@bot.event
async def on_voice_state_update(member, before, after):
    if before

@bot.event
async def on_connect():
    global start_time
    start_time = datetime.datetime.now()


@bot.event
async def on_shard_connect(shard_id):
    pass

@bot.event  
async def on_disconnect():
    await webhooksend("Discord Error", "Called when the client has disconnected from Discord, or a connection attempt to Discord has failed. This could happen either through the internet being disconnected, explicit calls to close, or Discord terminating the connection one way or the other.")

@bot.event
async def on_shard_disconnect(shard_id):
    pass

@bot.event
async def on_shard_ready(shard_id):
    pass

@bot.event
async def on_resumed():
    await webhooksend("Resumed", "Called when the client has resumed a connection to Discord.")

@bot.event
async def on_shard_resumed(shard_id):
    pass


@bot.event
async def on_socket_event_type(event_type):
    pass

@bot.event
async def on_typing(channel, user, when):
    pass

@bot.event
async def on_bulk_message_delete(messages):
    await webhooksend("Messages Bulk Deleted/Purged", f"Messages Bulk Deleted/Purged With A Total Of {len(messages)} Messages Deleted")

@bot.event
async def on_message_edit(before, after):
    if before.content != after.content:
        await webhooksend("Message Edited", f"**From:**\n{before.content}\n**To:**\n{after.content}")

@bot.event
async def on_reaction_add(reaction, user):
    await webhooksend("Reaction Added", f"{reaction.emoji} Was Added To {reaction.message.content} In {reaction.message.channel.mention} By {user.mention}")

@bot.event
async def on_reaction_remove(reaction, user):
    await webhooksend("Reaction Removed", f"{reaction.emoji} Was Removed From {reaction.message.content} In {reaction.message.channel.mention} By {user.mention}")



bot.run(config["token"])