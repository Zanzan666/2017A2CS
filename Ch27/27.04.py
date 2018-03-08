#Jenny Zhan
import datetime
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
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self):
        self.__IsRequested = True
    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested)
        
class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

C=[]
C.append(CD('And Justice For All','Metallica',123))
C.append(CD('Dark Side Of The Moon','Pink Floyd',234))
C.append(CD('Black Sabbath','Black Sabbath',345))
C.append(CD('hahahha','haha',456))
C.append(CD('hihihi','hihi',567))
B=[]
B.append(Book('12 Rules for Life','Jordan Peterson',678))
B.append(Book('White Fang','Jack London',789))
B.append(Book('I am a book','me',890))
B.append(Book('hi','hahh',111))
for i in C:
    i.PrintDetails()
for i in B:
    i.PrintDetails()
