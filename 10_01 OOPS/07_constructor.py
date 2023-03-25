class Employee:
    companyName="Google"
    # def __init__(self):
    #     pass
    # we don't need to call this function as it's a constructor??

    def __init__(self,name,salary):
        # We can take arguments here also
        self.name=name
        self.salary=salary
        print(f"Company name created....!!\nName: {self.name}\nSalary: {self.salary}\nCompany: {self.companyName}")

    def getDetails(self):
        print(f"Name={self.name}\nSalary={self.salary}")

anirban = Employee("Anirban",100)
# a.name="Anirban"
# a.salary="100K"
anirban.getDetails()
