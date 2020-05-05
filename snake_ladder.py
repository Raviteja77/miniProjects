import random
import sys
class Game:
    def get_player_name(self):
            player1_name = None
            while not player1_name:
                player1_name = input("Please enter a name: ")
            return player1_name
    def get_dice_value(self):
        dice = random.randint(1,6)
        print("Its a "+ str(dice))
        return dice
    def snake_ladder(self,player,current_value,dice):
        snakes = {19: 1, 26: 8, 39: 5, 56: 6, 75: 28, 85: 47, 92: 25, 99: 58}
        ladders = {3: 24, 11: 49, 17: 74, 22: 57, 48: 67, 61: 83, 81: 98}
        old_value = current_value
        current_value = current_value + dice
        if current_value > 100:
            print(player+" Maximum value is 100. So, not moved "+str(old_value))
            return old_value
        print(player+" moved from "+str(old_value)+" to "+str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            print( player + " got a snake bite!! down from " + str(current_value) + " to " + str(final_value))
        elif current_value in ladders:
            final_value = ladders.get(current_value)
            print( player + " climbed the ladder from " + str(current_value) + " to " + str(final_value))
        else :
            final_value = current_value
        return final_value
    def check_win(self,player, position):
        if position == 100:
            print("Congratulations!!! "+player+" you won")
            sys.exit(1)

object = Game()
print("Enter How many players are playing?\n1.One players 2.Two players 3.Three players")
n = int(input())
if n == 1:
    player1_name = object.get_player_name()
    player1_current_position = 0

    while True:
        print("\n"+player1_name + " rolling die")
        dice1 = object.get_dice_value()
        player1_current_position = object.snake_ladder(player1_name, player1_current_position, dice1)
        object.check_win(player1_name, player1_current_position)

elif n == 2:
    player1_name = object.get_player_name()
    player2_name = object.get_player_name()
    player1_current_position = 0
    player2_current_position = 0

    while True:
        print("\n"+player1_name + " rolling die")
        dice1 = object.get_dice_value()
        player1_current_position = object.snake_ladder(player1_name, player1_current_position, dice1)
        object.check_win(player1_name, player1_current_position)
        print("\n"+player2_name + " rolling die")
        dice2 = object.get_dice_value()
        player2_current_position = object.snake_ladder(player2_name, player2_current_position, dice2)
        object.check_win(player2_name, player2_current_position)

elif n == 3:
    player1_name = object.get_player_name()
    player2_name = object.get_player_name()
    player3_name = object.get_player_name()
    player1_current_position = 0
    player2_current_position = 0
    player3_current_position = 0

    while True:
        print("\n"+player1_name + " rolling die")
        dice1 = object.get_dice_value()
        player1_current_position = object.snake_ladder(player1_name, player1_current_position, dice1)
        object.check_win(player1_name, player1_current_position)
        print("\n"+player2_name + " rolling die")
        dice2 = object.get_dice_value()
        player2_current_position = object.snake_ladder(player2_name, player2_current_position, dice2)
        object.check_win(player2_name, player2_current_position)
        print("\n"+player3_name + " rolling die")
        dice3 = object.get_dice_value()
        player3_current_position = object.snake_ladder(player3_name, player3_current_position, dice3)
        object.check_win(player3_name, player3_current_position)

else :
    print("Enter a valid key!!")
