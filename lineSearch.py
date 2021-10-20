# 선형 검색

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
# print(datas)
# print(len(datas))

inputNum = int(input('input integer : '))
# 01 방법
# num = 0
#
# for idx, i in enumerate(datas):
#
#     if inputNum == i:
#         print(f'idx : {idx} \t num : {i}')
#
#     if idx == len(datas) -1:
#         print('nothing')


# 02 방법

# def lineSearch(inputNum):
#
#     n = 0
#
#     while True:
#
#         if n == len(datas):
#             searchResultIdx = -1
#             break
#
#         elif datas[n] == inputNum:
#             searchResultIdx = n
#             break
#
#         n += 1
#
#     if searchResultIdx < 0:
#         return 'nothing'
#     else:
#         return searchResultIdx

import lineSearchModule as lsm

lsmObj = lsm.SearchData(datas, inputNum)
result = lsmObj.getIndexOfData()

if result < 0:
    print('nothing')
else:
    print(f'index of data : {result}')