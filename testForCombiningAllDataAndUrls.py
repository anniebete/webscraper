import csv

# the goal of this script was to test how combining "TEST - iGEM Teams.cvs" and "TEST - iGEM URLs.cvs"
# this goal was accomplished
with open('TEST - iGEM Teams.txt.csv', newline='') as file:
    reader = csv.reader(file)
    teamData = list(reader)

with open('TEST - iGEM URLs.csv', newline='') as file:
    reader = csv.reader(file)
    urls = list(reader)

allData = list(zip(teamData, urls))

# prints team list
for team in allData:
    print(team[0][0])
    print("\n")

