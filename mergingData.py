import pandas as pd
import numpy as np

# import data
df = pd.read_excel('All_Data_PROCESSED.xlsx', header=None, index_col=False)
print("Data imported")

# processing data
dataArray = df.to_numpy()
i = 0
allData = []
count = 1
data = ""
print("Data processing beginning.")
x = 0
y = x + 1
length = len(dataArray)
print(length)
while y < length and x < length:
    y = x + 1
    heading = str(dataArray[x][7])
    text = str(dataArray[x][8])
    if heading != "nan" and text != "nan":
        data = data + heading + ": " + text
    elif heading != "nan" and text == "nan":
        data = data + heading
    elif heading == "nan" and text != "nan":
        data = data + text
    while y < length and dataArray[x][6] == dataArray[y][6]:
        heading = str(dataArray[y][7])
        text = str(dataArray[y][8])
        if heading != "nan" and text != "nan":
            data = data + heading + ": " + text
        elif heading != "nan" and text == "nan":
            data = data + heading
        elif heading == "nan" and text != "nan":
            data = data + text
        y = y + 1
        print(x)
        print(y)
    data = data.replace("\\n", "")
    newRow = [dataArray[x][0], dataArray[x][1], dataArray[x][2], dataArray[x][3], dataArray[x][4], dataArray[x][5],
              dataArray[x][6], data]
    x = y
    allData.append(newRow)
    data = ""

# print processed data to excel
print("Data finished processing. Printing to Excel.")
allDataDF = pd.DataFrame(data=allData)
writer = pd.ExcelWriter('All_Data_CONDENSED_PROCESSED.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
allDataDF.to_excel(writer, index=False, header=False)
writer.close()
