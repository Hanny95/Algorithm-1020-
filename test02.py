# 학급에 20명이 있다. 학생키 정렬(오름차순)
# random, range(170 ~ 185)

import random
import bubbleAlgo as ba
stdHeights = []

for i in range(20):
    stdHeights.append(random.randint(170, 185))

print(stdHeights)
print(f'height : {ba.bubbleSort(stdHeights, deepCopy=False)}')
print(stdHeights)
# scores = random.sample(range(50, 100), 20)
# print(scores)

# li = []
# stdHeight = [random.choice(li)] for i in range(20)
# stdHeight = random.sample(range(170, 185), 20)