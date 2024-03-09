from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active #selects first available sheet
sheet["A1"] = "hello"
sheet["B1"] = "world!"
workbook.save(filename="hello_world1.xlsx")