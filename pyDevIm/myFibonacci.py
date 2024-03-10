def sampleFibonacci(n): 
    store1=0
    store2=1
    final=0
    if n < 1:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(0,n-2,1):
            final=store1+store2
            store1=store2
            store2=final
        return final
    
def recursiveFibbonacci(n):
    if n <0:
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibbonacci(n-1)+recursiveFibbonacci(n-2)
    
term=int(input("Enter the nth term (positive integer from 1) for fibonacci sequence: "))
output1=recursiveFibbonacci(term-1)
output2=sampleFibonacci(term)
print("Recursive function = ",output1)
print("For loops = ", output2)
