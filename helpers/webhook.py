from disnake import Webhook
import disnake
import aiohttp
import datetime

async def webhooksend(title: str, description: str) -> None:
   async with aiohttp.ClientSession() as session:
         webhook = Webhook.from_url("https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG", session=session)
         embed = disnake.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0xDC143C,
            timestamp=datetime.datetime.now()
         )
         await webhook.send(embed=embed, username="Astral - Bot Logging")