# import packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path as osp
import csv
import string
from time import sleep


# returns list with all urls
def returnUrls(soup, url):
    urlList = [url]
    hyperlinks = soup.find_all("a")

    # use initial url to find base and netloc
    basePath = urlparse(url).path
    base = basePath
    netloc = urlparse(url).netloc

    for hyperlink in hyperlinks:
        href = hyperlink.get("href")
        path = urlparse(href).path

        # determine if page is wiki page
        sections = osp.split(path)
        if isinstance(sections[0], str):
            if base in sections[0] and href not in urlList:
                if " " in href:
                    href = href.replace(" ", "_")
                if urlparse(href).netloc == netloc:
                    urlList.append(href)

                # add netloc to url if not present
                else:
                    urlList.append("http://" + netloc + href)

    return urlList


# function to return webpage from a url
def processPage(soup):
    h = ["h1", "h2", "h3", "h4", "h5", "h6"]

    headers = soup.find_all(h)
    for heading in headers:
        print(heading.text)

        # determine if next element is heading
        nextSibling: object = heading.next_sibling

        # next sibling is not a header or blank
        while nextSibling is not None and nextSibling.name not in h:
            if nextSibling is not None and nextSibling.name not in h:
                # perform analysis on text here
                print(nextSibling)
            nextSibling = nextSibling.next_sibling


"""
        for each in headers:
            # print(each.text)
            for child in each.descendants:
                print(child)
"""
# for each in content:


# function to check if url is part of the team's wiki and if not, to add it to the list of links


# import team list using csv library
with open('iGEM All Teams.csv', newline='') as file:
    reader = csv.reader(file)
    teamData = list(reader)

# create new csv file to write team data to
with open('iGEM All Teams All Data.csv', 'w', newline='') as newFile:
    writer = csv.writer(newFile, delimiter=',')

# add all team page urls to teamData
for team in teamData:
    name = team[0]
    url = team[8]
    page = ''

    while page == '':
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        team.append(returnUrls(soup, url))

    print(team)

# writer(teamData)

"""# prints keys
print(teamData.keys())

# prints teamData (all columns)
pd.options.display.width
pd.set_option('display.width', None)
print(teamData)"""

"""# test an individual page with returnUrls
page = requests.get("http://2013.igem.org/Team:Carnegie_Mellon")
soup = BeautifulSoup(page.content, 'html.parser')
processPage(soup)
a = returnUrls(soup, "http://2013.igem.org/Team:Carnegie_Mellon")

for each in a:
    print(each)"""

# run first file
# this = return_webpage("https://2019.igem.org/Team:US_AFRL_CarrollHS")
# print(this.text)
