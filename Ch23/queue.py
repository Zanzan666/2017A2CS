#Jenny Zhan Option3
np=-1
class QueueNode:
    def __init__(self):
        self.value=''
        self.nextP=np

class Queue:
    def __init__(self,length):
        self.sp=np
        self.fp=0
        self.ep=np
        self.records=[]
        for i in range(length):
            newNode=QueueNode()
            newNode.nextP=i+1
            self.records.append(newNode)
        self.records[-1].nextP=np

    def enqueue(self,Item):
        if self.fp!=np:
            self.newnp=self.fp
            self.records[self.newnp].value=Item
            self.fp=self.records[self.fp].nextP
            self.records[self.newnp].nextP=np
            if self.sp==np:
                self.sp=self.newnp
            else:
                self.records[self.ep].nextP=self.newnp
            self.ep=self.newnp
            
        else:
            print("no space available")
    def dequeue(self):
        if self.sp==np:
            print('no data')
            return('')
        else:
            temp=self.records[self.sp].nextP
            if temp==np:
                self.ep=np
            self.records[self.sp].nextP=self.fp
            self.fp=self.sp
            self.sp=temp
        return(self.records[self.fp].value)

a=Queue(10)
a.enqueue(1)
a.enqueue(2)
a.enqueue(4)
a.enqueue(3)
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
