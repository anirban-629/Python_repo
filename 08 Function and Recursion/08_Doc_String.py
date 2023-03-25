def function(a,b,c):
    """Here we'll do a+b then /c
1st sentence in function is called docstring"""
    return f"A+B/C-->>{(a+b)/c}"

a=10
b=10
c=10
print(function.__doc__)
print(function(a,b,c))



