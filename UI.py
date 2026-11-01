
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

    # UI.py 에 추가/수정
    def ShowExit(self):
        print("\n게임을 종료합니다. 프로그램을 마칩니다.")

    def ShowGiveUp(self):
        print("\n퍼즐 풀기를 포기했습니다. 게임을 중단합니다.")

    def ShowSizeError(self):
        print(">> [오류] 난이도는 3 이상의 숫자 또는 '종료'를 입력해 주세요.")

    def ShowInputError(self):
        print(">> [오류] 이동할 타일의 숫자 또는 '포기'를 입력해 주세요.")
        
    def ShowRestartError(self):
        print(">> [오류] '재시작' 또는 '종료'를 입력해 주세요.")