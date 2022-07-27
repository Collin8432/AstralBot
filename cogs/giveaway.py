"""
Contains Giveaway commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""



# imports
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands, tasks


from utils.color import color
 

import random
import json
import time
import datetime


def convert(date):
    pos = ["s", "m", "h", "d"]
    time_dic = {"s": 1, "m": 60, "h": 3600, "d": 3600 *24}
    i = {"s": "Seconds", "m": "Minutes", "h": "Hours", "d": "Hours"}
    unit = date[-1]
    if unit not in pos:
        return -1
    try:
        val = int(date[:-1])

    except:
        return -2

    if val == 1:
        return val * time_dic[unit], i[unit][:-1]
    else:
        return val * time_dic[unit], i[unit]


async def stop_giveaway(self, g_id, data):
    channel = self.bot.get_channel(data["channel_id"])
    giveaway_message = await channel.fetch_message(int(g_id))
    users = await giveaway_message.reactions[0].users().flatten()
    users.pop(users.index(self.bot.user))
    if len(users) < data["winners"]:
        winners_number = len(users)
    else:
        winners_number = data["winners"]

    winners = random.sample(users, winners_number)
    users_mention = []
    for user in winners:
        users_mention.append(user.mention)
    embed = disnake.Embed(
        title="🎉 {} 🎉".format(data["prize"]),
        color=color,
        description="Congratulations {} you won the giveaway!".format(", ".join(users_mention))
    )
    await giveaway_message.edit(embed=embed)
    ghost_ping = await channel.send(", ".join(users_mention))
    await ghost_ping.delete()
    giveaways = json.load(open("cogs/giveaways.json", "r"))
    del giveaways[g_id]
    json.dump(giveaways, open("cogs/giveaways.json", "w"), indent=4)



class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giveaway_task.start()


    @tasks.loop(seconds=5)
    async def giveaway_task(self):
        await self.bot.wait_until_ready()
        giveaways = json.load(open("cogs/giveaways.json", "r"))

        if len(giveaways) == 0:
            return

        for giveaway in giveaways:
            data = giveaways[giveaway]
            if int(time.time()) > data["end_time"]:
                await stop_giveaway(self, giveaway, data)


    @commands.slash_command(
        name="giveaway",
        description="Create a giveaway",
    )
    @commands.has_permissions(manage_guild=True)
    async def giveaway(self,
                       interaction: ApplicationCommandInteraction,
                       prize: str, 
                       channel: disnake.TextChannel,
                       duration: str,
                       winners: int
    ):
        converted_time = convert(duration)
        embed = disnake.Embed(
            title="🎉 {} 🎉".format(prize),
            color=color,
            description=f'**{winners}** {"winner" if winners == 1 else "winners"}\n'
                        f'Hosted by {interaction.author.mention}\n\n'
                        f'**React with 🎉 to get into the giveaway**\n'
        )
        embed.set_footer(text="Ends at")

        embed.timestamp = datetime.datetime.utcnow() + datetime.timedelta(seconds=converted_time[0])
        giveaway_message = await channel.send(embed=embed)
        await giveaway_message.add_reaction("🎉")
        now = int(time.time())
        giveaways = json.load(open("cogs/giveaways.json", "r"))
        data = {
            "prize": prize,
            "host": interaction.author.id,
            "winners": winners,
            "end_time": now + converted_time[0],
            "channel_id": channel.id
        }
        giveaways[str(giveaway_message.id)] = data
        json.dump(giveaways, open("cogs/giveaways.json", "w"), indent=4)
        await interaction.send(msg="Giveaway Created", ephemeral=True)


    @commands.slash_command(
        name="stopgiveaway",
        description="stop a giveaway",
    )
    @commands.has_permissions(manage_guild=True)
    async def stopgiveaway(self,
                           interaction: ApplicationCommandInteraction,
                           message_id: disnake.Message):
        giveaways = json.load(open("cogs/giveaways.json", "r"))
        if not message_id in giveaways.keys(): 
            embed = disnake.Embed(
               title="Error!",
               description="Giveaway ID Not Found",
               color=color,
            )
            return await interaction.send(embed=embed)
        await stop_giveaway(self, message_id, giveaways[message_id])
        await interaction.send(msg="Giveaway Stopped", ephemeral=True)