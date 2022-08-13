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
            if legal: legal_moves.append(movement)
        return legal_moves

    def display(self, sq_color: str):
        if sq_color == 'dark' and self.color == 'black':
            return re.sub(' ', '#', self.visual)
            print(self.visual)
        elif sq_color != 'dark' and self.color != 'black':
            return re.sub('#', ' ', self.visual)
            print(self.visual)
        else:
            print(self.visual)
            return self.visual


    def r(self):
        visual = ["      ","      ","[UUU] "," |#|  "," {#}  ","{###} "]
        movements = []
        self._generate_attributes('Rook', 'r', 'black', visual, movements)

    def R(self):
        visual = ["######","######","[UUU]#","#| |##","#{ }##","{___}#"]
        movements = []
        self._generate_attributes('Rook', 'R', 'white', visual, movements)

    def n(self):
        visual = ["      "," _/|  ","//#o\ ","||#._)","//##\ ",")###( "]
        movements = []
        self._generate_attributes('Knight', 'n', 'black', visual, movements)

    def N(self):
        visual = ["######","#_/|##","// o\#","|| ._)","//  \#",")___(#"]
        movements = []
        self._generate_attributes('Knight', 'K', 'white', visual, movements)

    def b(self):
        visual = ["      ","      "," (^)  "," /#\  "," {#}  ","{###} "]
        movements = []
        self._generate_attributes('Bishop', 'b', 'black', visual, movements)

    def B(self):
        visual = ["######","#_/|##","// o\#","|| ._)","//  \#",")___(#"]
        movements = []
        self._generate_attributes('Bishop', 'B', 'white', visual, movements)

    def p(self):
        visual = ["      ","      ", "      "," (#)  "," {#}  ","{###} "]
        movements = []
        self._generate_attributes('Pawn', 'p', 'black', visual, movements)

    def P(self):
        visual = ["######","######","######","#( )##","#{ }##","{___}#"]
        movements = []
        self._generate_attributes('Pawn', 'P', 'white', visual, movements)
        

    def _generate_attributes(self, name, char, color, visual, movements):
        self.name = name
        self.char = char
        self.color = color
        self.visual = visual
        self.movements = movements

class Rook(Piece):
    def __init__(self, color: str):
        movements = []
        if color == "black":
            c1har = "n"
            visual = ["      ","      ","[UUU] "," |#|  "," {#}  ","{###} "]
        else:
            char = "N"
            visual = ["######","######","[UUU]#","#| |##","#{ }##","{___}#"]
        super().__init__("Rook", char, color, visual, movements)

class Knight(Piece):
    def __init__(self, color: str):
        movements = []
        if color == "black":
            char = "n"
            visual = ["      ","      "," (^)  "," /#\  "," {#}  ","{###} "]
        else:
            char = "N"
            visual = ["######","#_/|##","// o\#","|| ._)","//  \#",")___(#"]
        super().__init__("Knight", char, color, visual, movements)

class Bishop(Piece):
    def __init__(self, color: str):
        movements = []
        if color == "black":
            char = "b"
            visual = ["      ","      "," (^)  "," /#\  "," {#}  ","{###} "]
        else:
            char = "B"
            visual = ["######", "######", "#(^)##","#/ \##","#{ }##","{___}#"]
        super().__init__("Bishop", char, color, visual, movements)

class Queen(Piece):
    def __init__(self, color: str):
        movements = []
        if color == "black":
            char = "q"
            visual = [" _._  "," (#)  "," /#\  "," |#|  "," {#}  ","{###} "]
        else:
            char = "Q"
            visual = ["#_._##","#( )##","#/ \##","#| |##","#{ }##","{___}#"]
        super().__init__("Bishop", char, color, visual, movements)

class King(Piece):
    def __init__(self, color: str):
        movements = []
        if color == "black":
            char = "k"
            visual = ["##+###","#(#)##","#/#\##","#|#|##","#{#}##","{###}#"]
        else:
            char = "K"
            visual = ["##+###","#( )##","#/ \##","#| |##","#{ }##","{___}#"]
        super().__init__("Bishop", char, color, visual, movements)

class Pawn(Piece):
    def __init__(self, color: str):
        movements = []
        if color == "black":
            char = "p"
            visual = ["      ","      ", "      "," (#)  "," {#}  ","{###} "]
        else:
            char = "P"
            visual = ["######","######","######","#( )##","#{ }##","{___}#"]
        super().__init__("Bishop", char, color, visual, movements)

#Rank Header: +------+------...
def rank_header():
    i = 0
    while(i < 8):
        print("+------", end = "")
        i = i + 1
        if i == 8:
            print("+")

def print_row(rank, file, sq_color=None):
    if sq_color is None: 
        sq_color = sq_color(rank, file)
    if sq_color == "dark":
        print("|######", end ="")
    else:
        print("|      ", end = "")
    return file

def sq_color(rank: str, file: str) -> str:
    """
    rank(str): The rank for the given piece
    file(str): The file for the given piece
    return(str): 'dark' or 'light'
    """
    return "dark" if (rank + file) % 2 == 0 else "light"

def print_board(rank, partialFEN, file=1):
    for x in range(6):
        for char in partialFEN:
            if char.isdigit():
                for y in range(int(char)):
                    print_row(rank, file)
                if file == 7:
                    pass
                else:
                    file += 1
            else:
                #need to modify now that sq_color has been modified w/ print row function
                Piece(char).display(sq_color(rank,file))
                file += 1
            if file == 7:
                print("|")
                file = 1

    rank_header()

 

#create function "loadPositionFromFen"
#FEN starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
#Remove '/' and appropriate number of blank spaces, try to handle the rest using the piece class
fen = "8/8/8/8/8/8/8/8/"
def load_position_from_FEN(fen):
    rank = 8
    partialFEN = ""
    rank_header()
    for char in fen:
        if char == '/':
            print_board(rank, partialFEN)
            partialFEN = ""
            rank = rank - 1
        else:
            partialFEN = partialFEN + char

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
