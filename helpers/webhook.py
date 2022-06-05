# Imports
import disnake
from disnake import Webhook



import aiohttp



from helpers.database import webhook_search



# Function
async def webhooksend(title: str, description: str, guild_id: str) -> None:
   try:
      async with aiohttp.ClientSession() as session:
         hook = await webhook_search(guild_id)
         webhook = Webhook.from_url(f"{hook}", session=session)
         embed = disnake.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
            text=f"Astral Discord Bot"
         )
         await webhook.send(embed=embed, username="Astral - Bot Logging")
   except Exception as e:
      async with aiohttp.ClientSession() as session:
         hook = await webhook_search(guild_id)
         webhook = Webhook.from_url(f"{hook}", session=session)
         embed = disnake.Embed(
            title=f"Error With Bot Webhook Sending Definition",
            description=f"Error: {e}\n Stack Trace: {e.__traceback__}\nReport This To Astral Support",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
         )