class employee:
    name="Anirban"
    code=100
    salary=30000
    # def changeSal(self,sal):
    #     self.__class__.salary=sal
    @classmethod
    def changeSal(cls,sal):
        cls.salary=sal

e=employee()
print(f"e.salary->>{e.salary}")
print(f"Using functions changeSal-->> Done")
e.changeSal(50000)
print(f"Now e.salary-->>{e.salary}")
print("But class salary not changed instanced only")
print(f"Printing employee.salary-->>{employee.salary}")
print("using ""__class__"" or ""@classmethod"" we can change the salary in class")
print(f"Salary before change (employee.salary)-->> {employee.salary}")
e.changeSal(60000)
print(f"employee.salary-->>{employee.salary}")