class employee:
    companyName="Google"
    def getsalary(self):
        print(f"salary package = {self.salary} lacs per annum ")

anirban=employee()
anirban.salary= 40
anirban.getsalary()

# Same meaning-
# anirban.getsalary() = employee.getsalary(anirban)

