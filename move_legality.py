"""
Things legality will check for:
- is the end location on the end of the board
- does a piece on the correct team exist on the starting square
-(if not knight) is there a piece between the starting and ending positions
- does a piece inhabit the end location, and is that piece a friendly color
- is the king in check

Conditionally moves:

pawn double move:
if a pawn is on the starting rank it may advance 2 spaces

en passant:
if a pawn has advanced two spaces arriving adjacent to an enemy pawn that pawn may capture diagonally behind the enemy pawn

Castling
If neither the king, nor the rook to be castled with, have moved AND there is no piece between the two AND none of those squares is under enemy control the king will shift
2 squares towards the rook and the rook will shift 2 - 3 (depending on side) squares towards the king

IF king is under check, DOES move take king OUT of check

"""
def is_legal(piece_start, piece_stop, board, piece)-> bool:
    pass