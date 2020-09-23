# import packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path as osp
import csv
import string
from time import sleep

# function to return webpage from a url
def processPage(soup):
    h = ["h1", "h2", "h3", "h4", "h5", "h6"]
    text = ["p", "a", "td", "li", "ul", "ol", "tr"]

    content = soup.find('div', {"id": "content"})
    #print(content.get_text())

    headers = content.find_all(h)
    for heading in headers:
        print(heading.text)

        # determine if next element is heading
        nextSibling: object = heading.next_sibling
        #while nextSibling is None:
          #  nextSibling: object = heading.next_sibling

        #print("\n\nNEW ELEMENT")
        #print("HEADING")
        #print(nextSibling.name)

        # next sibling is not a header or blank
        while nextSibling is not None and nextSibling.name not in h:
             if nextSibling is not None and nextSibling.name not in h and nextSibling.name in text:
                 #perform analysis on text here
                 print(nextSibling.text)
             nextSibling = nextSibling.next_sibling

   # links = soup.find_all("a")
  #  for link in links:
   #     print(link)

"""
        for each in headers:
            # print(each.text)
            for child in each.descendants:
                print(child)
"""

# assign all teams list to teamData
with open('iGEM All Teams.csv', newline='') as file:
    reader = csv.reader(file)
    teamData = list(reader)

# assign iGEM urls to urls
with open('All Teams URLs.csv', newline='') as file:
    reader = csv.reader(file)
    urls = list(reader)

allData = list(zip(teamData, urls))

"""# prints team list
for team in allData:
    print(team)"""

"""# prints keys
print(teamData.keys())

# prints teamData (all columns)
pd.options.display.width
pd.set_option('display.width', None)
print(teamData)"""

# test an individual page with returnUrls
i = 1
for url in allData[1][1]:
    print("Page #" + str(i))
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    processPage(soup)

    i = i + 1

"""for each in a:
    print(each)"""

# run first file
# this = return_webpage("https://2019.igem.org/Team:US_AFRL_CarrollHS")
# print(this.text)
