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

# Get input method
def get_input(c_player):

    # user input
    user_input = input(f'{c_player}: Your turn, Enter Position (0-9): ').strip()

    # Check for win result
    if user_input.isnumeric() and int(user_input) > 0 and int(user_input) < 10:
        if status[int(user_input)-1] != " ":
            print('Wrong!!! Input already used')
            return get_input(c_player)
        else:
            return int(user_input)-1
    else:
        print('Wrong input!!!, Please try again')
        return get_input(c_player)

# Game Result Check
def game_status(*match_board):
    
    # initial result
    result = "no"

    # Check for win result
    for item_set in match_board:
        if status[item_set[0]] == status[item_set[1]] == status[item_set[2]] != " ":
            if status[item_set[0]] == 'x':
                result= "P1(x)"
            else:
                result = "P2(o)"
        else:
            continue
    
    # Match draw
    if result == "no" and " " not in status:
        print("It's a Draw")
        return 1
    
    # Continue
    if result == "no":
        return 0
    # Winner Found
    else:
        print(f'Congrats {result}, You won the game')
        return 1


# Game Stars
while True:

    # initial display
    game_status_disp()

    # Current Player
    current_player = 'P1(x)'

    # 9 times lifecycle
    for i in range(0,9):

        # get input
        user_input = get_input(current_player)

        if current_player == "P1(x)":
            status[user_input] = "x"
            current_player = "P2(o)"
        else:
            status[user_input] = "o"
            current_player = "P1(x)"

        # Current Status
        game_status_disp()

        # Search the result
        if game_status(*match_board):
            # clear and new game
            status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            break
        # if no result yet
        else:
            continue
        
        