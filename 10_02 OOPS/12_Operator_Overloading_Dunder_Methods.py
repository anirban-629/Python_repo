class employee:
    def __init__(self,name,salary,age):
        self.n=name
        self.s=salary
        self.a=age
        # print(f"Name-> {name}\nSalary-> {salary}\nAge-> {age}")
    def printdetails(self):
        return f"Name-> {self.n}\nSalary-> {self.s}\nAge-> {self.a}"
    def __add__(self, other):
        return self.a+ other.a
    def __mul__(self, other):
        return self.a* other.a
    def __repr__(self):
        return self.printdetails()
    def __str__(self):
        return "Hello this is employee class"
e1=employee("Anirban",30000,20)
e2=employee("Sucho",20000,20)
# print(e1+e2)
# print(e1*e2)
# print(e1)
# str is more higher in priority than repr
# print(repr(e1))
# print(str(e1))
print(e1)#This will print str