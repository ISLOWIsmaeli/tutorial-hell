# iterator from fruits tuple and print each value
fruitstuple=("banana","lemon","apple")
newit = iter(fruitstuple)

for item in fruitstuple:
    print(next(newit))
    print(next(newit))


# print(next(newit))
# print(next(newit))
