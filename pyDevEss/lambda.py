#lambda anonymous - function defined without any name
x=lambda i,y,z: i+y+z
print(x(1,2,3))

def new(i):
    return lambda x:x*i
double=new(2)
triple=new(3)
print(double(5))
print(triple(5))

addStuff=lambda val1,val2:(print(f"adding {val1} and {val2}"),val1 +val2) 
output=addStuff(3,4)
print(type(output))