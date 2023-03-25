def gen(n):
    for i in range(n):
        yield i

def func(n):
    for i in gen(n):
        print(i)

# func(100)

obj1=gen(5)
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1)) # -> will throw error 

string='anirban'
iteratedChar=iter(string)

print(next(iteratedChar))
print(next(iteratedChar))
print(next(iteratedChar))
print(next(iteratedChar))
print(next(iteratedChar))
print(next(iteratedChar))
print(next(iteratedChar))
print(next(iteratedChar))