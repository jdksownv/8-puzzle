from Engine import PuzzleEngine
from Input import PuzzleInput
from Make import PuzzleMake
from UI import PuzzleUI


class PuzzleController:
    def __init__(self):
        self.input = PuzzleInput()
        self.ui = None
        self.make = None
        self.engine = None

        self.size = 0
        self.goal_board = None
        self.current_board = None
        self.move_count = 0
        self.running = True

    def Run(self):
        while True:
            while True:
                size_command = self.input.GetSize()
                if size_command == "EXIT":
                    temp_ui = PuzzleUI(0)
                    temp_ui.Exit()
                    return

                if isinstance(size_command, int) and size_command >= 3:
                    self.size = size_command
                    break
                else:
                    temp_ui = PuzzleUI(0)
                    temp_ui.SizeError()

            self.ui = PuzzleUI(self.size)
            self.make = PuzzleMake(self.size)
            self.engine = PuzzleEngine(self.size)

            self.goal_board = self.make.Transformation(self.make.MakeGoal())
            self.current_board = self.make.Random()
            self.move_count = 0
            self.running = True

            while self.running:
                self.ui.DisplayBoard(self.current_board, self.move_count)
                if self.engine.CheckWin(self.current_board, self.goal_board):
                    self.ui.Victory(self.move_count)
                    self.running = False
                    break
                move_command = self.input.GetMove()

                if move_command == "GIVE_UP":
                    self.ui.GiveUp()
                    self.running = False
                    break

                if not isinstance(move_command, int):
                    self.ui.InputError()
                    continue

                success = self.engine.Move(self.current_board, move_command)
                if success:
                    self.move_count += 1
                else:
                    self.ui.MoveError()

            while True:
                choice = self.input.GetRestart()
                if choice == "RESTART":
                    break
                elif choice == "EXIT":
                    self.ui.Exit()
                    return
                else:
                    self.ui.RestartError()


if __name__ == "__main__":
    game = PuzzleController()
    game.Run()