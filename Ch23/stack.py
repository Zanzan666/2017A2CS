#Jenny Zhan Option3
np=-1
class StackNode:
    def __init__(self):
        self.value=''
        self.nextP=np

class Stack:
    def __init__(self,length):
        self.tp=np
        self.fp=0
        self.records=[]
        for i in range(length):
            newNode=StackNode()
            newNode.nextP=i+1
            self.records.append(newNode)
        newNode.nextP=-1
    def push(self,Item):
        if self.fp!=np:
            self.newnp=self.fp
            self.records[self.newnp].value=Item
            self.fp=self.records[self.fp].nextP
            self.records[self.newnp].nextP=self.tp
            self.tp=self.newnp
        else:
            print("no space available")
    def pop(self):
        if self.tp==np:
            print('no data')
            return('')
        else:
            value=self.records[self.tp].value
            self.cNodeP=self.tp
            self.tp=self.records[self.tp].nextP
            self.records[self.cNodeP].nextP=self.fp
            self.fp=self.cNodeP
            return(value)

