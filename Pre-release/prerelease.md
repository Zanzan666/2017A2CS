**Task 1.1**

JSP structure diagrams help to design a program, as it gives a structure of the data the intended program will handle.



**Task 1.2**

*: Repetition

°: Selection



**Task 1.3**

```pseudocode
WHILE EndOfFile = FALSE
	CALL ReadSalary()
	IF Salary > 50
		THEN
			IF Salary >= 90
				THEN
					Role ← ProjectManager
				ELSE
					Role ← LeadDeveloper
			ENDIF
		ELSE
			Role ← Manager
	ENDIF
ENDWHILE
```



**Task 1.4**

```
		

		Salary Classification

				|

			Identify Role *

				|

	|						|

Read Salary				Salary>50

							|

				|False				|True

		Assign Manager °			Salary>70

									|

							|False		|True

			Assign Lead Developer		Salary>=90

											|

								|False				|True

					Assign Consultant		Assign Project Manager



```



**Task 1.5**

```pseudocode
WHILE TRUE
	CALL ReadSalary()
	IF Salary > 50
		THEN
			IF Salary > 70
				THEN
					IF Salary >= 90
						THEN
							Role ← 'Project Manager'
						ELSE
							Role ← 'Consultant'
					ENDIF
				ELSE
					Role <- 'Lead Developer'
			ENDIF
		ELSE
			Role <- 'Manager'
	ENDIF
ENDWHILE
```





**Task 1.6**

```python
def deterRole(salary):
  role = ''
  if salary < 50:
    role = 'Manager'
  elif 50 < salary <= 70:
    role = 'Lead Developer'
  elif 70 < salary < 90:
    role = 'Consultant'
  else:
    role = 'Project Manager'
  return role
```







**Task 2.1**



Toy:

upper:

​	Name: STRING

​	ID: STRING

​	Price: CURRENCY

​	MinimumAge: INTEGER

lower:

​	Constructor(Name: STRING, ID: STRING, Price: CURRENCY, MinimumAge: INTEGER)

​	SetPrice(Price: CURRENCY)

​	GetName()

​	GetPrice()

​	GetID()

​	GetMinimumAge()



ComputerGame:

upper:

​	Category: STRING

​	Console: STRING

lower:

​	Constructor(Name: STRING, ID: STRING, Price: CURRENCY, MinimumAge: INTEGER, Category: STRING, Console: STRING)

​	GetCategory()

​	GetConsole()



Vehicle:

upper:

​	Type: STRING

​	Height: REAL

​	Length: REAL

​	Weight: REAL

lower:

​	Constructor(Name: STRING, ID: STRING, Price: CURRENCY, MinimumAge: INTEGER, Type: STRING, Height: REAL, Length: REAL, Weight: REAL)

​	GetType()

​	GetHeight()

​	GetLength()

​	GetWeight()

**Task 2.2**

```
				Toy

				  ↑

   		|		   		     |

ComputerGame			Vehicle
```

​	

**Task 2.3**

```python
class Toy:
    def __init__(self,n,i,p,a):
        self.__name=n
        self.__id=i
        self.__price=p
        self.__minimumAge=a
    def SetPrice(self,p):
        self.__price=p
    def GetName(self):
        print(self.__name)
    def GetPrice(self):
        print(self.__price)
    def GetID(self):
        print(self.__id)
    def GetMinimumAge(self):
        print(self.__minimumAge)
```



**Task 2.4**

```python
class ComputerGame(Toy):
    def __init__(self,category,console):
        self.__category=category
        self.__console=console
    def GetCategory(self):
        print(self.__category)
    def GetConsole(self):
        print(self.__console)
```



