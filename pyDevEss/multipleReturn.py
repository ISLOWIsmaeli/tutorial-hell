def subtractAddDivide(val1,val2):
    sub=val1-val2
    add=val1+val2
    div=val1/val2
    return sub, add, div
print("Enter two numbers to return multiple values: \n")
val1=input("Enter first Number: ")
val2=input("Enter second Number: ")
print(subtractAddDivide(int(val1),int(val2)))