print("""Welcome to the Gaussian 
      elimination method calculator.
      Please follow the instructions
      given below.\n""")

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

# Input the matrix
matrix = []
for i in range(row):
    row_numbers = []
    for j in range(column):
        number = float(input(f"Enter the number for matrix[{i+1}][{j+1}]: "))
        row_numbers.append(number)
    matrix.append(row_numbers)

# Gaussian Elimination Method
for i in range(row - 1):  # Step 1: Forward Elimination
    pivot_row = i
    while pivot_row < row and matrix[pivot_row][i] == 0:
        pivot_row += 1
    if pivot_row == row:
        print("No unique solution exists")
        exit()

    if pivot_row != i:  # Step 3: Swap rows if necessary
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

    for j in range(i + 1, row):  # Step 4: Elimination
        multiplier = matrix[j][i] / matrix[i][i]
        for k in range(i, column):
            matrix[j][k] -= multiplier * matrix[i][k]

# Check if the system is consistent
if matrix[row - 1][row - 1] == 0:
    print("No unique solution exists")
    exit()

# Backward Substitution
solution = [0] * row
solution[row - 1] = matrix[row - 1][column - 1] / matrix[row - 1][row - 1]
for i in range(row - 2, -1, -1):
    sum_val = matrix[i][column - 1]
    for j in range(i + 1, row):
        sum_val -= matrix[i][j] * solution[j]
    solution[i] = sum_val / matrix[i][i]

# Output the solution
print("\nThe solution is:", solution)
