import random
import time

class TicTacToe:

    def __init__(self):
        self.board = []
        self.player_2 = ''

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    @staticmethod
    def get_random_first_player():
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False


    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    @staticmethod
    def swap_player_turn(player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # _THUNDER_
    def ai(self):
        arr = []

        # TESTING AI
        # self.create_board()
        # self.fix_spot(2,1,'X')
        # self.fix_spot(0,1,'X')
        # self.fix_spot(2,0,'X')
        # self.fix_spot(0,2,'X')
        # self.show_board()

        #GETTING ALL EMPTY SPACES
        for row in enumerate(self.board):
            index = row[0]
            for item in enumerate(row[1]):
                if item[1] == '-':
                    arr.append([index ,item[0]])
        rand = random.randint(0, len(arr)-1)
        move = arr[rand]
        self.fix_spot(move[0],move[1],self.player_2)
    # end(_THUNDER_)

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'

        # _THUNDER_
        if player == 'X':
            self.player_2 = 'O'
        else:
            self.player_2 = 'X'

        print("3 ",end='')
        time.sleep(0.3)
        print("2 ",end='')
        time.sleep(0.3)
        print("1 ",end='')
        time.sleep(0.3)
        print(". ",end='')
        time.sleep(0.3)
        print(". ",end='')
        time.sleep(0.3)
        print("Go! ",end='')
        print('')
        self.show_board()
        # end(_THUNDER_)

        while True:
            print(f"Player {player} turn")

            # self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # _THUNDER_
            self.show_board()
            # AI PLAYS
            time.sleep(1)
            print(f"Player {self.player_2} turn")
            self.ai()
            self.show_board()
            # end(_THUNDER_)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_player_win(self.player_2): # _THUNDER_
                print(f"Player {self.player_2} wins the game!") # _THUNDER_
                break # _THUNDER_

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            # player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
