# import packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path as osp


# returns list with all urls
def returnUrls(soup, teamName):
    urlList = []
    hyperlinks = soup.find_all("a")

    for hyperlink in hyperlinks:
        href = hyperlink.get("href")
        path = urlparse(href).path

        # determine if page is wiki page
        sections = osp.split(path)
        if sections[0] == "/Team:" + teamName and href not in urlList:
            urlList.append(href)

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

# scrape page

# compile team list
teamList = []
teamData = pd.read_csv("iGEM All Teams.csv")

"""
# prints keys
print(teamData.keys())

# prints teamData (all columns)
pd.options.display.width
pd.set_option('display.width', None)
print(teamData)
"""

page = requests.get("https://2019.igem.org/Team:US_AFRL_CarrollHS/WikiGuide")
soup = BeautifulSoup(page.content, 'html.parser')
# processPage(soup)
a = returnUrls(soup, "US_AFRL_CarrollHS")

for each in a:
    print(each)

print("this is a test")

# run first file
# this = return_webpage("https://2019.igem.org/Team:US_AFRL_CarrollHS")
# print(this.text)
