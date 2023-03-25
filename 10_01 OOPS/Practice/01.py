class Programmer:
    companyName="Microsoft"
    def __init__(self,no,name,salary,code,):
        self.no=no
        self.name=name
        self.salary=salary
        self.code=code
    def printInfo(self):
        print(f"No<{self.no}>\nName--> {self.name}\nSalary-->{self.salary}\nCode-->{self.code}\n")

a=Programmer(1,"Anirban","50K",100)
b=Programmer(2,"Sucho","60K",200)
a.printInfo()
b.printInfo()