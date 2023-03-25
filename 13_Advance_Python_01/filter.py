def greaterThan(n):
    if(n<2):
        False
    else:
        return True

l1=[0,1,2,3,4,5,6,7,8,9]
l2=list(filter(greaterThan,l1))
print(l2)