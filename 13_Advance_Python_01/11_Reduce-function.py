from functools import reduce
list=[1,2,3,4]
sum_of_list=reduce(lambda x,y:x*y,list)
print(sum_of_list)