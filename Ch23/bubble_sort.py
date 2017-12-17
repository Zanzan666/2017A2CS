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
    return bubbleList
