# def newOut():
#     x=200
#     def newIn():
#         print(x)
#     newIn()
# newOut()
# x =100

# def newfunc():
#     print(x)

# newfunc()
# print(x)
# x=100
# def newfunc():
#     x=50
#     print(x)
# newfunc()
# print(x)
x=100
def newfunc():
    global x
    x=50

newfunc()

print(x)