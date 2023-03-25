class Student:
    no_of_students=100
    def showDetails(self):
        return f"Name = {self.name}\nRoll = {self.roll}\nSection = {self.section}"

anirban=Student()
sucho=Student()

anirban.name="Anirban"
anirban.roll=1
anirban.section="A"

sucho.name="Sucho"
sucho.roll=2
sucho.section="A"

print(anirban.showDetails())
# There int the function self is nothing but the argument
# as like here i'm sending anirban as the argument so anirban's
# details will be printed
# so here self means anirban