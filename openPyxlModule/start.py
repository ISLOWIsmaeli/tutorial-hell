from openpyxl import workbook, load_workbook

wb = load_workbook('C:\\Users\\Lennox\\documents\\myProjects\\tutorials\\tutorial-hell\\openPyxlModule\\grades.xlsx')
ws = wb.active
print(ws['A1'].value)

