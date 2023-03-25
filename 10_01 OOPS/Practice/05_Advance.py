class train:
    trainName="RAJDHANI EXPRESS"
    def __init__(self,seats,source,destin):
        self.seats=seats
        self.source=source
        self.destin=destin
    def showInfo(self):
        print(f"Seats Availabe-> {self.seats}\nSource Station-> {self.source}\nDestination-> {self.destin}")

    def bookSeat(self,num):
        seat=self.seats
        self.num=num
        if(num>0 and num<=seat):
            print(f"{self.num} Seats Booked")
            seat=seat-self.num
        elif(num==0):
            print("No seats booked")
        else:
            print(f"Only {seat} seats available")

while(1):
    a=train(10,"HOWRAH","NEW DELHI")
    a.showInfo()
    n=int(input("Enter how many seats You want to book-->> "))
    a.bookSeat(n)
    a=int(input("1/0"))
    if(a==0):
        exit()
