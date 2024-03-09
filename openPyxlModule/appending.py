from openpyxl import load_workbook
workbook = load_workbook(filename="hello_world.xlsx")
sheet=workbook.active
sheet["C1"]="writing ;)"
workbook.save(filename="hello_world_append.xlsx")