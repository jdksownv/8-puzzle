#1 퍼즐의 크기를 Controller로 부터전달받아 저장하고 판의 홀짝 여부를 판단해둔다.
#2 퍼즐의 크기에 따른 2차원 배열을 생성, 1부터 순서대로 숫자를 채운 뒤 마지막 자리에 0(빈칸)삽입(목표상태가 생성됨)
#3 랜덤 셔플 - 목표상태인 2차원 배열을 받아 랜덤으로 섞어 현재상태 배열에 저장한다.(검증 필요)
#4 배열 변환 - 반전수 계산이나 다른 계산의 편의를 위한 2차원 -> 1차원, 1차원 -> 2차원 배열 전환 기능
#5 검증 - 랜덤 상태의 배열은 배열 변환을 거쳐 1차원 상태로 검증을 시작, 판의 홀짝 여부에 따라 반전수 계산을 달리하며, 통과시, 미통과시 T/F를 출력한다.
import random

class PuzzleMake:
    def __init__(self, size):
        self.size = size
        self.OoE = size%2

    def MakeGoal(self):
        Goalarr = [0] * self.size ** 2
        num = 1
        for i in range(self.size ** 2):
                Goalarr[i] = num
                num += 1
        Goalarr[-1] = 0
        return Goalarr

    def Random(self):
        Nowarr = self.MakeGoal()
        random.shuffle(Nowarr)
        return Nowarr

    def Transformation(self):
        pass

    def Test(self, Nowarr):
        num = 0
        for i in range(len(Nowarr)):
            for j in range(i + 1, len(Nowarr)):
                if Nowarr[i] == 0 or Nowarr[j] == 0 :
                      pass
                elif Nowarr[i] > Nowarr[j] :
                      num += 1
                else :
                     pass
        if (num % 2) == 0:
            result = True
        else:
            result = False

        return result
                      
