print("""Welcome to the gaussian 
      elimination method calculator
      please follow the instructions
      given below \n""")
row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))

matrix=[]
for i in range(row):
    row_numbers=[]
    for j in range(column):
        number=int(input(f"Enter the number for matrix[{i+1}][{j+1}]: "))
        row_numbers.append(number)
    matrix.append(row_numbers)
print(matrix)