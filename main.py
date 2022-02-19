import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
web_driver = webdriver.Chrome(options=options)

# 野迫川ライブカメラ
url_nosegawa = 'https://www.komadori.ne.jp/nara-livecamera/area/nosegawa1.html'

web_driver.get(url_nosegawa)

time.sleep(5)

now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
now_str = now.strftime('%Y%m%d_%H')

web_driver.save_screenshot(f'data/{now_str}.png')
