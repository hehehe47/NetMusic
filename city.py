import openpyxl
from xlrd import open_workbook
import MongoDB


def get_citylist(cityData, sheet):
    for row in range(2, 3546):
        city_id = sheet['A' + str(row)].value
        city_name = sheet['B' + str(row)].value
        cityData[city_id] = city_name


def get_city(city_ID):
    if city_ID in cityData.keys():
        city_NAME = cityData.get(city_ID)
    else:
        city_NAME = 'else'
    return city_NAME


wb = openpyxl.load_workbook('city.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
cityData = {}
get_citylist(cityData, sheet)



# city_ID = 1001600
# city_NAME = get_city(city_ID)
# print(city_NAME)
# print(city_NAME)
