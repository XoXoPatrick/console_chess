import re
from helpers import *

class Piece:
    def __init__(self, piece: str):
        # Get attr searches the attributes of what's passed in (in this case self being the instantiated Piece) 
        # to see if it has an attribute or method with the name of the string
        # In this case, if you pass in 'r', it will call the method def r(self) below
        try:
            getattr(self, piece)()
        except:
            print('Sorry, the piece you passed in doesn\'t exist. Got', piece)

    def calculate_legal_moves(self, board):
        legal_moves = []
        for movement in self.movements:
            if self.is_legal(movement, board): legal_moves.append(movement)
        return legal_moves

    def is_legal(self, movement: str, board: str) -> bool:
        pass

    def display(self, sq_color: str, idx: int) -> str:
        if sq_color == 'dark' and self.color == 'black':
            print_inline(re.sub(' ', DARK_SQUARE_SYMBOL, self.visual[idx]))
        elif sq_color != 'dark' and self.color != 'black':
            print_inline(re.sub(DARK_SQUARE_SYMBOL, ' ', self.visual[idx]))
        else:
            print_inline(self.visual[idx])


    def r(self):
        visual = [BLANK_WHITE_SQUARE, BLANK_WHITE_SQUARE,"  [UUU]  ","   |#|   ","   {#}   ","  {###}  "]
        movements = []
        self.__generate_attributes('Rook', 'r', 'black', visual, movements)

    def R(self):
        visual = [BLANK_BLACK_SQUARE,BLANK_BLACK_SQUARE,"%%[UUU]%%","%%%| |%%%","%%%{ }%%%","%%{___}%%"]
        movements = []
        self.__generate_attributes('Rook', 'R', 'white', visual, movements)

    def n(self):
        visual = [ BLANK_WHITE_SQUARE,"   _/|   ","  //#o\  ","  ||#._) ","  //##\  ","  )###(  "]
        movements = []
        self.__generate_attributes('Knight', 'n', 'black', visual, movements)

    def N(self):
        visual = [BLANK_BLACK_SQUARE,"%%%_/|%%%","%%// o\%%","%%|| ._)%","%%//  \%%","%%)___(%%"]
        movements = []
        self.__generate_attributes('Knight', 'K', 'white', visual, movements)

    def b(self):
        visual = [ BLANK_WHITE_SQUARE, BLANK_WHITE_SQUARE,"   (^)   ","   /#\   ","   {#}   ","  {###}  "]
        movements = []
        self.__generate_attributes('Bishop', 'b', 'black', visual, movements)

    def B(self):
        visual = [BLANK_BLACK_SQUARE,"%%%_/|%%%","%%// o\%%","%%|| ._)%","%%//  \%%","%%)___(%%"]
        movements = []
        self.__generate_attributes('Bishop', 'B', 'white', visual, movements)

    def p(self):
        visual = [ BLANK_WHITE_SQUARE, BLANK_WHITE_SQUARE,  BLANK_WHITE_SQUARE,"   (#)   ","   {#}   ","  {###}  "]
        movements = []
        self.__generate_attributes('Pawn', 'p', 'black', visual, movements)

    def P(self):
        visual = [BLANK_BLACK_SQUARE,BLANK_BLACK_SQUARE,BLANK_BLACK_SQUARE,"%%%( )%%%","%%%{ }%%%","%%{___}%%"]
        movements = []
        self.__generate_attributes('Pawn', 'P', 'white', visual, movements)

    def q(self):
        visual = ["   _._   ","   (#)   ","   /#\   ","   |#|   ","   {#}   ","  {###}  "]
        movements = []
        self.__generate_attributes('Pawn', 'p', 'black', visual, movements)

    def Q(self):
        visual = ["%%%_._%%%","%%%( )%%%","%%%/ \%%%","%%%| |%%%","%%%{ }%%%","%%{___}%%"]
        movements = []
        self.__generate_attributes('Pawn', 'P', 'white', visual, movements)

    def k(self):
        visual = ["    +    ","   (#)   ","   /#\   ","   |#|   ","   {#}   ", "  {###}  "]
        movements = []
        self.__generate_attributes('Pawn', 'p', 'black', visual, movements)

    def K(self):
        visual = ["%%%%+%%%%","%%%( )%%%","%%%/ \%%%","%%%| |%%%","%%%{ }%%%","%%{___}%%"]
        movements = []
        self.__generate_attributes('Pawn', 'P', 'white', visual, movements)
        

    def __generate_attributes(self, name, char, color, visual, movements):
        self.name = name
        self.char = char
        self.color = color
        self.visual = visual
        self.movements = movements
