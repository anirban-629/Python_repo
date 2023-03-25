def show(normal,*args,**kwargs):
    # Here args and kwargs are just a name you can give it any name
    # But here args is a tuple may be it's a tuple or list but
    # in function it's a tuple
    # print(args)
    print(normal)
    print("Args-->")
    for item in args:
        print(item)

    print("Kwargs->")
    for key,item in kwargs.items():
        print(f"{key}:{item}")

normal="This is a normal Argument which we have to keep in \nfirst in the function otherwise it'll throw error\n"

list=["Anirban","Sucho","Sourin","Rajda"]

dict={"I":"ANIRBAN","She":"SUCHO","He1":"SOURIN","He2":"RAJDA"}

show(normal,*list,**dict)

