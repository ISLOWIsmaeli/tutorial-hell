# iterator from fruits tuple and print each value
# fruitstuple=("banana","lemon","apple")
# newit = iter(fruitstuple)

# print(next(newit))
# print(next(newit))
# print(next(newit))
# fruitstr="lemon"
# newit=iter(fruitstr)

# print(next(newit))  
# print(next(newit))
# print(next(newit))  
# print(next(newit))
# print(next(newit))  
# fruitstuple = ("banana","lemon","apple")
# fruitstr = "lemon"
# for i in fruitstuple:
#     print(i)
# for i in fruitstr:
#     print(i)
class Counting:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=19:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
newObbj=Counting()
newit=iter(newObbj)

for x in newit:
    print(x)