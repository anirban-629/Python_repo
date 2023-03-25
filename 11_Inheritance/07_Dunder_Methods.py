class number:
    def __init__(self,num):
        self.num=num

    def __add__(self, other):
        return self.num+other.num
    def __mul__(self, other):
        return self.num*other.num
    def __sub__(self, other):
        return self.num-other.num
    def __truediv__(self, other):
        return self.num/other.num
    def __floordiv__(self, other):
        return self.num // other.num

n1=number(100)
n2=number(25)
add=n1+n2
print("Addition Method __add__",add)
mul=n1*n2
print("Multiplication Method __mul__",mul)
sub=n1-n2
print("Substraction Method __sub__",sub)
div1=n1/n2
print("Division Method 1> __truediv__",div1)
div1=n1//n2
print("Division Method 2> __floordiv__",div1)
