from openpyxl import load_workbook,Workbook
filename="groupings.xlsx"
workbook = load_workbook(filename)
mysheets = workbook.sheetnames
print(mysheets)
class_list_sheet=workbook[mysheets[0]]
projects_without_ismael_sheet=workbook[mysheets[1]]
projects_with_ismael_sheet=workbook[mysheets[2]]

classmates_with_groups=[]

for class_list in class_list_sheet.iter_rows(min_row=3,
                                             max_row=128,
                                             min_col=2,
                                             max_col=2,
                                             values_only=True):
    classmate1=class_list[0]
    for without_ismael in projects_without_ismael_sheet.iter_rows(min_row=2,
                                                                  max_row=120,
                                                                  min_col=3,
                                                                  max_col=3,
                                                                values_only=True):
        classmate2=without_ismael[0]
        if classmate1==classmate2:
            print(classmate1,"has a group")
            classmates_with_groups.append(classmate1)
            break
        else:
            pass
    
print(classmates_with_groups)
