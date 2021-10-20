# 리스트에서 아스키코드가 가장 큰 값을 찾는 알고리즘을 만들기
# ord() 이용

class MaxAlgorithm:

    def __init__(self, cs):
        self.chars = cs
        self.maxChar = ''


    def getMaxChar(self):
        self.maxChar = self.chars[0]


        for c in self.chars:
            if ord(self.maxChar) < ord(c):
                self.maxChar = c

        return self.maxChar


if __name__ == '__main__':

    chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']


