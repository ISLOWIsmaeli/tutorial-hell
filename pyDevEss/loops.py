# continue and break keywords.
# you cannot use else statement when you use break in python
x=0
while x <7:
    x = x + 1
    if x == 3 :
        continue
    print(x)
else:
    print("x is no longer less than 7")

#for loops
fruits=["banana","orange","apple"]
for item in fruits:
    print(item)