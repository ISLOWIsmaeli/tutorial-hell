print("""Welcome to the row 
      echelon method calculator.
      Please follow the instructions
      given below.\n""")

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

matrix = []

for i in range(row):
    row_numbers = []
    for j in range(column):
        number = float(input(f"Enter the number for matrix[{i+1}][{j+1}]: "))
        row_numbers.append(number)
    matrix.append(row_numbers)

def gaussian_elimination(matrix):
    row = len(matrix)
    column = len(matrix[0])

    for i in range(row):
        pivot_row = i
        while pivot_row < row and matrix[pivot_row][i] == 0:
            pivot_row += 1
        if pivot_row == row:
            continue

        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        for j in range(i + 1, row):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, column):
                matrix[j][k] -= ratio * matrix[i][k]

gaussian_elimination(matrix)

print("\nThe matrix in row echelon form is:")
for row in matrix:
    print(row)
