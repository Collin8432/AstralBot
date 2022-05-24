# import disnake 
# import asyncio
# from disnake import Webhook
# import aiohttp

# async def foo():
#     async with aiohttp.ClientSession() as session:
#         webhook = Webhook.from_url('https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG', session=session)
#         await webhook.send('Hello World', username='Foo')
# asyncio.run(foo())

import random
import os
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
newlist = ""
for i in range(5, 50):
    newlist += (random.choice(list))
    continue
print(newlist)
