import os
import feedparser
from PIL import Image
import requests
from io import BytesIO
import ctypes
from os.path import expanduser

from loguru import logger


if __name__ == "__main__":
    feed = feedparser.parse("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    imageUrl = feed["items"][0].enclosures[0].href
    title = feed["items"][0].title
    logger.info(f"Image URL: {imageUrl}")
    logger.info(f"Image title: {title}")

    response = requests.get(imageUrl)
    image = Image.open(BytesIO(response.content))

    path = expanduser(r"~\Pictures") + r"\wallpaper.jpg"
    image.save(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    logger.info("New image set as wallpaper.")
