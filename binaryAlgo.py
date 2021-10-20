# 이진검색

# datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11]
#
# print(datas)
# print(len(datas))
#
#
# searchNum = int(input('찾고싶은 숫자 입력 :'))
# searchIndex = -1
#
# staIdx = 0
# endIdx = len(datas) -1
# midIdx = (staIdx + endIdx) // 2
# midValue = datas[midIdx]
#
# print(f'midIdx : {midIdx}')
# print(f'midValue : {midValue}')
#
# while searchNum <= datas[len(datas) -1] and searchNum >= datas[0]:
#
#     if searchNum == datas[len(datas) -1]:
#         searchIndex = len(datas) -1
#         break
#
#     if searchNum > midValue:
#         staIdx = midIdx
#         midIdx = (staIdx + endIdx) // 2
#         midValue = datas[midIdx]
#         print(f'midIdx : {midIdx}')
#         print(f'midValue : {midValue}')
#
#     elif searchNum < midValue:
#         endIdx = midIdx
#         midIdx = (staIdx + endIdx) // 2
#         midValue = datas[midIdx]
#         print(f'midIdx : {midIdx}')
#         print(f'midValue : {midValue}')
#
#
#     elif searchNum == midValue:
#         searchIndex = midIdx
#         break
#
# print(f'searchIndex : {searchIndex}')

# 리스트를 오름차순으로 정렬한 후 7을 검색하고 위치(인덱스)찾기

dataList = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]

dataList.sort()
print(dataList)

searchNum = int(input('숫자 7 입력 :'))
searchIndex = -1

staIdx = 0
endIdx = len(dataList) -1
midIdx = (staIdx + endIdx) // 2
midValue = dataList[midIdx]



while searchNum <= dataList[len(dataList) - 1] and searchNum >= dataList[0]:

    if searchNum == dataList[len(dataList) -1]:
        searchIndex = len(dataList) -1
        break

    if searchNum > midValue:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midValue = dataList[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midValue : {midValue}')

    elif searchNum < midValue:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midValue = dataList[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midValue : {midValue}')


    elif searchNum == midValue:
        searchIndex = midIdx
        break

print(f'searchIndex : {searchIndex}')