import random
#from Ipython.display import clear_output
def display_board(board):
    print(' '+board[7] + '|' + board[8] + '|' + board[9])
    print('--------')
    print(' '+board[4] + '|' + board[5] + '|' + board[6])
    print('--------')
    print(' '+board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker=''
    while marker != 'O' and marker !='X':
        marker=input('Player 1 , Choose X or O:')

    player1=marker
    if player1 == 'X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)

def place_marker(board, marker, postiton):
    board[postiton]=marker

def check_win(board,mark):
    return (board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)

def choose_first():
    flip= random.randint(0,1)
    if flip ==0:
        return 'Player1'
    else:
        return 'Player2'
def space_check(board,postion):
    return board[postion] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    postion=0
    while postion not in [1,2,3,4,5,6,7,8,9] or not space_check(board,postion):
        postion =int(input('Choose postion between 1-9:'))

    return postion

def replay():
    choice = input('Do you want to play again Yes or No:')
    return choice == 'Yes'


#Acutal Logic-----
print("Welcome to TIC TAC TOE")
while True:

    #Setting up Board,marker,who is first,choosing X,O
    the_board=[' ']*10
    player1_marker, player2_marker = player_input()

    turn=choose_first()
    print(turn+" will go first:")

    play_game= input("Ready to Play? y or  n: ")
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on= False

    #Game is ON

    while game_on:

        #Player1
        if turn == 'Player1':
            print("Player 1 Turn and his marker is "+player1_marker)
            display_board(the_board)
            # Choose Postion
            postion=player_choice(the_board)
            #place marker on Board
            place_marker(the_board,player1_marker,postion)
            #check if palyer 1 won
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 Won!!!!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    game_on=False

                else:
                    turn= 'Player2'


        #player2
        else:
            print("Player 2 Turn and his marker is " + player2_marker)
            display_board(the_board)
            # Choose Postion
            postion = player_choice(the_board)
            # place marker on Board
            place_marker(the_board, player2_marker, postion)
            # check if palyer 1 won
            if check_win(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 Won!!!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    game_on=False
                else:
                    turn = 'Player1'


    if not replay():
        break


