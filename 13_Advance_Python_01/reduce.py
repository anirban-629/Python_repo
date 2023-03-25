from functools import reduce

def add(a,b):
    return a+b

l1=[0,1,2,3,4,5,6,7,8,9]
l2=reduce(add,l1)
print(l2)

'''
0+1=1
1+2=3
3+3=6
6+4=10
10+5=15
15+6=21
21+7=28
28+8=36
36+9=45 -> ans
'''