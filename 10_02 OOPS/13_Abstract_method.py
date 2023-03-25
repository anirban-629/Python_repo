# from abc import ABCMeta,abstractmethod
# metaclass=ABC

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    # That means that we must have to make this function in child classes
    def area(self):
        pass

class rectangle(shape):
    def __init__(self):
        self.length=10
        self.width=20
    def area(self):
        return self.length*self.width

r=rectangle()
print(r.area())