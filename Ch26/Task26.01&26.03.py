#Jenny Zhan
import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID=''
        self.Registration=''
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00
class DataAndFile:
    def __init__(self,x,n):
        self.Car=x
        self.number=n
    def Save(self):
        CarFile=open('Cars.DAT','wb')
        for i in range(self.number):
            pickle.dump(self.Car[i],CarFile)
        CarFile.close()
    def Load(self):    
        CarFile=open('Cars.DAT','rb')
        self.Car=[]
        while True:
            try:self.Car.append(pickle.load(CarFile))
            except:break
        CarFile.close()
    def Display(self):
        for i in range(self.number):
            print(self.Car[i].VehicleID,self.Car[i].Registration,self.Car[i].DateOfRegistration,
                  self.Car[i].EngineSize,self.Car[i].PurchasePrice)
class main:
    def __init__(self,n=5):
        self.number=n
        self.Car=[]
        self.run()
    def run(self):
        for i in range(self.number):
            ThisCar=CarRecord()
            ThisCar.VehicleID=input("What's the vehicle ID?")
            ThisCar.Registration=input("What's the Registration?")
            ThisCar.DateOfRegistration=input("What's the date of registration?")
            ThisCar.EngineSize=input("What's the engine size?")
            ThisCar.PurchasePrice=input("What's the purchase price?")
            self.Car.append(ThisCar)
        A=DataAndFile(self.Car,self.number)
        A.Save()
        A.Load()
        A.Display()
if __name__=='__main__':
    main()
