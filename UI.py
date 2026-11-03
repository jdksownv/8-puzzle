class PuzzleUI:
    def __init__(self, size):
        self.size = size

    def DisplayBoard(self, board, move_count=None):
        print("\n" + "=" * (self.size * 6 + 1))
        
        if move_count is not None:
            print(f" [ 이동 횟수: {move_count} ]")
            print("-" * (self.size * 6 + 1))

        for row in board:
            line = "|"
            for num in row:
                if num == 0:
                    line += "     |"
                else:
                    line += f"  {num:2d} |"
            print(line)
            print("-" * (self.size * 6 + 1))

    def Exit(self):
        print("\n게임을 종료합니다. 프로그램을 마칩니다.")

    def GiveUp(self):
        print("\n퍼즐 풀기를 포기했습니다. 게임을 중단합니다.")

    def SizeError(self):
        print(">> [오류] 난이도는 3 이상의 숫자 또는 '종료'를 입력해 주세요.")

    def InputError(self):
        print(">> [오류] 이동할 타일의 숫자 또는 '포기'를 입력해 주세요.")
        
    def RestartError(self):
        print(">> [오류] '재시작' 또는 '종료'를 입력해 주세요.")

    def MoveError(self):
        print(">> [알림] 빈칸과 상·하·좌·우로 인접한 숫자만 이동할 수 있습니다.")

    def Victory(self, move_count):
        print(f"\n총 {move_count}번 이동하여 퍼즐을 완성했습니다.")
