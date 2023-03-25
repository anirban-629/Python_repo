class first:
    company="Google"
    code1=100
    def upgrade(self):
        self.code1=self.code1+1

class second(first):
    company = "Microsoft"
    code2=1000
    def upgrade(self):
        self.code1=self.code1+1

class third(second):
    name="Anirban"

rahul=third()
print(rahul.code1)
rahul.upgrade()
print(rahul.code1)
# We can access all the classes from the third but
# the same value will be taken from the upgraded
# as here if company then it'll be taken from the second