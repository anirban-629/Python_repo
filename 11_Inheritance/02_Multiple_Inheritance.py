class a:
    company="Google"
    code=100

class b:
    company="Microsoft"
    level=0
    def plusLevel(self):
        self.level=self.level+1

class c(a,b):
    Name="Anirban"

i=c()
print(c.company)
# Here Google will be printed always beacuse 1st priority is a..
print(i.code)
print(i.level)
i.plusLevel()
print(i.level)
print(i.Name)