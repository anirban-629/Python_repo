'''
                                                                    Example

1> Public variables are those variable which can be accesed         public
2> Protected variables are those variable which can be accessed
by that class                                                       _protected
3> Public are those which can't be accessed easily only without
that particular class using below method described below            __private

'''

class employee:
    public=100
    _protected=200
    __private=300
    def greet(self):
        print("Hello")

class boss(employee):
    def exit(self):
        print("Bye")


b=boss()
b.exit()
b.greet()
e=employee()
print(e.public)
print(employee()._protected)
print(e._employee__private)
