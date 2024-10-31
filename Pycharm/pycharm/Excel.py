import openpyxl
import os

# Excel 파일 경로 지정
cwd = os.getcwd()
filename = "df.xlsx"
filepath = os.path.join(cwd, "output", filename)

# 워크북 객체
wb = openpyxl.load_workbook(filepath)
print(wb)
print(type(wb))
print(wb.sheetnames)

# 시트 객체
ws = wb['Sheet1']
print(ws)
print(ws.title)

active_sheet = wb.active
print(active_sheet)
