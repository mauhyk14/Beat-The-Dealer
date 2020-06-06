#
# File:     huayy092_player_info.py
# Author:   Ying Ke Huang
# Email Id: huayy092
# Description: Assignment 2 - This program will simulate a BlackJack game.
# The user has the option to modify the players stored in the player list.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import player
import blackjack
import list_function

# Function user_input_varification () - This function ensures the user input a validate command.
def user_input_varification ():

    print('Please enter choice ')
    user_input = input('[players, buy, search, clear, add, remove, play, quit]: ')

    while user_input != 'players' and user_input != 'buy' and user_input != 'search' and user_input != 'clear' and user_input != 'add' and user_input != 'remove' and user_input != 'play' and user_input != 'quit':
        print()
        print('Not a valid command - please try again.', '\n', '\n')
        print('Please enter choice ')
        user_input = input('[players, buy, search, clear, add, remove, play, quit]: ')

    return user_input


# Function read_file() - This function reads the text file and returns a list with all the players.
# objects.
def read_file(filename, player_list):

    # Place your code here
    filename = 'players.txt'    
    infile = open(filename, 'r')
    new_list = []

    string = infile.readline()
    # This while function allows me to remove '\n' and reconstruct a list with the same
    # information as the text file.
    while string != '':

        new_string = string.strip()

        new_list.append(new_string)

        string = infile.readline()
        

    line_counter = 0

    # These few lines of code create each individual object based on the new list. The even number
    # elements store the player's name, and the odd number elements cretae the player's object by
    # assigning the appopriated information.
    for element in new_list:

        if line_counter % 2 == 0:
            player_name = element

        else:
            score_list = element.split()
            started_player = player.Player(player_name, int(score_list[0]), int(score_list[1]), int(score_list[2]), int(score_list[3]), int(score_list[4]), int(score_list[5]))

            player_list.append(started_player)

        line_counter += 1

    infile.close()
    return player_list


# Function display_players() - This function displays the object's information according
# to the assignment format.
def display_players(player_list):
    
    # Place your code here
    print('===========================================================')
    print('-', end = '')
    print(format('Player Summary', '>35'), end ='' )
    print(format('-', '>23'))
    print('===========================================================')
    print('-', end ='')
    print(format('P  W  L  D   Chips   Score', '>55'), end = '')
    print(format('-', '>3'))
    print('-----------------------------------------------------------')

    if len(player_list) == 0:

        print('\n', '\n', 'No players to display!', '\n')

    else:
    
        for player_object in player_list:

            print('-  ', end ='')
            
            print(player_object, ' -')

            print('-----------------------------------------------------------')

    print('===========================================================')
    print()

       
# Function write_to_file() - This function accepts filename and player_list parameters to
# write to a new_players.txt file.
def write_to_file(filename, player_list):
    
    # Place your code here
    outfile = open(filename, 'w')

    for players in range (len(player_list)):

        outfile.write(player_list[players].get_name() + '\n')

        outfile.write(str(player_list[players].get_games_played()) + ' ' + str(player_list[players].get_no_won()) + ' ' + \
                      str(player_list[players].get_no_lost()) + ' ' + str(player_list[players].get_no_drawn()) + ' ' + \
                      str(player_list[players].get_chips()) + ' ' + str(player_list[players].get_total_score()) + '\n')

    outfile.close()
        

# Function find_player() - This function will look for the name from the objects of
# the player_list that matches the user's input. The function will return the position
# of the player found in the list if there is a match. Otherwise, the value -1 will be returned.
def find_player(player_list, name):
    
    # Place your code here
    position_counter = -1
    position = 0

    for element in range (len(player_list)):

        if name == player_list[element].get_name():

            position = element + 1

    result = position_counter + position

    return result
       

