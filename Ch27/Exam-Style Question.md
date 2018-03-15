Jenny Zhan

#Chapter 27 Exam-style Questions

##1

###a

​			BankAccount

​				  ↑

   		|		   			|

PersonalAccount			SavingAccount



###b

```python
class BankAccount:
  def __init__(self,number):
    self.__IBAN=number
  def SetAccountHolderName(self,name):
    self.__AccountHolderName=name
  def GetAccountHolderName(self):
    print(self.__AccountHolderName)
  def GetIBAN(self):
    print(self.__IBAN)
```



###c

####i

Attributes: MonthlyFee, OverdraftLimit

Methods: Constructor, SetOverdraftLimit, GetMontlyFee, GetOverdraftLimit

####ii

Attributes: Balance, InterestRate

Methods: Constructor, SetInterestRate, GetBalance, GetInterestRate

####iii

encapsulation



##2

###a

EmailAddress: STRING

GetTicketHolderName()

GetEmailAddress()



Private

Amount: CURRENCY

Constructor(Name:STRING, email: STRING, Amount: CURRENCY)

GetAmount()

UpdateAmount()



Private

Fee: CURRENCY

GetFee()



###b

####i

so they can only be changed with methods in the class

####ii

can be used elsewhere to access the attributes



###c

```python
NewCustomer=ContractTicketHolder('A.Smith','xyz@abc.xx',10)
```





# 3

## a

Containment

## b

```python
class NodeClass:
  def __init__(self):
    self.__data=''
    self.__pointer=-1
  def SetData(self,d):
    self.__data=d
  def SetPointer(self,x):
    self.__pointer=x
  def GetData(self):
    print(self.__data)
  def GetPointer(self):
    print(self.__pointer)
    
```

## c

```python
class QueueClass():
  def __init__(self):
    self.__Queue=[NodeClass for i in range(51)]
    self.__Head=-1
    self.__Tail=-1
  
```



## d

```python
def JoinQueue(self,NewItem):
    if self.__Head==-1:
        self.__Head=0
    self.__Tail+=1
    i=self.__Tail
    self.__Queue[i].SetData(NewItem)
```

