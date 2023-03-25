def square(n):
    return n**2

l1=[0,1,2,3,4,5,6,7,8,9]
# l2=list(map(square,l1)) # map(name of function,list of input)
l2=map(square,l1)  
print(l2)
print(list(l2))