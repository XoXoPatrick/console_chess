from operator import is_
from board import Board
from move_legality import is_legal
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

class Game:
    def __init__(self):
        while True:
            self.__choose_color()
            self.__choose_difficulty()
            self.__play()
            if self.__wants_rematch():
                continue
            else:
                break


    def __play(self):
        playing = True
        self.board = Board(STARTING_FEN)
        self.turn = 1
        while playing:
            self.__take_turn()


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
    
    def __take_turn(self):
        if self.player_color == self.__turn_color():
            self.__player_turn()
        else:
            self.__ai_turn()
        self.turn += 1

    def __player_turn(self):
        piece_start = input('Enter the Rank and File of the Piece:')
        piece_stop = input('Enter the Rank and File of where you would like the piece to go: ')
        if is_legal(piece_start, piece_stop, self.board.boardFEN): #true pass to board.update_board
            pass
        else:
            print('There was an issue with that selection, please try again.')
            self.__player_turn()
    
    def __ai_turn(self):
        pass

    def __turn_color(self):
        return 'black' if self.turn % 2 == 0 else 'white'

    def __wants_rematch(self) -> bool:
        return input('Do you want a rematch? (y/n): ') == 'y'