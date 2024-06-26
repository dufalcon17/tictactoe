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
def check_board(board):
    global winner
    global game_Running
    # horizontal
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        game_Running = False
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        game_Running = False
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        game_Running = False
    # vertical
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        game_Running = False
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        game_Running = False
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        game_Running = False
    # diagnal
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        game_Running = False
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        game_Running = False
    elif "-" not in board:
        game_Running = False
        print("Tie Game!")
    else:
        print("Next player's turn.")
#switch player
def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
#check board

while game_Running:
    print_board(board)
    player_input(board)
    check_board(board)
    switch_player()
print("Thanks for playing!")
