"""
Contains all NSFW commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import commands


from utils.color import color
from utils.DeleteButton import DeleteButton
 

import aiohttp


class Nsfw(commands.Cog, name="NSFW"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("NSFW")

    # Commands
    @commands.slash_command(
        name="nsfw",
        description="ass, tits, thighs, hentai"
    )
    async def nsfw(self, interaction):
        pass


    @nsfw.sub_command(
        name="ass",
        description="show a random ass image",
    )
    @commands.is_nsfw()
    async def ass(self, interaction):
        embed = disnake.Embed(
            title="Ass!",
            color=color,
            timestamp=disnake.utils.utcnow(),
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}",
        )
        async with aiohttp.ClientSession() as NsfwSession:
            async with NsfwSession.get("https://nekobot.xyz/api/image?type=ass") as nsfw:
                res = await nsfw.json()
                embed.set_image(url=res["message"])
                await interaction.send(embed=embed, view=DeleteButton())


    @nsfw.sub_command(
        name="hentai",
        description="Show a random hentai image",
    )
    @commands.is_nsfw()
    async def hentai(self, interaction):
        embed = disnake.Embed(
            title="Hentai!",
            color=color,
            timestamp=disnake.utils.utcnow(),
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}",
        )
        async with aiohttp.ClientSession() as NsfwSession:
            async with NsfwSession.get("https://nekobot.xyz/api/image?type=hentai") as nsfw:
                res = await nsfw.json()
                embed.set_image(url=res["message"])
                await interaction.send(embed=embed, view=DeleteButton())


    @nsfw.sub_command(
        name="tits",
        description="show a random tits image",
    )
    @commands.is_nsfw()
    async def tits(self, interaction):
        embed = disnake.Embed(
            title="Tits!",
            color=color,
            timestamp=disnake.utils.utcnow(),
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        async with aiohttp.ClientSession() as NsfwSession:
            async with NsfwSession.get("https://nekobot.xyz/api/image?type=tits") as nsfw:
                res = await nsfw.json()
                embed.set_image(url=res["message"])
                await interaction.send(embed=embed, view=DeleteButton())


    @nsfw.sub_command(
        name="thighs",
        description="shows a random thighs image",
    )
    @commands.is_nsfw()
    async def thighs(self, interaction):
        embed = disnake.Embed(
            title="Thighs!",
            color=color,
            timestamp=disnake.utils.utcnow(),
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        async with aiohttp.ClientSession() as NsfwSession:
            async with NsfwSession.get("https://nekobot.xyz/api/image?type=thighs") as nsfw:
                res = await nsfw.json()
                embed.set_image(url=res["message"])
                await interaction.send(embed=embed, view=DeleteButton())