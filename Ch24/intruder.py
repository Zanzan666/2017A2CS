#Jenny Zhan Option3

import time
from threading import Thread


sysIna='System is inactive'
sysa='System is active'
alarm='Alarm bell rings'
alert='Alert mode'

def check():
    time.sleep(120)
    if Action != None:
        return
    A.twoMinutesPass()


class IntruderDetection():
    def __init__(self):
        self.state=sysIna

    def pressButton(self):
        if self.state==sysIna:
            self.state=sysa

    def enterPIN(self):
        if self.state==alert:
            self.state=sysIna
        if self.state==sysa:
            self.state=sysIna
        if self.state==alarm:
            self.state=sysIna

    def SensorActivated(self):
        if self.state==sysa:
            self.state=alert

    def twoMinutesPass(self):
        self.state=alarm

if __name__=='__main__':
    A=IntruderDetection()
    while True:
        print(A.state)
        if A.state==alert:
            Thread(target=check).start()
            Action=input("1.Enter PIN, 2. Press button, 3. Sensor activated")
            Action=None

        else:
            Action=input("1.Enter PIN, 2. Press button, 3. Sensor activated")
            if Action=='1':
                A.enterPIN()
            elif Action=='2':
                A.pressButton()
            elif Action=='3':
                A.SensorActivated()
            else:
                print('error')
            Action=None
    
