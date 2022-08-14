from helpers import *
from piece import Piece


class Board:
    def __init__(self, boardFEN: str):
        self.boardFEN = boardFEN
        self.__load_position_from_FEN(self.boardFEN)

    #create function "loadPositionFromFen"
    #FEN starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    #Remove '/' and appropriate number of blank spaces, try to handle the rest using the piece class
    def __load_position_from_FEN(self, fen):
        self.__rank_header()
        for idx, partialFEN in enumerate(fen.split('/')):
            self.__print_row(8 - idx, partialFEN)


#Rank Header: +------+------...
    def __rank_header(self):
        for i in range(8):
            print_inline("+---------")
        print('+')

    def __print_row(self, rank: int, partialFEN: str) -> None:
        """ ***Private*** Prints a row for the rank and partial fen
        rank(int): The rank of the row being printed
        partialFEN(str): The FEN for the row being printed
        """
        file = 1
        for x in range(6):
            for char in partialFEN:
                if char.isdigit():
                    for y in range(int(char)):
                        print_inline('|')
                        print_square(rank, file)
                        file += 1
                else:
                    print_inline("|")
                    Piece(char).display(sq_color(rank, file), x)
                    file += 1
            print("|")

        self.__rank_header()