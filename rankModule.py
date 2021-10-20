class RankDeviation:

    def __init__(self, mss, ess):
        self.midStdScores = mss
        self.finalStdScores = ess
        self.midRanks = [0 for i in range(len(mss))]
        self.endRanks = [0 for i in range(len(ess))]
        self.rankDeviation = [0 for i in range(len(mss))]

    # 순위 측정 함수
    def setRank(self, ss, rs):
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1


    # 중간고사 순위 설정
    def setMidRank(self):
        self.setRank(self.midStdScores, self.midRanks)

    # 중간고사 순위 반환
    def getMidRank(self):
        return self.midRanks

    # 기말고사 순위 설정
    def setEndRank(self):
        self.setRank(self.endStdScores, self.endRanks)

    # 기말고사 순위 반환
    def getEndRank(self):
        return self.endRanks

    # 편차 출력
    def printRankDeviation(self):

        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.fssRanks[idx]

            if deviation > 0:
                # 순위 다운
                deviation = '↑' + str(abs(deviation))


            elif deviation < 0:
                # 순위 업
                deviation = '↓' + str(abs(deviation))

            else:
                # 순위 변동 없음
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank : {mRank} \t end_rank : {self.fssRanks[idx]} \t deviation : {deviation}')