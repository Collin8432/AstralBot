
import json
import os
import random
import sys
from time import time
import datetime
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
    beforeuptime = datetime.datetime.now()
    uptime = beforeuptime
    before1 = beforeuptime.strftime("%I")
    before2 = beforeuptime.strftime("%M")
    before3 = beforeuptime.strftime("%S")
    aftertime = (f"{before1}:{before2}:{before3}")
    await webhooksend(f"Uptime Update", f"{starttime} -> {aftertime}")

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
    if before.status != after.status:
        await webhooksend("Presence Changed", f"<@{after.id}> Changed Status \n**From:**\n{before.status}\n**To:**\n{after.status}")
    if before.activity != after.activity:
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
    except:
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
    await webhooksend("Channel Created", f"<#{channel.name.id}> Was Created")
@bot.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        await webhooksend("Channel Name Changed", f"**From:**\n<#{before.id}>\n**To:**\n<#{after.id}>")
    if before.permissions_for != after.permissions_for:
        if before.id != after.id or before.name != after.name or before.rtc_region != after.rtc_region or before.position != after.position or before.bitrate != after.bitrate or before.video_quality_mode != after.video_quality_mode or before.user_limit != after.user_limit or before.category_id != after.category_id or before.nsfw != after.nsfw:
            await webhooksend("Channel Information", f"{after.mention} Was Updated\n**Id Before:**\n{before.id}\n**Id After:**\n{after.id}\n**Name Before:**\n{before.name}\n**Name After:**\n{after.name}\n**Position Before:**\n{before.position}\n**Position After:**\n{after.position}\n**Bitrate Before:**\n{before.bitrate}\n**Bitrate After:**\n{after.bitrate}\n**User Limit Before:**\n{before.user_limit}\n**User Limit After:**\n{after.user_limit}\n**Category Before:**\n{before.category_id}\n**Category After:**\n{after.category_id}\n**NSFW Before:**\n{before.nsfw}\n**NSFW After:**\n{after.nsfw}\n**RTC Region Before:**\n{before.rtc_region}\n**RTC Region After:**\n{after.rtc_region}\n**Video Quality Mode Before:**\n{before.video_quality_mode}\n**Video Quality Mode After:**\n{after.video_quality_mode}")
    everyone = after.guild.get_role(944297787779072020)
    if before.permission != after.permissions_for(everyone):






@bot.event
async def on_connect():
    global starttime
    beforeuptime = datetime.datetime.now()
    uptime = beforeuptime
    before1 = beforeuptime.strftime("%I")
    before2 = beforeuptime.strftime("%M")
    before3 = beforeuptime.strftime("%S")
    starttime = (f"{before1}:{before2}:{before3}")


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
    await webhooksend("Messages Bulk Deleted/Purged", f"{messages}, With A Total Of {len(messages)} Messages Deleted")

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

@bot.slash_command(name="setperms", description="Set Permissions")
async def setperms(interaction):
    await interaction.channel.set_permissions(interaction.author, view_channel=True,
                                                      send_messages=False)

bot.run(config["token"])