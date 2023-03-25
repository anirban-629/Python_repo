class A:
    def __init__(self):
        print("Google")

class B(A):
    def __init__(self):
        super().__init__()
        print("Microsoft")

class C(B):
    def __init__(self):
        super().__init__()
        print("OkCredit")

last=C()
