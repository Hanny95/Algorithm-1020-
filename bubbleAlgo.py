# 버블 정렬
import copy

# nums = [10, 2, 7, 21, 0]
#
# print(f'not sorted nums : {nums}')

# length = len(nums) -1
# print(length)
#
# for i in range(length):
#     for j in range(length-i):
#         if nums[j] > nums[j + 1]:
#             # temp = nums[j]
#             # nums[j] = nums[j+1]
#             # nums[j+1] = temp
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#
# print(f'sorted nums : {nums}')



# def bubbleSort(ns, deepCopy = True):
#     if deepCopy:
#         cns = copy.copy(ns)
#     else:
#         cns = ns
#
#     length = len(cns) - 1
#
#     for i in range(length):
#         for j in range(length - i):
#             if cns[j] > cns[j + 1]:
#                 cns[j], cns[j + 1] = cns[j + 1], cns[j]
#
#     return cns
#
# if __name__ == '__main__':
#     print(f'sorted nums : {bubbleSort(nums)}')
#     print(f'not sorted nums : {nums}')




# 삽입(insert)정렬

nums = [5, 10, 2, 1, 0]
print(f'not sorted nums : {nums}')

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] > cNum and i2 >= 0:
        nums[i2+1] = nums[i2]
        i2 -= 1

    nums[i2+1] = cNum

print(f'sorted nums: {nums}')

