from openpyxl import load_workbook
filename="groupings.xlsx"
workbook = load_workbook(filename)
mysheets = workbook.sheetnames
sheet1 = workbook.active
print(sheet1)