class Employee:
    companyName="ABCD"
    def getData(self,declaration):
        print(f"Salary of {self.name}\n{declaration}")

    @staticmethod
    #For using function without self
    def greet():
        print("Visit Again.!")

a=Employee()
a.name="Anirban"
b=a.declaration="Thanks..!!"
a.getData(b)
a.greet()
