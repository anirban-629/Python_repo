# Base/Mother class
class employee:
    company="Google"
    def show(self):
        print(f"Company name is -> {self.company}")
    def details(self):
        print("This is Google")
# Child/Derived class
class programmer(employee):
    Name="Youtube"
    # OverWriting the company name
    def show(self):
        print(f"Company name is -> {self.Name}")
    def showDetails(self):
        print(f"Hi this is Inheritance")

e=employee()
e.show()
p=programmer()
p.show()
p.showDetails()
print(p.company)
p.details()
# That's how inheritance works..