# 1
# List Comprehensions
# # l1=[]
# # for i in range(100):
#     # if i%3==0:
#         # l1.append(i)
# # print(l1)
# l1=[i for i in range(100) if i%3==0]
# print(l1)
# # This is called the list comprehension

# 2
# # Dictionary Comprehensions
# dict={i:f"ITEM-> {i}" for i in range(5)}
# print(dict)
# dict_reverse={value:key for key,value in dict.items()}
# print(dict_reverse)

# 3
# # Set Comprehensions
# set1={set for set in ["A","A","D","A","D","A"]}
# print(set1)
# print(type(set1))

# 4
# Generator Comprehensions
g1=(i for i in range(100) if i%2==0)
print(type(g1))
print(g1)
print(g1.__next__())
print(g1.__next__())