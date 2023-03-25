class train:
    trainName="RAJDHANI EXPRESS"
    def __init__(self,seats,source,destin):
        self.seats=seats
        self.source=source
        self.destin=destin
    def showInfo(self):
        print(f"Seats Availabe-> {self.seats}\nSource Station-> {self.source}\nDestination-> {self.destin}")

a=train(500,"HOWRAH","NEW DELHI")
a.showInfo()