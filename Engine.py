class PuzzleEngine:
    def __init__(self, size):
        self.size = size
        self.moves = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1)
        }

    def FindZero(self, board):
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == 0:
                    return (r, c)    

    def CanMove(self, pos, direction):
        r, c = pos
        dr, dc = self.moves[direction]
        
        next_r = r + dr
        next_c = c + dc
        
        if 0 <= next_r < self.size and 0 <= next_c < self.size:
            return True
        else:
            return False

    def CheckWin(self, current_board, goal_board):
        if current_board == goal_board:
            return True
        else:
            return False

    def FindNumber(self, board, target):
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == target:
                    return (r, c)
        return None

    def Move(self, board, target):
        target = self.FindNumber(board, target)
        if target is None:
            return False

        zero = self.FindZero(board)
        tr, tc = target
        zr, zc = zero

        if abs(tr - zr) + abs(tc - zc) == 1:
            board[zr][zc], board[tr][tc] = board[tr][tc], board[zr][zc]
            return True
        else:
            return False