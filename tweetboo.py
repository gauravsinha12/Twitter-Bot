from selenium import webdriver
import pyautogui as pg
import time
import pandas as pd
from conf import CHROME_PROFILE_PATH

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe',options=options)
browser.get('https://www.google.com/')
time.sleep(3)
usern = browser.find_element_by_xpath('//input[@type="text"]')
usern.send_keys('your ID')
passs = browser.find_element_by_xpath('//input[@type="password"]')
passs.send_keys('Your Password')
time.sleep(3)
pg.moveTo(491,446,1)
pg.click()
time.sleep(1)
twe = browser.find_element_by_xpath('//div[@data-offset-key="dvip0-0-0"][@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
twe.send_keys('lad jina marzi tu cheek mere te par soch kar le pareek mare tee ..')
butt = browser.find_element_by_xpath('//div[@aria-disabled="true"][@data-testid="tweetButtonInline"]')
butt.click()