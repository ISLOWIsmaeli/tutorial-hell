# def newUpTo(x):
#     for i in range(x):
#         yield i
# seql= newUpTo(7)
# print(next(seql))
# print(next(seql))
# print(next(seql))
# print(next(seql))
# print(next(seql))
# print(next(seql))
# print(next(seql))
def squareSequence(x):
    for i in range(x):
        yield i*i
newGenerat=squareSequence(7)
# while True:
#     try:
#         print("Receive on the next()",next(newGenerat))
#     except StopIteration:
#         break  
for sqr in newGenerat:
    print(sqr)