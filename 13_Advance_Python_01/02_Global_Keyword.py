x=10 #Global Variable
def anirban():
    # x=15
    # print("x is a local variable in anirban() x=",x)
    global x
    x=x+10
    print("Called the global Variable in anirban() x=x+10=",x)

anirban()
print('Here also variable has changed and now it is-> ',x)


def anirban2():
    y=20
    def rahul():
        global y
        y=50

    print(y,"-> anirban2()")
    rahul()
    print(y,"->rahul()")

anirban2()
print("In main function-> ",y)

