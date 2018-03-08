#Jenny Zhan
import datetime
class Borrower():
    def __init__(self,n,e,b):
        self.__BorrowerName=n
        self.__EmailAddress=e
        self.__BorrowerID=b
        self.__ItemsOnLoan=0

    def GetBorrowerName(self):
        return(self.__BorrowerName)

    def GetEmailAddress(self):
        return(self.__EmailAddress)

    def GetBorrowerID(self):
        return(self.__BorrowerID)

    def GetItemsOnLoan(self):
        return(self.__ItemsOnLoan)

    def UpdateItemsOnLoan(self,m):
        self.__ItemsOnLoan+=m

    def PrintDetails(self):
        print("Borrower's name:",self.__BorrowerName)
        print("Email address:",self.__EmailAddress)
        print("ID:",self.__BorrowerID)
        print("Items on loan:",self.__ItemsOnLoan)

class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
    def GetTitle(self):
        return(self.__Title)
    def GetAuthor_Artist(self):
        return(self.__Author_Artist)
    def GetItemID(self):
        return(self.__ItemID)
    def GetOnLoan(self):
        return(self.__OnLoan)
    def GetDueDate(self):
        return(self.__DueDate)
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
    def Returning(self):
        self.__OnLoan = False
    def PrintDetails(self):
        print(self.__Title,':',self.__Author_Artist,';',end='')
        print(self.__ItemID,';',self.__OnLoan,';',self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy=0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self,b):
        self.__IsRequested = True
        self.__RequestedBy=b
        
class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g

def menu():
    print('1. Add a new borrower')
    print('2. Add a new book')
    print('3. Add a new CD')
    print('4. Borrow a book')
    print('5. Borrow a CD')
    print('6. Exit program')
    ID=0
    Borrowers=[]
    CDs=[]
    Books=[]
    while True:
        choice=input('Enter your menu choice:')
        if choice=='1':
            name=input('name:')
            email=input('email:')
            ID+=1
            Borrowers.append(Borrower(name,email,ID))
        if choice=='2':
            title=input('title:')
            author=input('author:')
            ID+=1
            Books.append(Book(title,author,ID))
        if choice=='3':
            title=input('title:')
            artist=input('artist:')
            ID+=1
            CDs.append(CD(title,artsit,ID))
        if choice=='4':
            borrowerID=input('borrowerID:')
            bookID=input('bookID:')
            Book.Borrowing(bookID,borrowerID)
        if choice=='5':
            borrowerID=input('borrowerID:')
            cdID=input('cdID:')
            CD.Borrowing(cdID,borrowerID)
        if choice=='6':
            exit()
menu() 
