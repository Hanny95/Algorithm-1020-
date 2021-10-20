import random

# 학급 학생 20명의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고,
# 중간고사 대비 기말고사 순위 변화 (편차)를 출력하는 프로그램 만들기
# 1 : mid_score : 85 final_score : 90 deviation : ↑5
# score : 50 ~ 100


# mid_score = random.sample(range(50, 100), 20)
# final_score = random.sample(range(50, 100), 20)
#
# print(mid_score)
# print(final_score)
#
# midRanks = [0 for i in range(len(mid_score))]
# finalRanks = [0 for i in range(len(final_score))]
#
# for idx, mid1 in enumerate(mid_score):
#
#     midRanks[idx] = 1
#     for mid2 in mid_score:
#         if mid1 < mid2:
#             midRanks[idx] +=1
#
# for idx, final1 in enumerate(final_score):
#
#     finalRanks[idx] = 1
#     for final2 in final_score:
#         if final1 < final2:
#             finalRanks[idx] += 1
#
# for i, m in enumerate(mid_score):
#     for i, f in enumerate(final_score):
#         print(f'{i + 1}번째 학생')
#         print(f'midScore : {m}, midRanking : {midRanks[i]}')
#         print(f'finalScore : {f}, midRanking : {finalRanks[i]}')



import rankModule as rm

midStdScores = random.sample(range(50, 100), 20)
finalStdScores = random.sample(range(50, 100), 20)

rd = rm.RankDeviation(midStdScores, finalStdScores)

rd.setMidRank()
print(f'mid_rank : {rd.getMidRank()}')

rd.setEndRank()
print(f'final_rank : {rd.getEndRank()}')

rd.printRankDeviation()