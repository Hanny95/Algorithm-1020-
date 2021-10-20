# 최댓값 알고리즘

# nums = [-1, -4, 5, 7, 10, 0, 8, 20, -11]
#
# def getMaxNum(ns):
#     maxNum = -1000
#
#     for n in ns:
#         if maxNum < n:
#             maxNum = n
#
#     return maxNum
#
# maxNum = getMaxNum(nums)
# print(maxNum)

# 01 : max() 이용
# maxNum = max(nums)
# print(maxNum)

# sort() 이용
# nums.sort()
# print(nums)
# print(nums[len(nums) -1])

# 함수
# def getMaxNum(ns):
#     ns.sort()
#     return ns[len(ns) -1]
#
# maxNum = getMaxNum(nums)
# print(maxNum)

# 리스트에서 아스키코드가 가장 큰 값을 찾는 알고리즘을 만들기
# ord() 이용
chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']


def getCodeMaxNum():

    maxNum = 0

    for c in chars:
        if ord(maxNum) < ord(c):
            maxNum = c

    return maxNum

# 다른 파일 클래스
# import maxNumForCharCode
# ma = maxNumForCharCode.MaxAlgorithm(chars)
# maxChar = ma.getMaxChar()
# print(maxChar)