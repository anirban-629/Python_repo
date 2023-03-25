l1=[123,3,52,34,7,23,6,867,32,7,34,324,3658,2313,4,67,52,3,456,3,12432,375,3463,]
l2=[]
for ele in l1:
    if ele%3==0:
        l2.append(ele)

print('Using Iterative method -> ',l2)

print('Using Comprehension method -> ',[item for item in l1 if item%3==0])
