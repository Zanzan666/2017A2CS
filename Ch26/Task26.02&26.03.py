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
    def LimitingLength(x,n):
        try:
            x[n-1]
            x=x[:n]
        except:
            x=x.ljust(n,'/')
        return x
    def Hash(ID):
        return ((ord(ID[0])+ord(ID[1]))%20)*32+1
    def Access(ID):
        CarFile=open('Cars.DAT','rb')
        CarFile.seek(DataAndFile.Hash(ID))
        ThisCar=pickle.load(CarFile)
        print(ThisCar.VehicleID,ThisCar.Registration,ThisCar.DateOfRegistration,ThisCar.EngineSize,ThisCar.PurchasePrice)
        CarFile.close()
class main:
    def __init__(self,n=5):
        self.number=n
        self.run()
    def run(self):
        print('input data now')
        CarFile=open('Cars.DAT','rb+')
        for i in range(self.number):
            ThisCar=CarRecord()
            ThisCar.VehicleID=DataAndFile.LimitingLength(input("What's the vehicle ID?"),8)
            ThisCar.Registration=DataAndFile.LimitingLength(input("What's the Registration?"),8)
            ThisCar.DateOfRegistration=DataAndFile.LimitingLength(input("What's the date of registration?"),8)
            ThisCar.EngineSize=DataAndFile.LimitingLength(input("What's the engine size?"),8)
            ThisCar.PurchasePrice=DataAndFile.LimitingLength(input("What's the purchase price?"),8)
            CarFile.seek(DataAndFile.Hash(ThisCar.VehicleID))
            pickle.dump(ThisCar,CarFile)
        CarFile.close()
        print('input over')
        target=input('find a record with the vehicle ID:')
        DataAndFile.Access(target)

if __name__=='__main__':
    main(2)
