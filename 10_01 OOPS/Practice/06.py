class Programmer:
    companyName="Microsoft"
    def __init__(slf,no,name,salary,code,):
        slf.no=no
        slf.name=name
        slf.salary=salary
        slf.code=code
    def printInfo(self):
        print(f"No<{self.no}>\nName--> {self.name}\nSalary-->{self.salary}\nCode-->{self.code}\n")

a=Programmer(1,"Anirban","50K",100)
b=Programmer(2,"Sucho","60K",200)
a.printInfo()
b.printInfo()

# Yes We can change the self parameter but we should'nt do that beacuse
# whenever other programmer will do work on that they may confused