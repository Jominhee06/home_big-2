import openpyxl
import os

# 워크북 객체 만들기
wb = openpyxl.Workbook()
print(wb.sheetnames)

wb.save(os.path.join(os.getcwd(), "output", "create_workbook.xlsx"))