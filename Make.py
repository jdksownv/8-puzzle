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
        while True:
            Nowarr = self.MakeGoal()
            random.shuffle(Nowarr)
            if self.Test(Nowarr):
                break
        return self.Transformation(Nowarr)

    def Transformation(self, arr):
        Nowarr = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(arr[i * self.size + j])
            Nowarr.append(row)
        return Nowarr


    def Test(self, Nowarr):
        num = 0
        for i in range(len(Nowarr)):
            for j in range(i + 1, len(Nowarr)):
                if Nowarr[i] == 0 or Nowarr[j] == 0:
                    pass
                elif Nowarr[i] > Nowarr[j]:
                    num += 1
                else :
                    pass
                
        if self.OoE == 1:
            if (num % 2) == 0:
                result = True
            else:
                result = False
        else:
            blank_row = self.size - (Nowarr.index(0) // self.size)
            if (blank_row + num) % 2 == 1:
                result = True
            else:
                result = False
                  
             
        return result
                      
