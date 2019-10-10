import math

def n_choose_k(n,k):
    comp = 1
    for i in range(n,n-k,-1):
        comp = comp * i
    denom = math.factorial(k)
    return (comp/denom)

def buildboard(n):
    board = [0]*n
    for i in range(0,n):
        board[i] = [0]*n
    open_pos = enumerate_all(board,n)

#try all in row major form
def enumerate_all(game_board, n):
    all_possible = n_choose_k(n*n,n)
    queen_counter = 0

    gb = game_board
    # Here we can take advantage of some symmetry and see if we can optimize our code to run less iterations
    opt = 1
    if n == 5: opt = 6

    for i in range(0,n):
        for j in range(0,n):
            if (queen_counter != n):
    #             gb[i][j] = 1
    #             queen_counter += 1
    #             print(gb)
    #         else:
    #             queen_counter = 0
    #             gb= buildboard(n)
    #             find_pawns(gb,n)



def find_pawns(gb, n):
    return "swag"
    # for i in range(0,n):
    #     for j in range(0,n):
    #         if gb[i][j] == 1:
            
#     for col in range(0,n):
#         for row in range(col, n):
#             game_board[col][row] = 1
#             queen_counter = -1
            # game_board = update_board(game_board)


# def update_board(game_board):
#     for i in range (0,len(game_board)):
#         for j in range(

    
# def count_pawns (board):
#     counter = 0

#     for i in range 
#     return

buildboard(2)