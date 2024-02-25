#used to create iterators, special functions, yield statement
def Item():
    print("First item")
    yield 15
    return

    print("Second item")
    yield 25

    print("Last item")
    yield 40

newGenerat = Item()

print(next(newGenerat))
print(next(newGenerat))
print(next(newGenerat))
print(next(newGenerat))