from IPython.display import clear_output 

clear_output()

# Display the game to the user
game_list = [0, 1, 2]


def display_game(game_list):
    print("\nHere is the current list: ")
    print(game_list)


# chose your position choice
def position_choice():
    choice = "wrong"

    while choice not in ["0", "1", "2"]:
        choice = input("Pick a position (0, 1, 2): ")

        if choice not in ["0", "1", "2"]:
            # This clears the output of the cell and displays the game list.
            clear_output()
            print("\nInvalid choice. Please enter a valid position.")

    return int(choice)


# let the user choose a replacement value
def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at the position: ")
    game_list[position] = user_placement

    return game_list


# Make sure the user keeps playing the game
def keep_playing():
    pick = "wrong"

    while pick not in ["Y", "N"]:
        pick = input("Keep playing? (Y or N): ")

        if pick not in ["Y", "N"]:
            print("Wrong pick. Please choose Y or N.")

    if pick.lower() == "y":
        return True
    else:
        print("\nGame Over!")


# Variable to keep game playing
game_on = True

# First Game List
game_list = [0, 1, 2]


while game_on:

    # Clear any historical output and show the game list
    clear_output()
    display_game(game_list)

    # Have player choose position
    position = position_choice()

    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)

    # Clear Screen and show the updated game list
    clear_output()
    display_game(game_list)

    # Ask if you want to keep playing
    game_on = keep_playing()