class student:
    college="GMIT"
    def gdm9(self,name):
        return f"Good Morning "+name

    @staticmethod
    def gdn8(name):
        return "Good Night "+name

s=student()
print(s.gdm9("Anirban"))
print(s.gdn8("Rahul"))