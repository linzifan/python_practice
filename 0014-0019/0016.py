# coding: utf-8
import xlwt
import json


def txt2xls(file_name):
    txt = open(file_name, "r")
    data = json.load(txt)
    book =xlwt.Workbook(encoding = 'utf-8')
    sheet =book.add_sheet(file_name.rstrip("txt").rstrip("."))
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j])
    book.save(file_name.rstrip("txt").rstrip(".")+".xls")

if __name__ == "__main__":
    txt2xls("numbers.txt")
