import openpyxl
import os
from Excel import filepath

cwd = os.getcwd()
filename = "df.xlsx"
filename = os.path.join(cwd, "output", filename)

wb = openpyxl.load_workbook(filepath)
ws = wb['Sheet1']

# 열,행 객체
cols = tuple(ws.columns)
rows = tuple(ws.rows)

print(cols[0])
print(rows[0])

for col_idx, col in enumerate(cols):
    for each_cell in col:
        print("%s번째 열: %s" % (col_idx, each_cell))

a3 = cols[0][2]
print(a3.value)
a3.value = 'row1'
print(a3.value)

wb.save(os.path.join(cwd, "output", "df3.xlsx"))