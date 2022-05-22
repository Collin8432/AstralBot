from disnake import Webhook
import disnake
import aiohttp
import asyncio
import datetime

async def uptimesend(title: str, description: str) -> None:
   async with aiohttp.ClientSession() as session:
         webhook = Webhook.from_url("https://discord.com/api/webhooks/977766434581151795/xYgBFz026UYS6MyvyWQBReFNBwW_UhpDo3-DYuU32oqvC4K3daI6Kej0MeeRRGvnHFe3", session=session)
         embed = disnake.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0xDC143C,
            timestamp=datetime.datetime.now()
         )
         await webhook.send(embed=embed, username="Astral - Bot Logging")