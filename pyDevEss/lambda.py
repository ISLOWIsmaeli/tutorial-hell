#lambda anonymous - function defined withou any name
x=lambda i,y,z: i+y+z
print(x(1,2,3))

def new(i):
    return lambda x:x*i
double=new(2)
triple=new(3)
print(double(5))
print(triple(5))