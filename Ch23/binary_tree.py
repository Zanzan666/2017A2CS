#Jenny Zhan Opt3
np=-1

class BTNode:
    def __init__(self):
        self.value=''
        self.lp=np
        self.rp=np

class BT:
    def __init__(self,length):
        self.fp=0
        self.records=[]
        self.rootp=np
        for i in range(length):
            newNode=BTNode()
            newNode.lp=i+1
            self.records.append(newNode)
        self.records[-1].lp=np

    def insert(self,Item):
        if self.fp != np:
            self.newnp=self.fp
            self.fp=self.records[self.fp].lp
            self.records[self.newnp].value=Item
            self.records[self.newnp].lp=np
            self.records[self.newnp].rp=np
            if self.rootp==np:
                self.rootp=self.newnp
            else:
                tempP=self.rootp
                while tempP != np:
                    prevP=tempP
                    if self.records[tempP].value>Item:
                        self.TurnLeft=True
                        tempP=self.records[tempP].lp
                    elif self.records[tempP].value==Item:
                        print("error")
                        return None
                    else:
                        self.TurnLeft=False
                        tempP=self.records[tempP].rp
                if self.TurnLeft:
                    self.records[prevP].lp=self.newnp
                else:
                    self.records[prevP].rp=self.newnp
                    
    def find(self,Item):
        tempP=self.rootp
        while tempP !=np and self.records[tempP].value != Item:
            if self.records[tempP].value > Item:
                tempP=self.records[tempP].lp
            else:
                tempP=self.records[tempP].rp
        return tempP

a=BT(10)
a.insert(1)
a.insert(3)
a.insert(5)
a.insert(2)
a.insert(6)
a.insert(4)
print(a.find(3))
            
               
