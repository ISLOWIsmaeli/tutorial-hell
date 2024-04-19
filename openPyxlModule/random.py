import pandas as pd
from openpyxl import load_workbook
import random

data_from_excel=pd.read_excel()
names_data_list=[]
campus_data_list=[]
gender_data_list=[]
year_data_list=[]

tuple_list=[]
final_list=[]

for person in data_from_excel.values:
    names_data_list.append(person[0])
    campus_data_list.append(person[1])
    gender_data_list.append(person[2])
    year_data_list.append(person[3])
    tuple_list = zip(
        names_data_list,
        campus_data_list,
        gender_data_list,
        year_data_list
    )
    sites_with_allocated_people={}
    people_data_copy=final_list.copy()
    for site_index in range(len(final_list)):
        selected_person= random.choice(people_data_copy)
        try:
            sites_with_allocated_people[site_index%5].append(selected_person)
        except KeyError as site_not_yet_created:
            sites_with_allocated_people[site_index%5] = [selected_person]
        people_data_copy.remove(selected_person)

    print(sites_with_allocated_people)
    pd.set_option("display.max_columns",None)
    print(pd.DataFrame({key:pd.Series(value) for key, value in sites_with_allocated_people.items}))