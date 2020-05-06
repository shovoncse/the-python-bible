# Game Status
status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Match board
match_board = [[0,1,2], [3,4,5], [6,7,8], [6,4,2], [2,5,8], [0,3,6], [0,4,8], [1,4,7]]

# Print Game board status
def game_status_disp():
    print()
    print(f'| {status[0]} | {status[1]} | {status[2]} |')
    print(f'| {status[3]} | {status[4]} | {status[5]} |')
    print(f'| {status[6]} | {status[7]} | {status[8]} |')
    print()

# Get input
def get_input(c_player):
    user_input = input(f'{c_player}: Your turn, Enter Position (0-9): ').strip()
    if user_input.isnumeric() and int(user_input) > 0 and int(user_input) < 10:
        return int(user_input)-1
    else:
        print('Wrong!!! Input, Please try again')
        return get_input(c_player)

# Game Resul Check
def game_status(*match_board):
    result = "no"
    if " " not in status:
        print("It's a Draw")
        return 1
    else:
        for item_set in match_board:
            if status[item_set[0]] == status[item_set[1]] == status[item_set[2]] != " ":
                if status[item_set[0]-1] == 'x':
                    result= "P1"
                else:
                    result = "P2"
            else:
                continue
    
    if result == "no":
        return 0
    else:
        print(f'Congrats {result}, You won the game')
        return 1


while True:
    game_status_disp()
    current_player = 'P1'
    for i in range(0,9):

        user_input = get_input(current_player)

        if current_player == "P1":
            status[user_input] = "x"
            current_player = "P2"
        else:
            status[user_input] = "o"
            current_player = "P1"

        game_status_disp()
        if game_status(*match_board):
            # clear and new game
            status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            break
        else:
            continue
        
        