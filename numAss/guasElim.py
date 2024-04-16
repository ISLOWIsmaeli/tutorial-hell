print("""Welcome to the Gaussian 
      elimination method calculator.
      Please follow the instructions
      given below.\n""")# Print a welcoming message

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

matrix = [] # Initialize the matrix
#Allow entry of matrix values
for i in range(row):
    row_numbers = []
    for j in range(column):
        number = float(input(f"Enter the number for matrix[{i+1}][{j+1}]: "))
        row_numbers.append(number)
    matrix.append(row_numbers)


for i in range(row - 1):  #  Forward Elimination
    pivot_row = i
    while pivot_row < row and matrix[pivot_row][i] == 0:
        pivot_row += 1
    if pivot_row == row:
        print("No solution exists")
        exit()

    if pivot_row != i:  #  Swap rows if necessary
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

    for j in range(i + 1, row):  # Elimination
        multiplier = matrix[j][i] / matrix[i][i]
        for k in range(i, column):
            matrix[j][k] -= multiplier * matrix[i][k]


if matrix[row - 1][row - 1] == 0:
    print("No solution exists")
    exit()


solution = [0] * row
solution[row - 1] = matrix[row - 1][column - 1] / matrix[row - 1][row - 1]
for i in range(row - 2, -1, -1):
    sum_val = matrix[i][column - 1]
    for j in range(i + 1, row):
        sum_val -= matrix[i][j] * solution[j]
    solution[i] = sum_val / matrix[i][i]

print("""The final reduced matrix is:\n""")
for i in range(row):
    print("|",end="")
    for j in range(column):
        print(matrix[i][j],end=" ")
    print("|",end="\n")
        
print("\nThe solution is:", solution)

for i in solution:
    # print(f"x{i+1} = ",solution[i],end="\n")
    print(int(solution[i]))
