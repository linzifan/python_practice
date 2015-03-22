# coding: utf-8
import xlwt
import json

file_name = "city.txt"
def txt2xls(file_name):
    txt = open(file_name, "r")
    data = json.load(txt)
    book =xlwt.Workbook(encoding = 'utf-8')
    sheet =book.add_sheet(file_name.rstrip("txt").rstrip("."))
    for i in range(len(data)):
        obs = data[str(i+1)]
        sheet.write(i, 0, i+1) # start from row 0, column 0
        sheet.write(i, 1, obs)
    book.save(file_name.rstrip("txt").rstrip(".")+".xls")

if __name__ == "__main__":
    txt2xls("city.txt")
