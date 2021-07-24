# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Ball Crush

from random import randint
import time

# INSERT YOUR CODE HERE ...

# DISPLAY BOARD FUNCTION

def display_board(board):
    rows = len(board)
    
    for row in range(rows):
        print(board[row])
        
# DISPLAY BALL POSITIONS FUNCTION

def display_ball_positions(ball_positions):
    ball_positions_temp = []

    for tuple_ in ball_positions: # for indexing ball_positions
        row = tuple_[0] + 1
        col = tuple_[1] + 1
        tuple_temp = row, col
        ball_positions_temp.append(tuple_temp)
    
    print(ball_positions_temp)
    
# CHOOSE BALL FUNCTION

def choose_ball(board):
    
    while True: # loop for valid ball choice input
        choice = input("Which ball? ")
        row_and_col = choice.split(",")
        row = row_and_col[0]
        col = row_and_col[1]
        flag = "continue"
        
        if len(row_and_col) != 2: # checking the lenght of the input
            print("You must enter a valid tuple [i.e => (a, b)]")
            continue
        
        try:
            row = int(row)
            col = int(col)

            if board[row-1][col-1] == 1:
                flag = "break"                

            else:
                print("It is not a ball position.")

        except:
            print("It is not a ball position.")
        
        if flag == "break":
            break
    
    return row, col
          
# GET VALID MOVES FUNCTION
  
def get_valid_moves(pos, len_board):
    valid_moves_list = []
    
    if pos[0] != 1:
        valid_moves_list.append("w")
        
    if pos[0] != len_board:
        valid_moves_list.append("s")
        
    if pos[1] != 1:
        valid_moves_list.append("a")
        
    if pos[1] != len_board:
        valid_moves_list.append("d")
    
    return valid_moves_list

# MAKE MOVE FUNCTION

def make_move(board, pos, valid_moves, ball_positions):
    
    row = pos[0]
    col = pos[1]
    rowminus1 = pos[0] - 1
    colminus1 = pos[1] - 1
    posminus1 = rowminus1, colminus1
    indx = ball_positions.index(posminus1)
    
    while True: # Infinite for loop for valid input for move
        direction = input("Your move? ")  
        
        if direction not in valid_moves:
            print("Enter a valid direction!")
            continue
        
        elif direction == "w":
            board[row-1][col-1] = 0
            row -= 1
            pos = row - 1, col - 1

        elif direction == "s":
            board[row-1][col-1] = 0
            row += 1
            pos = row - 1, col - 1

        elif direction == "d":
            board[row-1][col-1] = 0
            col += 1
            pos = row - 1, col - 1

        else:
            board[row-1][col-1] = 0
            col -= 1
            pos = row - 1, col - 1

        break

    ball_positions[indx] = pos

    if check_collision(board, pos) == True: # if collision then delete ball
        delete_ball(board, pos, ball_positions)    
    
    for position in ball_positions: # for deleting same positions
        
        if ball_positions.count(position) > 1:
            ball_positions.remove(position)
    
    board[row-1][col-1] = 1 # board updates

# DELETE BALL FUNCTION

def delete_ball(board, pos, ball_positions):
    
    row = pos[0]
    col = pos[1] 
    
    board[row-1][col-1] = 0
    
# CHECK COLLISION FUNCTION
    
def check_collision(board, pos):
    
    collision = False
       
    if board[pos[0]-1][pos[1]-1] == 1:
        collision = True
        
    return collision

# MAIN

def main():
    len_board = 5
    board = [[0 for col in range(len_board)] for row in range(len_board)]  
 
    while True:
        ball_positions = [(randint(0, len_board-1), randint(0, len_board-1)) for i in range(3)]
        if len(ball_positions) == len(set(ball_positions)):
            break
    
    for pos in ball_positions:
        board[pos[0]][pos[1]] = 1

    start_time = time.time()
    
    while True:
        display_ball_positions(ball_positions)
        display_board(board)
        
        if len(ball_positions) == 1:
            break
        
        ball_pos = choose_ball(board)
        
        valid_moves = get_valid_moves(ball_pos, len(board))
        print("Valid moves:", valid_moves)
        
        make_move(board, ball_pos, valid_moves, ball_positions)
        
    end_time = time.time()

    minutes, seconds = divmod(end_time-start_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("Game Over!")
    print("Passed time= {:02d}:{:02d}:{:02d}".format(int(hours), int(minutes),int(seconds)))
    
main()