# Function add_player() - This function accepts an input from the user then looks
# for the name attributes from the player_list objects. If a match is found, it will
# display an error message. Otherwise, a new object will be created and added to the
# player_list.
def add_player(player_list):
    
    # Place your code here
    print()
    name = input('Please enter name: ')

    add_player_value = find_player(player_list, name)

    if add_player_value == -1:

        new_player = player.Player(name)

        player_list.append(new_player)

        print()
        print('Successfully added', name, 'to player list.', '\n', '\n')

    else:
        print()
        print(name, 'already exists in player list.', '\n', '\n')

    return player_list

    
# Function remove_player() - This function uses the remove_value function in Part 1
# to remove the selected object from the player_list. If the player doesn't exist in
# the list, it will return an error message. After the execution of this function, it
# will return an updated player_list.
def remove_player(player_list):
    
    # Place your code here
    print()
    name = input("Please enter name: ")
    print()

    position = find_player(player_list, name)

    if position == -1:

        print(name, 'is not found in players.', '\n', '\n')

    else:
        player_list = list_function.remove_value(player_list, position)
        print('Successfully remove', name, 'from player list.', '\n', '\n')

    return player_list
        

# Function buy_player_chips() - This function uses the pos value from the find_player function
# to locate the player object in the player list. Once the player has been found, the function
# will update the player's chip balance according to the user's input by using the set_chips
# method. If the user input is not exist in the list, an error message will be displayed.
def buy_player_chips(player_list, pos):
    
    # Place your code here
    current_chips = player_list[pos].get_chips()
    player_name = player_list[pos].get_name()
    display_chips = str(current_chips) + ' chips.'

    print()
    print(player_name, 'currently has', display_chips, '\n')

    buy_chips = int(input('How many chips would you like to buy? '))

    while buy_chips < 0 or buy_chips > 100:
        print('You may only buy between 1-100 chips at a time!', '\n')
        buy_chips = int(input('How many chips would you like to buy? '))

    total_chips = current_chips + buy_chips

    player_list[pos].set_chips(total_chips)
    print()
    print('Successfully updated', player_name, 'chips balance to', total_chips, '\n', '\n')
    
        
   
# Function clear_player_stats() - The function will reset the player's statistics
# back to 0 if the player is in the player_list. I initialise the clear_function_indicator
# as 0(False condition) so if find_player function comes back with a positive integer,
# the return value will change to 1.
def clear_player_stats (player_list, name):
    
    # Place your code here
    player_object_position = find_player(player_list, name)

    clear_function_indicator = 0

    if player_object_position != -1:

        player_list[player_object_position].set_games_played(0)
        player_list[player_object_position].set_no_won(0)
        player_list[player_object_position].set_no_lost(0)
        player_list[player_object_position].set_no_drawn(0)
        player_list[player_object_position].set_chips(0)
        player_list[player_object_position].set_total_score(0)

        clear_function_indicator = 1

    return clear_function_indicator
    

# Function play_blackjack_games() - The function uses the player_pos to locate the player's object
# in the player_list. Based on the outcomes of the game_result and chip balances, the function
# modifies the player's object accordingly. 
def play_blackjack_games (player_list, player_pos):

    game_result = 0   # Stores result of blackjack game - 3 for win, 1 for draw, 0 for loss.
    no_chips = 0      # Number of chips held by the player.
    again = 'y'       # Stores player's response to whether we keep looping.

    # While player would like to keep playing.
    while (again == 'y' or again == 'Y'):

        # Plays one game of blackJack and assigns the result of the game and the chip balance
        # to variables game_result and no_chips respectively.
        game_result, no_chips = blackjack.play_one_game(player_list[player_pos].get_chips())
        
        # Update player stats.

        # Place your code here...  : )
        
        # After every game, the selected player's game_play attribute will increase by 1 and
        # the object's set_chip attribute will reset by the no_chip variable accordingly. Statements
        # from different conditions will execute based on on the outcomes of game_result variables.
        player_list[player_pos].increment_games_played()
        player_list[player_pos].set_chips(no_chips)

        if game_result == 3:

            player_list[player_pos].increment_no_won()
            player_list[player_pos].increment_total_score(3)

        elif game_result == 0:

            player_list[player_pos].increment_no_lost()
            player_list[player_pos].increment_total_score(0)

        elif game_result == 1:

            player_list[player_pos].increment_no_drawn()
            player_list[player_pos].increment_total_score(1)
            
            
        # Prompt for and read whether the player would like to play again.
        again = input("\nPlay again [y|n]? ")
        print()
        
        while again != 'n' and again != 'y':
            again = input("\nPlay again [y|n]? ")
            


