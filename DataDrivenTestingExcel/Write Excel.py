import openpyxl

path = "F:/Selenium/Dummy2.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.get_sheet_by_name('Sheet2')

for r in range(1, 4):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "Welcome"

workbook.save(path)