



**Task 2.1**



Toy:

upper:

​	Name: STRING

​	ID: STRING

​	Price: CURRENCY

​	MinimumAge: INTEGER

lower:

​	Constructor()

​	SetNamae()

​	SetID()

​	SetPrice()

​	SetMinimumAge()

​	GetName()

​	GetPrice()

​	GetID()

​	GetMinimumAge()



ComputerGame:

upper:

​	Category: STRING

​	Console: STRING

lower:

​	Constructor()

​	SetCategory()

​	SetConsole()

​	GetCategory()

​	GetConsole()



Vehicle:

upper:

​	Type: STRING

​	Height: REAL

​	Length: REAL

​	Weight: REAL

lower:

​	Constructor()

​	SetType()

​	SetHeight()

​	SetLength()

​	SetWeight()

​	GetType()

​	GetHeight()

​	GetLength()

​	GetWeight()

**Task 2.2**

Inheritance is when in object-oriented programming a class or object is based on another class or object. 



```
				Toy

				  ↑

   		|		   		     |

ComputerGame			Vehicle
```

​	

**Task 2.3**

```python
class Toy(object):
	def __init__(self):
		self.__Name=''
		self.__ID=''
		self.__Price=0.00
		self.__MinimumAge=0
	def SetName(self, n):
		self.__Name=n
	def SetID(self,i):
		self.__ID=i
	def SetPrice(self, p):
		self.__Price=p
	def SetMinimumAge(self, a):
		self.__MinimumAge=a
	def GetName(self):
		return self.__Name
	def GetID(self):
		return self.__ID 
	def GetPrice(self):
		return self.__Price 
	def GetAge(self):
		return self.__MinimumAge

```



**Task 2.4**

```python
class ComputerGame(Toy):
	def __init__(self):
		self.__Category=''
		self.__Console=''
	def SetCategory(self, new):
		self.__Category=new
	def SetConsole(self, new):
		self.__Console=new
	def GetCategory(self):
		return self.__Category
	def GetConsole(self):
		return self.__Console

class Vehicle(Toy):
	def __init__(self):
		self.__Type=''
		self.__Height=0
		self.__Length=0
		self.__Weight=0
	def SetType(self, t):
		self.__Type=t
	def SetHeight(self, h):
		self.__Height=h
	def SetLength(self, l):
		self.__Length=l
	def SetWeight(self, w):
		self.__Weight=w
	def GetType(self):
		return self.__Type
	def GetHeight(self):
		return self.__Height
	def GetLength(self):
		return self.__Length
	def GetWeight(self):
		return self.__Weight
```



**Task 2.5**

```python
class Toy:
    def SetMinimumAge(self, a):
    	if a>18 or a<0:
        	print('not valid')
		else:
			self.__MinimumAge=a
```



**Task 2.6**

```python
toys = []
newToy = Vehicle()
newToy.SetName('Red Sports Car')
newToy.SetID('RSC13')
newToy.SetMinimumAge(6)
newToy.SetType('Car')
newToy.SetHeight(3.3)
newToy.SetLength(12.1)
newToy.SetWeight(0.08)
toys.append(newToy)
newToy=ComputerGame()
newToy.SetName('Gardenscapes')
newToy.SetID('aaaa')
newToy.SetMinimumAge(4)
newToy.SetPrice(0)
newToy.SetCategory('puzzle')
newToy.setConsole('PC')
toys.append(newToy)
```



**Task2.7**

```python
class Toy:
	def PrintDetais(self):
		print(" Name:",self.__name)
		print(" ID:",self.__ID)
		print(" Price:",self.__Price)
		print(" Minimum age:",self.__MinimumAge)

class ComputerGame(self):
	def PrintDetais(self):
		print(" Name:",self.__name)
		print(" ID:",self.__ID)
		print(" Price:",self.__Price)
		print(" Minimum age:",self.__MinimumAge)
		print(" Category:",self.__Category)
		print(" Console:",self.__Console)

class Vehicle(self):
	def PrintDetais(self):
		print(" Name:",self.__name)
		print(" ID:",self.__ID)
		print(" Price:",self.__Price)
		print(" Minimum age:",self.__MinimumAge)
		print(" Type:",self.__Type)
		print(" Height:",self.__Height)
		print(" Length:",self.__Length)
		print(" Weight:",self.__Weight)

def FindToy(ID):
    Found=False
	for i in toys:
		if i.GetID == ID:
			i.PrintInfo()
			Found=True
			break
	if not Found:
		print('not found')
```



**Task 2.8**

```python
def Discount():
	rate=int(input('Enter discount rate:'))
	for i in range(len(toys)):
		p1=toys[i].GetPrice()
		p2=toys[i].SetPrice(p1*(1-rate/100))
toys = []
newToy = Vehicle()
newToy.SetName('Red Sports Car')
newToy.SetID('RSC13')
newToy.SetMinimumAge(6)
newToy.SetType('Car')
newToy.SetHeight(3.3)
newToy.SetLength(12.1)
newToy.SetWeight(0.08)
toys.append(newToy)
newToy=ComputerGame()
newToy.SetName('Gardenscapes')
newToy.SetID('aaaa')
newToy.SetMinimumAge(4)
newToy.SetPrice(0)
newToy.SetCategory('puzzle')
newToy.setConsole('PC')
toys.append(newToy)
Discount(10)
for t in toys():
	t.PrintDetails()
```



**Task 2.9**

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.



**Task 2.10**

```python
def bubbleSort(games): 
	for i in range(len(games)):
		for j in range(i, len(games)):
			if games[i].getPrice() > games[j].getPrice():
				temp = games[i]
				games[i] = games[j]
				games[j] = temp
	for g in games():
		g.PrintDetails()
```

