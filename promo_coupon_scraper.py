# Get data from the morph.io api
import requests
import selenium-webdriver
import pandas as pd
import numpy as np
import sqlite3
from bs4 import BeautifulSoup
import string
import re
import os
import time
from math import *

# We're always asking for json because it's the easiest to deal with
morph_api_url = "GET https://api.morph.io/[coupon scrapers]/coupon codes.[text.html]?key=[L2R2egk07syVDkczV7Of]&query=[https://www.opticsplanet.com/seasonal-promotions.html]/data.json"

def scrape_data():
    data = requests.get("https://www.opticsplanet.com/seasonal-promotions.html")
    print(data.text)
    soup = BeautifulSoup(data.text, 'html.parser')
    divs = soup.findAll("div", {"class": "event"})
    for div in divs:
        link = div.findAll('a')[0]
        names = link.findAll('span')
        p1 = names[0].text
        p2 = names[1].text
        buttons_having_odds = div.findAll('button')
        p1_odds = frac(buttons_having_odds[0]["data-odds"])
        p2_odds = frac(buttons_having_odds[1]["data-odds"])
        f1.append(p1)
        f2.append(p2)
        f1_odds.append(p1_odds)
        f2_odds.append(p2_odds)


# Keep this key secret!
morph_api_key = "L2R2egk07syVDkczV7Of"

r = requests.get(morph_api_url, params={
  'key': morph_api_key,
})
