#Jenny Zhan Opt3

class HashTables():
    def __init__(self,length):
        self.length=length
        self.HashTable=[[] for i in range(self.length)]
    def Hash(self,Key):
        Address=Key % self.length
        return Address
    def insert(self,Key):
        index=self.Hash(Key)
        while self.HashTable[index] !=[]:
            index+=1
            if index > self.length:
                index=1
            print("Checking index",index)
        self.HashTable[index]=Key
    def Find(self,SearchKey):
        index=self.Hash(SearchKey)
        print("Checking index",index)
        while (self.HashTable[index]!=SearchKey) and (self.HashTable[index]!=[]):
            index+=1
            if index > self.length:
                index=0
                print("Checking index",index)
        if self.HashTable[index]:
            return self.HashTable[index]

a=HashTables
a.insert(a,1)
