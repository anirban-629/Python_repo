"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def generator(n):
    for i in range(n):
        yield i

g=generator(100000102400120301230120)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())

name="Anirban"
iter=iter(name)
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())

