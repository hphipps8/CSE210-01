#Tic-Tac-Toe Game
#Author: Hailey Phipps

def main():
    #creates a variable "board" by calling make_game_board function
    board = make_game_board()
    #creates a variable "player" by calling select_player function
    #makes player 1 use x's
    player = select_player('o')
    
    #check for conditions of a win or a tie, runs through the loop if not met
    while not (winner(board) or tie(board)):
        #shows the user the updated board
        draw_board(board)
        #let's the current player take their turn
        take_turn(player, board)
        #switches which player gets the next turn (x or o)
        player = select_player(player)
    print('Thanks for playing!')
    draw_board(board)

#sets conditions for a tie game
def tie(board):
    for box in range(9):
        #checks each index in the list to see if there are any numbers
        #left on the board for a player to choose
        if board[box] != 'x' and board[box] != 'o':
            #if there are still numbers on the board, there has NOT been a tie
            #so return False
            return False 
    #if all the numbers have been chosen AND winning conditions have NOT been met
    # the game is a tie. return True  
    print('Tie Game! Better luck next time.')      
    return True


#this function takes the users input and updates the board with their move
def take_turn(player, board):
    #gets the players box they would like to choose
    box = int(input(f"Player {player} it's your move. Pick a box (1-9): "))
    #subtracts one from user choice, to select the proper index
    board[box - 1] = player


#This function selects which players turn it is
def select_player(my_turn):
    #if it is player x's turn, then the next turn is player o
    if my_turn == "x": 
        return 'o'
    #if it is player o's turn, then the next turn is player x
    elif my_turn == 'o':
        return 'x'

#These are the conditions that are checked every pass through
#while loop at the beginning of the program
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

#this function makes a list from 1-9
def make_game_board():
    board = []
    for box in range(0, 9):
        board.append(box + 1)
    return board

#this function sets up the tic tac toe grid for the user
def draw_board(board):
    print()
    print(f'{board[0]} | {board[1]} | {board[2]} ')
    print('----------')
    print(f'{board[3]} | {board[4]} | {board[5]} ')
    print('----------')
    print(f'{board[6]} | {board[7]} | {board[8]} ')
    print()

main()