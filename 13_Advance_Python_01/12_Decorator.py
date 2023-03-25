'''
def function(funct):
    funct("ANIRBAN")
function(print)
'''

# Here argument is print function
# funct=print

def func1(func2):
    def func3():
        print("HELLO")
        func2()
        print("ANIRBAN")
    return func3

# @func1 => func3=func1(func3)

@func1
def func3():
    print("I'm")

func3()