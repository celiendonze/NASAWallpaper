# -*- coding: utf-8 -*-

import feedparser
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import requests
from io import BytesIO
import ctypes
import sys
from os.path import expanduser

def drawTitle(title, img):
    width, height = img.size

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 50)
    w, h = draw.textsize(title, font)
    x = (width-w)//2
    y = (height-h)//16

    black = (0, 0, 0)
    white = (255, 255, 255)
    i = 1
    draw.text((x-i, y-i), title, black, font)
    draw.text((x+i, y-i), title, black, font)
    draw.text((x-i, y+i), title, black, font)
    draw.text((x+i, y+i), title, black, font)
    draw.text((x, y), title, white, font)

if __name__ == "__main__":
    i = 0
    if len(sys.argv) == 2:
        try:
            i = int(sys.argv[1])
        except:
            pass
    
    feed = feedparser.parse("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    imageUrl = feed["items"][i].enclosures[0].href
    
    title = feed["items"][i].title

    response = requests.get(imageUrl)
    img = Image.open(BytesIO(response.content))

    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    img.thumbnail((width,height), Image.BICUBIC)

    drawTitle(title, img)
    
    path = expanduser(r"~\Pictures") + r"\wallpaper.jpg"
    
    img.save(path)
    
    user32.SystemParametersInfoW(20, 0, path , 0)

    print("New image set as wallpaper.")
    print(title)