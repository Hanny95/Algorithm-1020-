# 최솟값 알고리즘

nums = [-1, -4, 5, 7, 10, 0, 8, 20, -11]

def getMinNum(nums):

    minNum = 0

    for n in nums:
        if minNum > n:
            minNum = n

    return minNum

minNum = getMinNum(nums)
print(minNum)