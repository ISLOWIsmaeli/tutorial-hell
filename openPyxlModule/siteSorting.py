from openpyxl import load_workbook
import random

filename="testData.xlsx"
workbook=load_workbook(filename)

sites=int(input("Enter the number of sites"))

for i in range(sites):
    print(i)