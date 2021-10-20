# 선택 정렬 : 앞에있는 수를 기준으로 뒤에 있는 수 중 최솟값과 자리 바꿈

nums = [4,2,5,1,3]
print(f'not sorted nums : {nums}')

for i in range(len(nums) -1):
    minIdx = i

    for j in range(i+1, len(nums)):
       if nums[minIdx] > nums[j]:
           minIdx =  j

    nums[i], nums[minIdx] = nums[minIdx], nums[i]

print(f'nums : {nums}')

