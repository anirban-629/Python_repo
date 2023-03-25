class employee:
    num=100
    @classmethod
    def change_num(cls,new_num):
        cls.num=new_num
        # herer cls mean class that means e.change_num means class employee()

e=employee()
print(e.num)
e.change_num(200)
print(e.num)
