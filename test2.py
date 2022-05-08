    from PIL import Image
    from PIL import ImageDraw
   
    img = Image.open('astral.png')
   
    I1 = ImageDraw.Draw(img)
   
    I1.text((200, 200), "nice Car", fill=(255, 0, 0))
   
    img.save("astral2.png")