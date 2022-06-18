# Imports
from time import time
import disnake
from disnake.ext import commands

from helpers.color import color
from helpers.deleteinteraction import deleteinteraction
from helpers import checks

import aiohttp


class nsfw(commands.Cog, name="NSFW"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Commands
    @commands.slash_command(
        name="nsfw",
        description="ass, tits, thighs"
    )
    async def nsfw(self, interaction):
        pass

    @nsfw.sub_command(
        name="ass",
        description="Show a random ass image",
    )
    @commands.is_nsfw()
    @checks.not_blacklisted()
    async def ass(self, interaction):
        embed = disnake.Embed(
            title="Ass",
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
                await interactionsend(interaction, embed=embed, view=deleteinteraction())

    @nsfw.sub_command(
        name="hentai",
        description="Show a random hentai image",
    )
    @commands.is_nsfw()
    @checks.not_blacklisted()
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
                await interactionsend(interaction, embed=embed, view=deleteinteraction())


    @nsfw.sub_command(
        name="tits",
        description="Show a random tits image",
    )
    @commands.is_nsfw()
    @checks.not_blacklisted()
    async def tits(self, interaction):
        embed = disnake.Embed(
            title="Tits",
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
                await interactionsend(interaction, embed=embed, view=deleteinteraction())

    @nsfw.sub_command(
        name="thighs",
        description="Show a random thighs image",
    )
    @commands.is_nsfw()
    @checks.not_blacklisted()
    async def thighs(self, interaction):
        embed = disnake.Embed(
            title="Tits",
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
                await interactionsend(interaction, embed=embed, view=deleteinteraction())


def setup(bot):
    bot.add_cog(nsfw(bot))
