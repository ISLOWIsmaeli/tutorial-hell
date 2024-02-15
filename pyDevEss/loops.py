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

fruit = "banana"
for x in fruit:
    print(x)
    if x == "n":
        break
#last item is not included in the loop
for x in range(0,74,3):
    print(x)
else: 
    print("says what to do after for loop completes")