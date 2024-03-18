from openpyxl import load_workbook
import random

filename="testData.xlsx"
workbook=load_workbook(filename)

no_of_sites=int(input("Please enter the number of sites: "))
site_names =[]

for i in range(no_of_sites):
    site_entry=input("Site {}".format(i+1))


