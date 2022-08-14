from board import Board
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

class Game:
    def __init__(self):
        while True:
            self.__choose_color()
            self.__choose_difficulty()
            self.play()
            if self.wants_rematch():
                continue
            else:
                break


    def play(self):
        playing = True
        color = 'white'
        board = Board(STARTING_FEN)
        while playing:
            self.__take_turn(color, board)


    def __choose_color(self) -> None:
        self.player_color = input('Choose your color (b/w): ')
        if self.player_color == 'b':
            self.player_color = 'black'
            self.ai_color = 'white'
        else:
            self.player_color = 'white'
            self.ai_color = 'black'

    def __choose_difficulty(self):
        # self.ai = AI(difficulty)
        pass
    
    def __take_turn(self, color, board):
        pass