#Jenny Zhan opt3


def groupSum(start,nums,target):
    if start==len(nums) and target!=0:
        return False
    if target==0:
        return True
    return groupSum(start+1,nums,target-nums[start]) or groupSum(start+1,nums,target)

"""
print(groupSum(0, [2, 4, 8], 10))
print(groupSum(0, [2, 4, 8], 14))
print(groupSum(0, [2, 4, 8], 9))
"""

def groupSum6(start,nums,target):
    if start==len(nums) and target!=0:
        return False
    if target==0:
        return True
    if nums[start]==6:
        return groupSum6(start+1,nums,target-nums[start])
    return groupSum6(start+1,nums,target-nums[start]) or groupSum6(start+1,nums,target)

"""
print(groupSum6(0, [5, 6, 2], 8))
print(groupSum6(0, [5, 6, 2], 9))
print(groupSum6(0, [5, 6, 2], 7))
"""

def groupNoAdj(start,nums,target):
    if start>=len(nums) and target!=0:
        return False
    if target==0:
        return True
    return groupNoAdj(start+2,nums,target-nums[start]) or groupNoAdj(start+1,nums,target)

"""
print(groupNoAdj(0, [10, 2, 2, 3, 3], 7))
print(groupNoAdj(0, [10, 2, 2, 3, 3], 15) )
print(groupNoAdj(0, [2, 5, 10, 4], 9))
"""

def groupSum5(start,nums,target):
    if start==len(nums) and target!=0:
        return False
    if target==0:
        return True
    if nums[start]%5==0 and nums[start+1]==1:
        return groupSum5(start+2,nums,target-nums[start])
    if nums[start]%5==0:
        return groupSum5(start+1,nums,target-nums[start])
    return groupSum5(start+1,nums,target-nums[start]) or groupSum5(start+1,nums,target)

"""
print(groupSum5(0, [3, 5, 1], 5))
print(groupSum5(0, [3, 5, 1], 9))
print(groupSum5(0, [2, 5, 10, 4], 12))
"""

def groupSumClump(start,nums,target):
    if start>=len(nums) and target!=0:
        return False
    if target==0:
        return True
    i=1
    if start<len(nums)-1:
        while nums[start]==nums[start+i] and (start+i)<len(nums)-1:
            i+=1
    return groupSumClump(start+i,nums,target-nums[start]*i) or groupSumClump(start+i,nums,target)

#print(groupSumClump(0, [2, 4, 8], 10),groupSumClump(0, [1, 2, 4, 8, 1], 14),groupSumClump(0, [1,1,1,1,1], 3),
#      groupSumClump(0, [8, 2, 2, 1], 11),groupSumClump(0, [9], 1),groupSumClump(0, [1], 1))


def splitArray(nums,x=0,y=0,start=0):
    if start>=len(nums) and x!=y:
        return False
    if start==len(nums) and x==y:
        return True
    return splitArray(nums,x+nums[start],y,start+1) or splitArray(nums,x,y+nums[start],start+1)

#print(splitArray([2, 2]),splitArray([2, 3]),splitArray([5, 2, 3]))
    
def splitOdd10(nums,x=0,y=0,start=0):
    if start>=len(nums):
        if x%10==0 and y%2==1:
            return True
        if x%2==1 and y%10==0:
            return True
        return False
    return splitOdd10(nums,x+nums[start],y,start+1) or splitOdd10(nums,x,y+nums[start],start+1)

#print(splitOdd10([5, 5, 5]),splitOdd10([5, 5, 6]),splitOdd10([5, 5, 6, 1]))

def split53(nums,x=0,y=0,start=0):
    if start==len(nums) and x!=y:
        return False
    if start==len(nums) and x==y:
        return True
    if nums[start]%5==0:
        return split53(nums,x+nums[start],y,start+1)
    if nums[start]%3==0:
        return split53(nums,x,y+nums[start],start+1)
    return split53(nums,x+nums[start],y,start+1) or split53(nums,x,y+nums[start],start+1)

