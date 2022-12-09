import numpy as np

class Connect4:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.current_player = 1

    def make_move(self, column):
        row = np.where(self.board[:, column] == 0)[0]
        if not row.size:
            print('Column is full, please select a different column.')
            return

        row = row[-1]
        self.board[row, column] = self.current_player
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def check_win(self):
        # Check for horizontal win
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1] - 3):
                if self.board[row, col] != 0 and \
                        self.board[row, col] == self.board[row, col+1] == self.board[row, col+2] == self.board[row, col+3]:
                    return self.board[row, col]

        # Check for vertical win
        for row in range(self.board.shape[0] - 3):
            for col in range(self.board.shape[1]):
                if self.board[row, col] != 0 and \
                        self.board[row, col] == self.board[row+1, col] == self.board[row+2, col] == self.board[row+3, col]:
                    return self.board[row, col]

        # Check for diagonal win (top-left to bottom-right)
        for row in range(self.board.shape[0] - 3):
            for col in range(self.board.shape[1] - 3):
                if self.board[row, col] != 0 and \
                        self.board[row, col] == self.board[row+1, col+1] == self.board[row+2, col+2] == self.board[row+3, col+3]:
                    return self.board[row, col]

        # Check for diagonal win (top-right to bottom-left)
        for row in range(self.board.shape[0] - 3):
            for col in range(3, self.board.shape[1]):
                if self.board[row, col] != 0 and \
                        self.board[row, col] == self.board[row+1, col-1] == self.board[row+2, col-2] == self.board[row+3, col-3]:
                    return self.board[row, col]

        # Check for draw
        if np.all(self.board != 0):
            return 3

        # No win or draw, continue game
        return 0

    def print_board(self):
        print(self.board)

# Initialize game
game = Connect4()

if __name__ == '__main__':
    # Play game
    while True:
        # Print board
        game.print_board()

        # Get player input
        move = int(input('Player {}: Select column to play (0-6): '.format(game.current_player)))

        # Check if column is full
        if game.board[:, move].all():
            print('Column is full, please select a different column.')
            continue

        # Make move
        game.make_move(move)

        # Check if game is over
        result = game.check_win()
        if result != 0:
            game.print_board()
            if result == 1:
                print('Player 1 wins!')
            elif result == 2:
                print('Player 2 wins!')
            else:
                print('Draw!')
            break