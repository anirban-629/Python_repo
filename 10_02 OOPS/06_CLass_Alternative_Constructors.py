class employee:
    quota=100
    def __init__(self,name,salary,code):
        self.name=name
        self.salary=salary
        self.code=code
        print(f"{name},{salary},{code}")

    @classmethod
    def change_quota(cls,num):
        cls.quota=num

    @classmethod
    def from_dash_to_list(cls,str):
        # a=str.split("-")
        # return cls(a[0],a[1],a[2])
        return cls(*str.split("-"))

# e=employee("Anirban",10000,110)
# print(e.quota)
# e.change_quota(200)
# print(e.quota)
d=employee.from_dash_to_list("Rahul-100-100")
print(d.salary)