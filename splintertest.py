#import splinter, etc
from bs4 import BeautifulSoup
import requests
import pymongo

from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#go to the URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

#Navigate to the full image
browser.click_link_by_partial_text('FULL IMAGE')

#soup it up
image_html = browser.html
image_soup = BeautifulSoup(image_html, 'html.parser')

print(image_soup)
#grab that image
image_ext = image_soup.find('img', class_= "fancybox-image")

print(image_ext)

'''
featured_image_url = "https://www.jpl.nasa.gov" + image_ext
#image_link = image_soup.find("div", class_="fancybox-inner")
print(featured_image_url)
image_dict = {"featured_image" : featured_image_url}'''