FROM python:3.10.1

ADD bot.py .

RUN pip install disnake json os random sys time datetime typing colorama random PIL asyncio aiohttp asyncio arrow

CMD ["python", "./bot.py"]
