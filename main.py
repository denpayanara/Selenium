import datetime
import time

from PIL import Image, ImageFont, ImageDraw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

options = Options()
options.add_argument('--headless')
web_driver = webdriver.Chrome(options=options)

url = ''
web_driver.get(url)
time.sleep(3)
web_driver.save_screenshot('image.png')
web_driver.quit()
time.sleep(1)

img = Image.open('image.png')
draw  = ImageDraw.Draw(img)
font = ImageFont.truetype('NotoSansJP-Light.otf', 45)
draw.text((400, 25), now.strftime('%Y/%m/%d %H:%M'), (255, 0, 0), font=font)
img.save(f"data/{now.strftime('%Y%m%d_%H')}.png")
