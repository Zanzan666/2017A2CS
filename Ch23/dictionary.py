#Jenny Zhan Opt3

class Dictionary():
    def __init__(self,length=50):
        self.length=length
        self.Key=[[] for i in range(50)]
        self.Value=[[] for i in range(50)]
    def Hash(self,Key):
        Address=0
        for i in range (len(Key)):
            Address+=ord(str(Key)[i])
        Address=Address % self.length
        return Address
    def insert(self,Key,Value):
        index=self.Hash(Key)
        while self.Key[index] !=[]:
            index+=1
            if index > self.length:
                index=1
            print("Checking index",index)
        self.Key[index]=Key
        self.Value[index]=Value
    def Find(self,SearchKey):
        index=self.Hash(SearchKey)
        print("Checking index",index)
        while (self.Key[index]!=SearchKey) and (self.Key[index]!=[]):
            index+=1
            if index > self.length:
                index=0
                print("Checking index",index)
        if self.Key[index]:
            return self.Value[index]

