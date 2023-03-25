class A:
    def companyName(self):
        print("Google")

class B(A):
    def companyName(self):
        super().companyName()
        print("Microsoft")

class C(B):
    def companyName(self):
        super().companyName()
        print("OkCredit")

last=C()
last.companyName()

# super() method works to acces all the same named function in base class through childclass