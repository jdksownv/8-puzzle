class PuzzleInput:
    def GetSize(self):
        raw = input("퍼즐 크기(난이도)를 입력하세요 (예: 3, 4, 5 / 종료: '종료'): ").strip()
        
        if raw == "종료":
            return "EXIT"
        
        try:
            return int(raw)
        except ValueError:
            return None

    def GetMove(self):
        raw = input("\n이동할 숫자 입력 (포기: '포기'): ").strip()
        
        if raw == "포기":
            return "GIVE_UP"
        
        try:
            return int(raw)
        except ValueError:
            return None

    def GetRestartChoice(self):
        raw = input("\n다시 플레이하시겠습니까? (재시작 / 종료): ").strip()
        if raw == "재시작":
            return "RESTART"
        elif raw == "종료":
            return "EXIT"
        else:
            return None