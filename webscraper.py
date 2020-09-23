# import packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path as osp
import csv
import string
import xlsxwriter
from time import sleep


# function to return webpage from a url
def processPage(soup, teamInfo, url):
    h = ["h1", "h2", "h3", "h4", "h5", "h6"]
    text = ["p", "a", "td", "li", "ul", "ol", "tr"]

    # create arrays for allRows and currentRow
    allRows = []
    currentRow = []
    contentText = []

    content = soup.find('div', {"id": "content"})
    # print(content.get_text())

    headers = content.find_all(h)
    for heading in headers:
        contentText.clear()
        headingText = heading.text

        # determine if next element is heading
        nextSibling: object = heading.next_sibling
        # while nextSibling is None:
        #  nextSibling: object = heading.next_sibling

        # print("\n\nNEW ELEMENT")
        # print("HEADING")
        # print(nextSibling.name)

        # next sibling is not a header or blank
        while nextSibling is not None and nextSibling.name not in h:
            if nextSibling is not None and nextSibling.name not in h and nextSibling.name in text:
                # perform analysis on text here
                if nextSibling.text != "\n":
                    contentText.append(nextSibling.text)
            nextSibling = nextSibling.next_sibling

        # create current row and add to allRows
        urlList = [url]
        headingList = [headingText]
        currentRow = teamInfo + urlList + headingList + contentText
        # print(currentRow)
        allRows.append(currentRow)

    return allRows


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

# prints team list
# for team in allData:
# print(team)

# prints keys
"print(teamData.keys())"

# prints teamData (all columns)
# pd.options.display.width
# pd.set_option('display.width', None)
# print(teamData)

# test an individual page with returnUrls

# create list for all output data
outputList = []

# counter for what team we are on
y = 1
length = len(allData)
for team in allData:
    # counter
    print(str(y) + "/" + str(length))
    for url in team[1]:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        outputList.append(processPage(soup, team[0], url))
    y = y + 1

# turn list into Pandas dataframe
pd0 = pd.DataFrame(outputList[0])
pd1 = pd.DataFrame(outputList[1])
pd2 = pd.DataFrame(outputList[2])
pd3 = pd.DataFrame(outputList[3])

outputPandas = pd.concat([pd0, pd1, pd2, pd3], axis=0)

"""# prints keys
print(outputPandas.keys())

# prints teamData (all columns)

print(outputPandas)"""

# write dataframe to excel file
writeXLS = pd.ExcelWriter('iGEM_WEBSCRAPER_ALL_DATA.xlsx', engine='xlsxwriter')
outputPandas.to_excel(writeXLS, sheet_name="All_Teams", )
writeXLS.save()

"""for each in a:
    print(each)"""

# run first file
# this = return_webpage("https://2019.igem.org/Team:US_AFRL_CarrollHS")
# print(this.text)
