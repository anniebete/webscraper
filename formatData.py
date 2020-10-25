import pandas as pd
import numpy as np


def printRow(cell):
    column = cell[1:-1]
    x = column.split(',')

    for each in x:
        if each != ', ' and each != '[' and each != ']':
            # print(each)
            team = x[0]
            team = team[1:-1]
            continent = x[1]
            continent = continent[2:-1]
            country = x[2]
            country = country[2:-1]
            size = x[5]
            size = size[2:-1]
            year = x[7]
            year = year[2:-1]
            wikiURL = x[8]
            wikiURL = wikiURL[2:-1]
            pageURL = x[10]
            pageURL = pageURL[2:-1]
            heading = x[11]
            heading = heading[2:-1]

            # get content
            data = ""
            for position in range(12, len(x)):
                data += x[position]
            """print("Team: " + team)           """
            """print("Continent: " + continent) """
            """print("Country: " + country)     """
            """print("Size: " + size)           """
            """print("Year: " + year)           """
            """print("WikiURL: " + wikiURL)     """
            """print("Page: " + pageURL)        """
            """print("Heading: " + heading)     """
            """print("Data: " + data)           """
            allData = [team, continent, country, size, year, wikiURL, pageURL, heading, data]
            # print(allData)
    return allData


# import sample data
df = pd.read_excel('iGEM_WEBSCRAPER_ALL_DATA - no indices.xlsx', header=None, index_col=False)
print("Data imported")

# processing data
dataArray = df.to_numpy()
i = 0
allData = []
count = 1
print("Data processing beginning.")
for row in dataArray:
    for column in row:
        if not pd.isnull(column):
            allData.append(printRow(column))
            print(count)
            count = count + 1

# print processed data to excel
print("Data finished processing. Printing to Excel.")
allDataDF = pd.DataFrame(data=allData)
writer = pd.ExcelWriter('All_Data_PROCESSED.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
allDataDF.to_excel(writer, index=False, header=False)
writer.close()