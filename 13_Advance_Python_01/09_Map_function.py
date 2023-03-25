# Map
list1=["12","34","54","64","76","87"]
print(type(list1[1]))

# for i in range(len(list1)):
#     list1[i]=int(list1[i])
# print(type(list1[1]))

list1=list(map(int,list1))
print(type(list1[1]))

list2=[1,2,3,4,5,6]
list2=list(map(lambda x: x*x, list2))
print(list2)

def square(x):
    return x*x
def cube(x):
    return x*x*x

list3=[square,cube]
for i in range(10):
    list3_val=list(map(lambda x: x(i), list3))
    print(list3_val)