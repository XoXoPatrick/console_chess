SQUARE_WIDTH = 9
BLANK_WHITE_SQUARE = ' ' * SQUARE_WIDTH
DARK_SQUARE_SYMBOL = '%'
BLANK_BLACK_SQUARE = DARK_SQUARE_SYMBOL * SQUARE_WIDTH

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