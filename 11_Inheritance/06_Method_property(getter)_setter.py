class employee:
    company="Google"
    salary=100000
    bonus=8000
    @property
    def total(self):
        # Thats how total is not a function now it's works like a normal
        return self.salary+self.bonus

    @total.setter
    def total(self,val):
        # Thats how we can set the salary
        self.bonus=val-self.salary


e=employee()
print(e.total)
e.total=169999
print(e.salary)
print(e.bonus)
