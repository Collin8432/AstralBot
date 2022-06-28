# Imports
import disnake
from disnake.ext import commands



from utils.color import color
from utils.deleteinteraction import deleteinteraction
from utils.message import interactionsend



import aiohttp



class nsfw(commands.Cog, name="NSFW"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot



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
                await interactionsend(interaction=interaction, embed=embed)

    @nsfw.sub_command(
        name="hentai",
        description="Show a random hentai image",
    )
    @commands.is_nsfw()
    async def hentai(self, interaction):
        embed = disnake.Embed(
            title="hentai",
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
                await interactionsend(interaction=interaction, embed=embed)


    @nsfw.sub_command(
        name="tits",
        description="show a random tits image",
    )
    @commands.is_nsfw()
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
                await interactionsend(interaction=interaction, embed=embed)

    @nsfw.sub_command(
        name="thighs",
        description="shows a random thighs image",
    )
    @commands.is_nsfw()
    async def thighs(self, interaction):
        embed = disnake.Embed(
            title="Thighs",
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
                await interactionsend(interaction=interaction, embed=embed)