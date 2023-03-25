class Employee:
    def __init__(self,myname,mysalary,myage):
        # name,salary and age is the instance variable
        # myname,mysalary and myage are arguments
        self.name=myname
        self.salary=mysalary
        self.age=myage
        print(f"Name: {myname}\nAge: {myage}\nSalary: {mysalary}")
        # No need to declare init automatically declares itself

e=Employee("Anirban",10000,30)
