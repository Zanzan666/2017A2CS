#Jenny Zhan Option3
np=-1

class ListNode:
    def __init__(self):
        self.value=''
        self.nextP=np

class List:
    def __init__(self,length):
        self.freeP=0
        self.sp=-1
        self.records=[]
        for i in range(length):
            newNode=ListNode()
            newNode.nextP=i+1
            self.records.append(newNode)
        self.records[-1].nextP=np
    
    def Access(self):
        self.cp=self.sp
        while self.cp != np:
            print(self.records[self.cp].value)
            self.cp=self.records[self.cp].nextP

    def Insert(self,newItem):
        if self.freeP != np:
            self.newNodeP=self.freeP
            self.records[self.newNodeP].value=newItem
            self.freeP=self.records[self.freeP].nextP
            self.prevNodeP=np
            self.cNodeP=self.sp
            while (self.cNodeP != np) and (self.records[self.cNodeP].value < newItem):
                self.prevNodeP=self.cNodeP
                self.cNodeP=self.records[self.cNodeP].nextP
            if self.prevNodeP == np:
                #self.records[self.newNodeP].nextP=self.sp
                self.records[self.newNodeP].nextP=np
                self.sp=self.newNodeP
            else:
                self.records[self.newNodeP].nextP=self.records[self.prevNodeP].nextP
                self.records[self.prevNodeP].nextP=self.newNodeP

    def Find(self,Item):
        self.cNodeP=self.sp
        while self.cNodeP != np and self.records[self.cNodeP].value != Item:
            self.cNodeP=self.records[self.cNodeP].nextP
        return self.cNodeP

    def Delete(self,Item):
        self.cNodeP=self.sp
        while self.cNodeP != np and self.records[self.cNodeP].value != Item:
            self.prevNodeP=self.cNodeP
            self.cNodeP=self.records[self.cNodeP].nextP
        if self.cNodeP != np:
            if self.cNodeP ==self.sp:
                self.sp=self.records[self.sp].nextP
            else:
                self.records[self.prevNodeP].nextP=self.records[self.cNodeP].nextP
            self.records[self.cNodeP].nextP=self.freeP
            self.freeP=self.cNodeP

a=List(5)
a.Insert(1)
a.Insert(3)

a.Insert(4)
a.Insert(2)
a.Delete(3)
a.Insert(6)
a.Insert(3)
a.Access()
