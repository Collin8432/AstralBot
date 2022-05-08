from PIL import Image
from PIL import ImageDraw

img = Image.open('astral.png')

I1 = ImageDraw.Draw(img)
numer = 1255111111231

I1.text((180, 275), f"{numer}", fill=(255,0,0))
I1.text((60, 300), f"Please enter the numbers above to gain access to the server", fill=(255,0,0))
img.save(f"astral{numer}.png")