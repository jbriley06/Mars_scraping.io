import os 
import time 
import pandas as pd
import numpy as np 
from splinter import Browser
from bs4 import BeautifulSoup as bs 
from selenium import webdriver


browser = Browser('chrome', headless=False)
url = 'https://mars.nasa.gov/news/'
time.sleep(1)
browser.visit(url)
time.sleep(2)
html = browser.html
soup= bs(html, 'html.parser')
side_panel = soup.find('ul', class_="item_list")
news_title = side_panel.find('h3').getText()
news_p= soup.find('div', class_="article_teaser_body").getText()

url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser = Browser('chrome', headless=False)
browser.visit(url_image)
time.sleep(1)
image = browser.find_by_id('full_image')
image.click()
time.sleep(1)
html = browser.html
soup = bs(html, 'lxml')
find_img = soup.find('div',class_='fancybox-inner')
img = soup.find('img', class_= 'fancybox-image')
extract_img_src = img['src']

img_nav = 'https://www.jpl.nasa.gov' + extract_img_src


url_twitter = 'https://twitter.com/marswxreport?lang=en'
browser = Browser('chrome', headless=False)
time.sleep(2)
browser.visit(url_twitter)
time.sleep(2)
html = browser.html
soup = bs(html, 'html.parser')
mars_weather= soup.find('div', class_='js-tweet-text-container').getText()

url_fact = 'http://space-facts.com/mars/'
browser = Browser('chrome', headless=False)
time.sleep(2)
browser.visit(url_fact)
html = browser.html
soup = bs(html, 'html.parser')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
description_list = df[0]
value_list = df[1]
all_list = zip(description_list, value_list)

mars_dict = {}

for description, value in all_list:
    mars_dict[description] = value



scraped_stuff = {
    "News Headline": news_title,
    "News Description": news_p,
    "NASA image": img_nav,
    "Mars Info": mars_dict
}

print(scraped_stuff)    
    
