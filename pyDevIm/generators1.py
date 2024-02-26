def newUpTo(x):
    for i in range(x):
        yield i
seql= newUpTo(7)
print(next(seql))
print(next(seql))
print(next(seql))
print(next(seql))
print(next(seql))
print(next(seql))
print(next(seql))
