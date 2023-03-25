class Calculator:
    workFunc="Calculating"
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"Square-->>{self.num**2}")
    def squareroot(self):
        print(f"Square-->>{self.num**.5}")
    def cube(self):
        print(f"Square-->>{self.num**3}")

c=Calculator(10)
c.square()
c.squareroot()
c.cube()
