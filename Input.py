class PuzzleInput:
    def GetSize(self):
        user_A = input("퍼즐 크기(난이도)를 입력하세요 (예: 3, 4, 5 / 종료: '종료'): ").strip()
        
        if user_A == "종료":
            return "EXIT"
        
        try:
            return int(user_A)
        except ValueError:
            return None

    def GetMove(self):
        user_A = input("\n이동할 숫자 입력 (포기: '포기'): ").strip()
        
        if user_A == "포기":
            return "GIVE_UP"
        
        try:
            return int(user_A)
        except ValueError:
            return None

    def GetRestart(self):
        user_A = input("\n다시 플레이하시겠습니까? (재시작 / 종료): ").strip()
        if user_A == "재시작":
            return "RESTART"
        elif user_A == "종료":
            return "EXIT"
        else:
            return None