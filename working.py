board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    
    for i in range(len(board)):
        # sudoku board is made up of 3x3 squares
        # this is to break up rows
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        # board[0] = len of rows
        for j in range(len(board[0])):
            # checking to make sure it is not the 0th colum
            # 0 % 3 === 0 and would print out on the edge
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # as opposed to default line ending of \n
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#print_board(board)

"""
    Given a board, find empty square. empty = 0
"""
def find_empty(board):
    # iterate through the rows
    for i in range(len(board)):
        # iterate through the columns
        for j in range(len(board[0])):
            # if the number in the space is 'empty' (0) return it
            if board[i][j] == 0:
                return (i, j)   # row, col
            
#print(find_empty(board))


