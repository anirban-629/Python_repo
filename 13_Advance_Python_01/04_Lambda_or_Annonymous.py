"""Lambda or Annonymous functions:
a=10
b=20
[def add(a,b):
    return a+b
print(add(a,b))]
or
[add=lambda a,b:a+b]
"""

a=[[13,23],[1,65],[70,12]]
a.sort(key=lambda x:x[0])
print(a)
"""That means lambda is a one type of function that takes the arguments and
make it as a normal function here x[0] means the 1st element in list of list to sort"""