class employee1:
    var11="Anirban in EMPLOYEE1"
    def __init__(self):
        self.var111="Rahul in __init__11"
        self.var112="Variable in __init__11"
        self.var113="Special"
class employee2(employee1):
    var21="Babai in EMPLOYEE2"
    def __init__(self):
        super().__init__()
        self.var221="Rahul in __init__22"
        self.var222="Variable in __init__22"

e1=employee1()
e2=employee2()
print(e2.var111)
print(e2.var112)
print(e2.var113)