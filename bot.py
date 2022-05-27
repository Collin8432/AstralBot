
import json
import os
import random
import sys
import datetime
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb
from helpers.database import on_join_insert, webhook_add, webhook_search, on_leave_remove

if not os.path.isfile("./secret/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)

intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents)
token = config.get("token")


@tasks.loop(minutes=1.0)
async def status_task() -> None:
    statuses = [f"Watching Over {len(bot.guilds)} Servers"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))
    channel = await bot.fetch_channel(975404941919260672)
    member = channel.guild.member_count
    await channel.edit(name=f"Members: {member}")


@bot.slash_command(
    name="uptime",
    description="Shows the uptime of the bot",
)
async def uptime(interaction):
    end_time = disnake.utils.utcnow()
    diff = end_time - start_time
    seconds = diff.seconds % 60
    minutes = (diff.seconds // 60) % 60
    hours = (diff.seconds // 3600) % 24
    days = diff.days
    uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    embed = disnake.Embed(
        title="**Uptime**",
        description=f"**The bot has been online for: {uptime_str}**",
        color=0xDC143C,
        timestamp=disnake.utils.utcnow()
    )
    await interaction.send(embed=embed)



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
        img = Image.open('./img/astral.png')

        I1 = ImageDraw.Draw(img)
        
        font = ImageFont.truetype("./font/MomB.ttf", 30)
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
                description=f"**To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive**",
                color=0xDC143C,
                timestamp=disnake.utils.utcnow()
            )
            await interaction.send(embed=embed)

@commands.Cog.listener()
async def on_guild_join(guild):
    await on_join_insert(guild.name, guild.id)

@commands.Cog.listener()
async def on_guild_remove(guild):
    await on_leave_remove(guild.id)

@commands.Cog.listener()
async def on_guild_channel_delete(channel):
    await webhooksend("Channel Deleted", f"{channel.name} **Was Deleted**")

@commands.Cog.listener()
async def on_guild_channel_create(channel):
    await webhooksend("Channel Created", f"{channel.mention} **Was Created**")

@commands.Cog.listener()
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        await webhooksend("Channel Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.mention}")
    if before.changed_roles != after.changed_roles:

        await webhooksend("Channel Roles Changed", f"**From:**\n{before.changed_roles}\n**To:**\n{after.changed_roles}\n\n//idek what this does")
    roles = after.guild.roles
    for role in roles:
        if dict(after.overwrites_for(role)) != dict(before.overwrites_for(role)):
            permissions = dict(after.overwrites_for(role))
            finalpermissions = (str(permissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
            await webhooksend("Channel Permissions Changed", f"\n**Channel Permissions Changed For** {role.mention} **In** {after.mention}\n```\n{finalpermissions}```")
    members = after.guild.members  
    for member in members:
        if dict(after.overwrites_for(member)) != dict(before.overwrites_for(member)):
            permissions = dict(after.overwrites_for(member))
            finalpermissions = (str(permissions).replace("{", "").replace("}", "").replace("'", "").replace(":", " -> ").replace("None", "/").replace("True", "✅").replace("False", "❌").replace(",", "\n"))
            await webhooksend("Channel Permissions Changed", f"\n**Channel Permissions Changed For** {member.mention} **In** {after.mention}\n```\n{finalpermissions}```")

@commands.Cog.listener()
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

@commands.Cog.listener()
async def on_guild_role_create(role):
    await webhooksend("Role Created", f"{role.mention} **Was Created**")

@commands.Cog.listener()
async def on_guild_role_delete(role):
    await webhooksend("Role Deleted", f"{role.name} **Was Deleted**")

@commands.Cog.listener()
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
            await webhooksend("Role Permissions Changed", f"{after.mention}'s **Permissions Updated To:**```\n{finalpermissions}```")
    if before.position != after.position:
        await webhooksend("Role Position Changed", f"**From:**\n{before.position}\n**To:**\n{after.position}")

#
@commands.Cog.listener()
async def on_guild_emojis_update(before, after):
    if before.name != after.name:
        await webhooksend("Emoji Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}")

@commands.Cog.listener()
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel == None:
            await webhooksend("Member Left Voice Channel", f"{member.mention} **Left** {before.channel.mention}")
        else:
            await webhooksend("Member Joined Voice Channel", f"{member.mention} **Joined** {after.channel.mention}")
        if before.deaf != after.deaf:
            if after.deaf:
                await webhooksend("Member Deafened", f"{member.mention} **Was Server Deafened**")
            else:
                await webhooksend("Member Un-Deafened", f"{member.mention} **Was Server Un-Deafened**")
        if before.mute != after.mute:
            if after.mute:
                await webhooksend("Member Muted", f"{member.mention} **Was Server Muted**")
            else:
                await webhooksend("Member Un-Muted", f"{member.mention} **Was Server Un-Muted**")
        if before.self_deaf != after.self_deaf:
            if after.self_deaf:
                await webhooksend("Member Self Deafened", f"{member.mention} **Has Self Deafened**")
            else:
                await webhooksend("Member Self Un-Deafened", f"{member.mention} **Has Self Un-Deafened**")
        if before.self_mute != after.self_mute:
            if after.self_mute:
                await webhooksend("Member Self Muted", f"{member.mention} **Has Self Muted**")
            else:
                await webhooksend("Member Self Un-Muted", f"{member.mention} **Has Self Un-Muted**")
        if before.self_stream != after.self_stream:
            if after.self_stream:
                await webhooksend("Member Streamed", f"{member.mention} **Is Streaming**")
            else:
                await webhooksend("Member Stopped Streaming", f"{member.mention} **Stopped Streaming**")
        if before.self_video != after.self_video:
            if after.self_video:
                await webhooksend("Member Started Showing Video", f"{member.mention} **Started Showing Video**")
            else:
                await webhooksend("Member Stopped Showing Video", f"{member.mention} **Stopped Showing Video**")
        if before.suppress != after.suppress:
            if after.suppress:
                await webhooksend("Member Suppressed", f"{member.mention} **Was Suppressed**")
            else:
                await webhooksend("Member Un-Suppressed", f"{member.mention} **Has Been Un-Suppressed**")
        if before.requested_to_speak_at != after.requested_to_speak_at:
            if after.requested_to_speak_at:
                await webhooksend("Member Requested To Speak", f"{member.mention} **Requested To Speak**")
            else:
                await webhooksend("Member Stopped Requesting To Speak", f"{member.mention} **Stopped Requesting To Speak**")

@commands.Cog.listener()
async def on_guild_scheduled_event_create(event):
    await webhooksend("Scheduled Event Created", f"**{event.name} Was Created**\n**Description:**\n{event.description}\n**Start:**\n{event.scheduled_start_time}\n**End:**\n{event.scheduled_end_time}\n**Event Channel:**\n{event.channel.mention}")

@commands.Cog.listener()
async def on_guild_scheduled_event_delete(event):
    await webhooksend("Scheduled Event Deleted", f"**{event.name} Was Deleted**")

@commands.Cog.listener()
async def on_guild_scheduled_event_update(before, after):
    if before.name != after.name:
        await webhooksend("Scheduled Event Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}")
    if before.description != after.description:
        await webhooksend("Scheduled Event Description Changed", f"**From:**\n{before.description}\n**To:**\n{after.description}")
    if before.scheduled_start_time != after.scheduled_start_time:
        await webhooksend("Scheduled Event Start Changed", f"**From:**\n{before.scheduled_start_time}\n**To:**\n{after.scheduled_start_time}")
    if before.scheduled_end_time != after.scheduled_end_time:
        await webhooksend("Scheduled Event End Changed", f"**From:**\n{before.scheduled_end_time}\n**To:**\n{after.scheduled_end_time}")
    if before.channel != after.channel:
        await webhooksend("Scheduled Event Channel Changed", f"**From:**\n{before.channel.mention}\n**To:**\n{after.channel.mention}")

@commands.Cog.listener()
async def on_stage_instance_create(stage_instance):
    await webhooksend("Stage Instance Created", f"**{stage_instance.name} Was Created**\n**Topic:**\n{stage_instance.Topic}\n**Stage Instance Channel:**\n{stage_instance.channel.mention}")

@commands.Cog.listener()
async def on_stage_instance_delete(stage_instance):
    await webhooksend("Stage Instance Deleted", f"**{stage_instance.name} Was Deleted**")

@commands.Cog.listener()
async def on_stage_instance_update(before, after):
    if before.name != after.name:
        await webhooksend("Stage Instance Name Changed", f"**From:**\n{before.name}\n**To:**\n{after.name}")
    if before.topic != after.topic:
        await webhooksend("Stage Instance topic Changed", f"**From:**\n{before.topic}\n**To:**\n{after.topic}")
    if before.channel != after.channel:
        await webhooksend("Stage Instance Channel Changed", f"**From:**\n{before.channel.mention}\n**To:**\n{after.channel.mention}")

@commands.Cog.listener()
async def on_invite_create(invite):
    if invite.max_age == 0:
        inviteage = "Never"
    else:
        inviteage = f"{invite.max_age}"
    if invite.max_uses == 0:
        inviteuses = "Unlimited"
    else:
        inviteuses = f"{invite.max_uses}"
    await webhooksend("Invite Created", f"**Invite Created By:**\n{invite.inviter.mention}\n**Invite Age:**\n{inviteage}**Possible Uses:**\n{inviteuses}\n**Invite Code:**\n{invite.code}\n**Temporary Membership?**\n{invite.temporary}\n**Invite Channel:**\n{invite.channel.mention}\n**Expires At:**\n{invite.expires_at}")

@commands.Cog.listener()
async def on_invite_delete(invite):
    await webhooksend("Invite Deleted", f"**Invite Created By:**\n{invite.inviter.mention}\n**Invite Code:**\n{invite.code}")

@commands.Cog.listener()
async def on_group_join(channel, user):
    await webhooksend("Group Joined", f"**{user.mention} **Joined** {channel.mention}**")

@commands.Cog.listener()
async def on_group_remove(channel, user):
    await webhooksend("Group Left", f"**{user.mention} **Left** {channel.mention}")


@commands.Cog.listener()
async def on_connect():
    global start_time
    start_time = disnake.utils.utcnow()


@commands.Cog.listener()
async def on_shard_connect(shard_id):
    pass

@commands.Cog.listener()  
async def on_disconnect():
    await webhooksend("Discord Error", "Called when the client has disconnected from Discord, or a connection attempt to Discord has failed. This could happen either through the internet being disconnected, explicit calls to close, or Discord terminating the connection one way or the other.")

@commands.Cog.listener()
async def on_shard_disconnect(shard_id):
    pass

@commands.Cog.listener()
async def on_shard_ready(shard_id):
    pass

@commands.Cog.listener()
async def on_resumed():
    await webhooksend("Resumed", "Called when the client has resumed a connection to Discord.")

@commands.Cog.listener()
async def on_shard_resumed(shard_id):
    pass


@commands.Cog.listener()
async def on_socket_event_type(event_type):
    pass

@commands.Cog.listener()
async def on_typing(channel, user, when):
    pass

@commands.Cog.listener()
async def on_bulk_message_delete(messages):
    await webhooksend("Messages Bulk Deleted/Purged", f"**Messages Bulk Deleted/Purged With A Total Of {len(messages)} Messages Deleted**")

@commands.Cog.listener()
async def on_message_edit(before, after):
    if before.content != after.content:
        await webhooksend("Message Edited", f"**From:**\n{before.content}\n**To:**\n{after.content}")

@commands.Cog.listener()
async def on_reaction_add(reaction, user):
    await webhooksend("Reaction Added", f"{reaction.emoji} **Was Added To** {reaction.message.content} **In** {reaction.message.channel.mention} **By** {user.mention}")

@commands.Cog.listener()
async def on_reaction_remove(reaction, user):
    await webhooksend("Reaction Removed", f"{reaction.emoji} **Was Removed From** {reaction.message.content} **In** {reaction.message.channel.mention} **By** {user.mention}")


@bot.slash_command(
    name="setup",
    description="Sets Up The Bot",
)
async def setup(interaction):
    await interaction.send("Setup Started")
    await interaction.send("Please Wait...")
    category = await interaction.guild.create_category(name="Astral")
    channel = await category.create_text_channel(name="Astral - Bot Logging")
    with open("./img/astral.png", "rb") as file:
        data = file.read()
    webhook = await channel.create_webhook(name="Astral - Bot Logging", avatar=data)
    
    await webhook_add(f"{interaction.guild.id}", f"{webhook.url}")
    await interaction.send("Setup Complete!")
    

bot.run(config["token"])