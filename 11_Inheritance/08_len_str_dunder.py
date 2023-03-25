class num:
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f"Decimal->{self.num}"
    def __len__(self):
        return 1
c=num(10)
print(c)
print(len(c))