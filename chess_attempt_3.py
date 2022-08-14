#Chess Attempt #3

#Life hack:  For light and dark squares add File + Rank /2 = determine if light or dark

#create class 'piece'?

#implementation of FEN strings:  Method for representing entire chess board in a  single line of text
#creating function to disect FEN strings into board positions, additionally this will create a methodology
#for loading custom positions for tactcs/ specific scenario testing


#Create function to list all legal moves.
#calculate from each square the distance on all sides to the edge of the board??

#create ASCII chess art and then design board that fits pieces nicely
#Inherent in this representation of the board is that each piece will need to have 2 arts, one for dark
#and one for light squares

#White Pieces:
#Pawn:      Rook:      Knight:      Bishop:      Queen:      King:
#                                                 _._          +
#                       _/|                       ( )         ( )
#           [UUU]      // o\       (^)            / \         / \
# ( )        | |       || ._)      / \            | |         | |
# { }        { }       //  \       { }            { }         { }
#{___}      {___}      )___(      {___}          {___}       {___}       
#Black Pieces:
#Pawn:      Rook:      Knight:      Bishop:      Queen:      King:
#                                                 _._          +
#                       _/|                       (#)         (#)
#           [UUU]      //#o\       (^)            /#\         /#\
# (#)        |#|       ||#._)      /#\            |#|         |#|
# {#}        {#}       //##\       {#}            {#}         {#}
#{###}      {###}      )###(      {###}          {###}       {###}


#Generate Board for the computer as a 64 number string
board = [64]
SQUARE_WIDTH = 9
BLANK_WHITE_SQUARE = ' ' * SQUARE_WIDTH
DARK_SQUARE_SYMBOL = '%'
BLANK_BLACK_SQUARE = DARK_SQUARE_SYMBOL * SQUARE_WIDTH
import re
import string

#read in from FEN string and print appropriate graphic for appropriate piece

#Create a class for pieces, this will be used to dissect FEN string + potentially hold different move types of
#each piece
class Piece:
    def __init__(self, piece: str):
        # Get attr searches the attributes of what's passed in (in this case self being the instantiated Piece) 
        # to see if it has an attribute or method with the name of the string
        # In this case, if you pass in 'r', it will call the method def r(self) below
        try:
            getattr(self, piece)()
        except:
            print('Sorry, the piece you passed in doesn\'t exist. Got', piece)

    def calculate_legal_moves(self):
        legal_moves = []
        for movement in self.movements:
            if legal(movement): legal_moves.append(movement)
        return legal_moves

    def legal(self, movement):
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


#Rank Header: +------+------...
def rank_header():
    for i in range(8):
        print_inline("+---------")
    print('+')


def print_square(rank, file):
    print_inline(BLANK_BLACK_SQUARE if sq_color(rank, file) == 'dark' else BLANK_WHITE_SQUARE)


def print_inline(line):
    print(line, end = "")

def sq_color(rank: str, file: str) -> str:
    """ Method to determine the color of a given square
    rank(str): The rank for the given piece
    file(str): The file for the given piece
    return(str): 'dark' or 'light'
    """
    return "dark" if (rank + file) % 2 == 0 else "light"

def print_row(rank, partialFEN):
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

    rank_header()

 

#create function "loadPositionFromFen"
#FEN starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
#Remove '/' and appropriate number of blank spaces, try to handle the rest using the piece class
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
def load_position_from_FEN(fen):
    rank_header()
    for idx, partialFEN in enumerate(fen.split('/')):
        print_row(8 - idx, partialFEN)

load_position_from_FEN(fen)           
        

#~~intended board layout
#+------+------+------
#|######|       ######
#|######|       ######
#|######|       ######
#|######|       ######
#|######|       ######
#|######|       ######
#+------+------+------        
#        ######
#        ######
