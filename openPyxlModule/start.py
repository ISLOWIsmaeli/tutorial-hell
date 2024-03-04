from openpyxl import Workbook, load_workbook

# wb = load_workbook('C:\\Users\\Lennox\\documents\\myProjects\\tutorials\\tutorial-hell\\openPyxlModule\\grades.xlsx')
# ws = wb['Grades']
# wb.create_sheet("Test")
# print(wb.sheetnames)
wb=Workbook()
ws=wb.active
ws.title = "Data"

ws.append(['Lennox','Is','Great','!'])
ws.append(['Lennox','Is','Great','!'])
ws.append(['Lennox','Is','Great','!'])
ws.append(['End',])
wb.save('ismael.xlsx')
