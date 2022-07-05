import time


#time.sleep(1)


#'♔' for the black King;
#'♛' for a white Queen;
#'♝' for a white Bishop;
#'♞' for a white Knight;
#'♜' for a white Rook;
#'♟' for a white Pawn;


def king_is_in_check(chessboard):
    king = king_location(chessboard)
    pawn_attacks = pawn(chessboard)
    for i in range(len(pawn_attacks)):
        if pawn_attacks[i] == king:
            return True
    return False


             
def king_location(chessboard):    #takes in the chessboard returns kings location in list of [pos1,pos2]
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if chessboard[i][j] == '♔':
                return [i,j]



def pawn(chessboard): #takes in the chessboard, returns a nested list of hot spots for the king [[c1,r1],[c2,r2]]
    hot_spots = []
    pawn_position = [0,0]
    for column in range(len(chessboard)):
        for row in range(len(chessboard[column])):
            if chessboard[column][row] == '♟':
                pawn_position = [column,row]
    if pawn_position[0] < 7 and pawn_position[1]>0 and pawn_position[1]<7:
        hot_spots.insert(0,[pawn_position[0] + 1, pawn_position[1] - 1])
        hot_spots.insert(1,[pawn_position[0] + 1, pawn_position[1] + 1])
    
    return hot_spots










print(king_is_in_check([
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♟',' ',' ',' ',' '],
            [' ',' ','♔',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ]))


