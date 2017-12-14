#Jenny Zhan Option3
def factorial(x):
    if x==1:
        return 1
    return factorial(x-1)*x

def bunnyEars(bunnies):
    if bunnies==0:
        return 0
    return 2+bunnyEars(bunnies-1)

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

#print([fibonacci(i) for i in range(9)])

def bunnyEars2(bunnies):
    if bunnies==0:
        return 0
    if bunnies % 2 == 1:
        return 2+bunnyEars2(bunnies-1)
    return 3+bunnyEars2(bunnies-1)


#print([bunnyEars2(i) for i in range(9)])

def triangle(rows):
    if rows==0:
        return 0
    return rows+triangle(rows-1)

#print([triangle(i) for i in range(9)])

def sumDigits(n):
    if n//10==0:
        return n
    return n % 10 + sumDigits(n//10)

"""
print(sumDigits(126))
print(sumDigits(49))
print(sumDigits(12))
"""

def count7(n):
    if n//10==0:
        if n==7:
            return 1
        return 0
    if n % 10==7:
        return 1+count7(n//10)
    return count7(n//10)
"""
print(count7(717))
print(count7(7))
print(count7(123))
print(count7(7777777))
"""



def count8(n):
    if n/10<=0:
        return 0
    if n % 10 == 8 and (n % 100)//10==8:
        return 2+count8(n//10)
    if n % 10 ==8:
        return 1+count8(n//10)
    return count8(n//10)
    
"""
print(count8(8))
print(count8(818))
print(count8(8818))
print(count8(88888))
"""

def powerN(base,n):
    if n==1:
        return base
    return base*powerN(base,n-1)
"""
print(powerN(3,1))
print(powerN(3,2))
print(powerN(4,2))
print(powerN(9,3))
"""

def countX(str):
    if len(str)==0:
        return 0
    if str[0]=='x':
        return 1+countX(str[1:])
    return countX(str[1:])

"""
print(countX('xxxx'))
print(countX('hi'))
print(countX('xiii'))
"""
def countHi(str):
    if len(str)<=1:
        return 0
    if str[0]+str[1]=='hi':
        return 1+countHi(str[2:])
    return countHi(str[1:])
"""
print(countHi("xxhixx"))
print(countHi("xhixhix"))
print(countHi("hi"))
print(countHi("hihihihihi"))
"""


def changeXY(str):
    if len(str)==0:
        return str
    if str[0]=='x':
        return changeXY('y'+str[1:])
    return str[0]+changeXY(str[1:])

"""
print(changeXY('codex'))
print(changeXY('xxhixx'))
print(changeXY('xhixhix'))
"""

def changePi(str):
    if len(str)<=1:
        return str
    if str[0]+str[1]=='pi':
        return '3.14'+changePi(str[2:])
    return str[0]+changePi(str[1:])

"""
print(changePi('xpix'))
print(changePi('pipi'))
print(changePi('pip'))
"""

def noX(str):
    if len(str)==0:
        return str
    if str[0]=='x':
        return ''+noX(str[1:])
    return str[0]+noX(str[1:])
"""
print(noX("xaxb"))
print(noX("abc"))
print(noX("xx"))
"""

def array6(nums,index):
    if len(nums)==0:
        return False
    if nums[index]==6:
        return True
    return array6(nums[(index+1):],0)

"""
print(array6([1, 6, 4], 0))
print(array6([1, 4], 0))
print(array6([6], 0))
print(array6([1,2,3,6,2,3],5))
"""

def array11(nums,index):
    if len(nums)==0:
        return 0
    if nums[index]==11:
        return 1+array11(nums[index+1:],0)
    return array11(nums[index+1:],0)

"""
print(array11([1, 2, 11], 0))
print(array11([11, 11], 0))
print(array11([1, 2, 3, 4], 0))
"""

def array220(nums,index):
    if len(nums)<=1:
        return False
    if nums[1]/nums[0]==10:
        return True
    return array220(nums[index+1:],0)
"""
print(array220([1, 2, 20], 0))
print(array220([3, 30], 0))
print(array220([3], 0))
"""

def allStar(str):
    if len(str)==1:
        return str
    return str[0]+'*'+allStar(str[1:])

"""
print(allStar("hello"))
print(allStar("abc"))
print(allStar("ab"))
"""

def pairStar(str):
    if len(str)<=1:
        return str
    if str[0]==str[1]:
        return str[0]+'*'+pairStar(str[1:])
    return str[0]+pairStar(str[1:])

"""
print(pairStar("hello"))
print(pairStar("xxyy"))
print(pairStar("aaaa"))
"""
def endX(str):
    if len(str)==0:
        return str
    if str[0]=='x':
        return endX(str[1:])+'x'
    return str[0]+endX(str[1:])
"""
print(endX("xxre"))
print(endX('xxhixx'))
print(endX('xhixhix'))
"""
def countPairs(str):
    if len(str)<=2:
        return 0
    if str[0]==str[2]:
        return 1+countPairs(str[1:])
    return countPairs(str[1:])
"""
print(countPairs('axa'))
print(countPairs('axax'))
print(countPairs('axbx'))
print(countPairs('axaxa'))
"""
def countAbc(str):
    if len(str)<=2:
        return 0
    if str[:3]=='abc' or str[:3]=='aba':
        return 1+countAbc(str[1:])
    return countAbc(str[1:])

"""
print(countAbc('abc'))
print(countAbc('abcxxabc'))
print(countAbc('ababc'))
"""

def count11(str):
    if len(str)<=1:
        return 0
    if str[:2]=='11':
        return 1+count11(str[2:])
    return count11(str[1:])
#print(count11('abc1111x11x11'))

def stringClean(str):
    if len(str)<=1:
        return str
    if str[0]==str[1]:
        return stringClean(str[1:])
    return str[0]+stringClean(str[1:])

#print(stringClean('xxabcyy'))

def countHi2(str):
    if len(str)<=1:
        return 0
    if str[:3]=='xhi':
        return countHi2(str[3:])
    if str[:2]=='hi':
        return 1+countHi2(str[2:])
    return countHi2(str[1:])
#print(countHi2('xhibhi'))

def parenBit(str):
    if str[0]!='(':
        return parenBit(str[1:])
    if str[-1]!=')':
        return parenBit(str[:-1])
    return str
#print(parenBit("xyz(abc)123"))

def nestParen(str):
    if len(str)<3:
        if str=='()' or str=='':
            return True
        return False
    if str[0]=='(' and str(-1)==')':
        return nestParen(str[1:-1])
    return False

#print(nestParen("(((x))"))

def strCount(str,sub):
    if len(str)<len(sub):
        return 0
    if str[:len(sub)]==sub:
        return 1+strCount(str[len(sub):],sub)
    return strCount(str[1:],sub)

#print(strCount("cccc", "cc"))

def strCopies(str,sub,n):
    if len(str)<len(sub):
        if n==0:
            return True
        else:
            return False
    if str[:len(sub)]==sub:
        return strCopies(str[len(sub):],sub,n-1)
    return strCopies(str[1:],sub,n)

#print(strCopies("catcowcat", "cat", 2))

def strDist(str,sub):
    if str[:len(sub)]!=sub:
        return strDist(str[1:],sub)
    if str[-len(sub):]!=sub:
        return strDist(str[:-1],sub)
    return len(str)
#print(strDist("hiHellohihihi", "ll"))
