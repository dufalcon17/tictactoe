# joshua Younger

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "x"
winner = None
game_Running = True

#print board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#print_board(board)

#player input
def player_input(board):
    inp = int(input("Enter a number 1 - 9."))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = current_player
#check board

#switch player
def switch_player():
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
#check board
