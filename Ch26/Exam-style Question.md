# Exam-style Question

Jenny Zhan

1.

a.

i.

```python
class CustomerRecord:
  def __init__(self):
    self.customerID=0
    self.name=''
    self.tel=''
    self.value=0
```

ii.

```python
CustomerData=[CustomerRecord() for i in range(1000)]
```

b.

i.

```python
def Hash(CustomerID):
  Address=CustomerID % 1000
  return Address
```

ii.

```python
def AddRecord(Customer):
  Address=Hash(Customer.customerID)
  while CustomerData[Address].customerID != 0:
    Address+=1
  	if Address==1000:
      Address=0
  CustomerData[Address]=Customer
```

iii.

```python
def FindRecord(CustomerID):
  Address=Hash(CustomerID)
  while CustomerData[Address].customerID!=CustomerID:
    Address+=1
   	if Address==1000:
      Address=0
  return Address
```

c.

```python
import pickle
CustomerFile=open('CustomerData.DAT','wb')
for i in range(1000):
  pickle.dump(CustomerData.[i],CustomerFile)
CustomerFile.close()
```

d.

Changing the record to fixed-length records. We can use a hashing function to calculate an address from the record key and store the record at the calculated address in the file. Save and Load each individual record.

2.

```python
FileName=input('which file do you want to use?')
try:
  fileHandle=open(FileName,'rb+')
except:
  print('wrong file name')
```

