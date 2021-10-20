import random


scores = random.sample(range(50, 100), 20)
print(f'scores : {scores}')

ranks = [0 for i in range(len(scores))]
# print(f'ranks : {ranks}')

for idx, sco1 in enumerate(scores):

    ranks[idx] = 1

    for sco2 in scores:
        if sco1 < sco2:
            ranks[idx] += 1

print(f'ranks : {ranks}')

for i, s in enumerate(scores):
    print(f'{s}, rank : {ranks[i]}')