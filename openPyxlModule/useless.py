import pandas as pd
import random

data_from_class_list=pd.read_excel("C:\\Users\\Lennox\Documents\\myProjects\\tutorials\\tutorial-hell\openPyxlModule\\NUMERICAL METHODS CLASS LIST (1).xlsx")
regno_data_list=[]
names_data_list=[]

tuple_list=[]
final_list=[]

for student in data_from_class_list:
    regno_data_list.append(student[0])
    names_data_list.append(student[1])
    tuple_list=zip(regno_data_list,names_data_list)
final_list=list(tuple_list)

groups_with_allocated_students={}
students_data_copy=final_list.copy()

for group_index in range(len(final_list)):
    selected_student=random.choice(students_data_copy)
    try:
        groups_with_allocated_students[group_index%5].append(selected_student)
    except KeyError as group_not_yet_created:
        groups_with_allocated_students[group_index%5]=[selected_student]
    students_data_copy.remove(selected_student)
print(groups_with_allocated_students)
