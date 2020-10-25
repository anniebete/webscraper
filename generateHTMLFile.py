import pandas as pd
import numpy as np
import xlrd

"""
def printRow(row):
    # print td for first few columns
    print("    <tr>")
    print("      <td>" + team + "</td>")
    print("      <td>" + region + "</td>")
    print("      <td>" + country + "</td>")
    print("      <td>" + track + "</td>")
    print("      <td>" + section + "</td>")
    print("      <td>" + size + "</td>")
    print("      <td>" + status + "</td>")
    print("      <td>" + year + "</td>")
    print("      <td>" + mainURL + "</td>")
    print("      <td>" + teamID + "</td>")
    print("      <td>" + pageURL + "</td>")
    print("      <td>" + pageHeader + "</td>")
    print("    </tr>")
    # combine data for the content columns

    #print content column
    print("      <td>" + pageContent + "</td>")"""


def printHeading():
    # print the start of the HTML document
    print("{{OhioState}}")
    print("<html>")
    print("<!-- MDBootstrap Datatables  -->")
    print(
        "<link href=\"https://2020.igem.org/wiki/index.php?title=Template:OhioState/databaseCSS&action=raw&ctype=stylesheet\" rel=\"stylesheet\">")
    print("<!-- MDBootstrap Datatables  -->")
    print(
        "<script type=\"text/javascript\" src=\"https://2020.igem.org/wiki/index.php?title=Template:OhioState/databaseJS&action=raw&ctype=text/javascript\"></script>")
    print("<style>")
    print("table.dataTable thead .sorting:after,")
    print("table.dataTable thead .sorting:before,")
    print("table.dataTable thead .sorting_asc:after,")
    print("table.dataTable thead .sorting_asc:before,")
    print("table.dataTable thead .sorting_asc_disabled:after,")
    print("table.dataTable thead .sorting_asc_disabled:before,")
    print("table.dataTable thead .sorting_desc:after,")
    print("table.dataTable thead .sorting_desc:before,")
    print("table.dataTable thead .sorting_desc_disabled:after,")
    print("table.dataTable thead .sorting_desc_disabled:before {")
    print("  bottom: .5em;")
    print("}")
    print(".table {overflow-y: hidden}")
    print("</style>")
    print("<script>")
    print("$(document).ready(function () {")
    print("$('#dtBasicExample').DataTable();")
    print("$('.dataTables_length').addClass('bs-select');")
    print("});")
    print("</script>")
    print("<div class=\"main-content\">")
    print("<p></p>")
    print("<p></p>")
    print("<div class=\"table-responsive\">")
    print(
        "<table id=\"dtBasicExample\" class=\"table table-striped module table-bordered table-sm\" cellspacing=\"0\" width=\"100% overflow-y: hidden overflow-auto\">")
    print("  <thead>")
    print("    <tr>")
    print("      <th class=\"th-sm\">Team")
    print("      </th>")
    print("      <th class=\"th-sm\">Region")
    print("      </th>")
    print("      <th class=\"th-sm\">Country")
    print("      </th>")
    print("      <th class=\"th-sm\">Track")
    print("      </th>")
    print("      <th class=\"th-sm\">Section")
    print("      </th>")
    print("      <th class=\"th-sm\">Size")
    print("      </th>")
    print("      <th class=\"th-sm\">Status")
    print("      </th>")
    print("      <th class=\"th-sm\">Year")
    print("      </th>")
    print("      <th class=\"th-sm\">Main URL")
    print("      </th>")
    print("      <th class=\"th-sm\">Team ID")
    print("      </th>")
    print("      <th class=\"th-sm\">Page URl")
    print("      </th>")
    print("      <th class=\"th-sm\">Page Header")
    print("      </th>")
    print("      <th class=\"th-sm\">Page Content")
    print("      </th>")
    print("    </tr>")
    print("  </thead>")
    print("  <tbody>")


def printClosing():
    # print HTML close
    print("  </tbody>")
    print("</table>")
    print("</div>")
    print("</div>")
    print("</html>")


# get data from iGEM_WEBSCRAPER_ALL_DATA.xlsx
dataframe = pd.read_excel('iGEM_WEBSCRAPER_ALL_DATA - no indices - Copy.xlsx', nrows=1, header=None)
dataframeTF = dataframe.isnull()
# print(dataframe)

# set up excel spreadsheet
workbook = xlsxwriter.Workbook('iGEM_WEBSCRAPER_ALL_DATA - no indices - Copy.xlsx', sheet="NEW")

print(outputList)
print(outputPandas)
for x in range(0, 2):
    for number in range(0, 1077):
        if not dataframeTF[number][x]:
            dataframe2 = dataframeTF[number][x]
            for each in dataframe2[0]:
                workbook.write(each)

"""for column in dataframe:
    if column != "NaN":
        print(column[0])"""
"""print(dataframe[0][0])
print(dataframe[1][0])"""

# print HTML for each row
# printRow()

printClosing()