### Define list to store player information
player_list = []


### Place your code here...  : )

print('File     : wayby001_player_info.py')
print('Author   : Batman')
print('Stud ID  : 0123456X')
print('Email ID : wayby001')
print("This is my own work as defined by the University's Academic Misconduct Policy", '\n', '\n')

# The read_file function will constrcut the player list based on players.txt file when
# the program begins.
read_file(read_file,player_list)


user_input = 'y'

# As long as the user doesn't input quit in the menu option, the while loop will
# ensure the program to keep going.
while user_input != 'quit':

    user_input = user_input_varification()
    
    # Display the player's status according to the format.    
    if user_input == 'players':

        print()

        display_players(player_list)


    elif user_input == 'search':

        print()

        name = input('Please enter name: ')

        search_result = find_player(player_list, name)

        # Based on the search_result, the if statement will display
        # the player's object information according to the format or
        # display the not found message.
        if search_result == -1:
            print()
            print(name, 'is not found in player list.', '\n', '\n')

        else:
            print()
            print(player_list[search_result].get_name(), 'stats:', '\n')
            print('P  W  L  D  Score')
            print(player_list[search_result].get_games_played(), end ='')
            print(format(player_list[search_result].get_no_won(), '>3d'), end ='')
            print(format(player_list[search_result].get_no_lost(), '>3d'), end = '')
            print(format(player_list[search_result].get_no_drawn(), '>3d'), end ='')
            print(format(player_list[search_result].get_total_score(), '>4d'), '\n')
            print('Chips: ', player_list[search_result].get_chips(), '\n', '\n')

    # The clear option sets the player's status to 0 if the player is in the list.
    # Otherwise, the program will display an error message.
    elif user_input == 'clear':
        print()
        name = input('Please enter name: ')

        clear_result = clear_player_stats (player_list, name)

        if clear_result == 1:
            display_name = str(name) + "'s"
            print()
            print('Successfully cleared', display_name, 'statistics.', '\n', '\n')

        else:
            print()
            print(name, 'is not found in player list.', '\n', '\n')


    elif user_input == 'add':

        player_list = add_player(player_list)

    # The buy option allows the user to update the player's chip balance. If the
    # the player is found in the list, the program uses the find_player function
    # to locate the player's object. If the player is not found, an error message
    # will be displayed.
    elif user_input == 'buy':
        print()
        name = input('Please enter name: ')

        pos = find_player(player_list, name)

        if pos == -1:
            print()
            print(name, 'is not found in player list.', '\n', '\n')

        else:
            buy_player_chips(player_list, pos)

    elif user_input == 'remove':

        player_list = remove_player(player_list)

    # The buy command gives the player the opportunity to play a game of Blackjack.
    # At the end of each game, the player's status is updated, and the while loop
    # gives the player a choice to keep playing until he/she doesn't want to continue
    # playing.
    elif user_input == 'play':
        
        print()
        name = input('Please enter name: ')

        player_pos = find_player(player_list, name)

        if player_pos == -1:
            print()
            print(name, 'is not found in player list.', '\n', '\n')

        else:
            play_blackjack_games (player_list, player_pos)


print("\n\n-- Program terminating --\n")

# Once the user quit the program, the player_list and filename variable
# will be passed to write_to_file function. The function accept both parameters
# to carry out the write file statements.
filename = 'new_players.txt'
write_to_file(filename, player_list)


