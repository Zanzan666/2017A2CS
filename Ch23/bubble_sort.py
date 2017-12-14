#Jenny Zhan Option3
def bubblesort(bubbleList):
    n=len(bubbleList)
    NoMoreSwaps=False
    while not NoMoreSwaps:
        NoMoreSwaps=True
        for i in range(n-1):
            if bubbleList[i]>bubbleList[i+1]:
                NoMoreSwaps=False
                bubbleList[i],bubbleList[i+1]=bubbleList[i+1],bubbleList[i]
        n-=1
        print(bubbleList,NoMoreSwaps)
    return bubbleList

print(bubblesort([1,6,3,20,99,33,12,4,0]))
