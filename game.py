import sys

class GameBoard():
    
    nums = []
    previousChoices = []
    
    def __init__ (self):
        print("Welcome to a little game. Here's the board")
        self.nums = [[1,2,3],[4,5,6],[7,8,9]]
        self.previousChoices = []
    
    def print_game_board(self):
        print("-" * 15)
        i = 0
        for x in range(3):
            print("| " + str(self.nums[x][0]) + " |" + "| " + str(self.nums[x][1]) + " |" "| " + str(self.nums[x][2]) + " |" )
            print("-" * 15)
            i = 0
    
    def append_choice(self, choice, player):
        is_alread_chosen = choice in self.previousChoices
        if choice >= 1 and choice <= 9 and is_alread_chosen == False:
            if choice <= 3:
                row = 0
                self.nums[0][choice -1] = player
            elif choice <= 6:
                row = 1
                self.nums[1][choice -4] = player
            elif choice <= 9:
                row = 2
                self.nums[2][choice -7] = player
            self.previousChoices.append(choice)
            self.print_game_board()
            exit = self.check_win_condition(row,choice,player)
            return exit
        elif is_alread_chosen == True:
            print("That number was already chosen. Enter a different number.")
            return 0
        else: 
            print("Not a valid option, try again (type quit to exit)")
            return 0

    def check_win_condition(self, row, choice, player):
        isFull = self.check_full_board()
        if isFull == True:
            print("Looks like there's a tie. Would you like to play again? yes/no")
            exit_choice = input()
            return check_choice(exit_choice)
        elif choice == 1:
            if self.nums[row][1] == player and self.nums[row][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row+1][0] == player and self.nums[row+2][0] == player:
                print(player + "'s win!")
                print("Would you like to play again? yes/no")
                exit_choice = input() 
                return check_choice(exit_choice)
            elif self.nums[row+1][1] == player and self.nums[row+2][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice) 
            else:
                return 1
        elif choice == 2:
            if self.nums[row][0] == player and self.nums[row][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row+1][1] == player and self.nums[row+2][1] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1  
        elif choice == 3:
            if self.nums[row][1] == player and self.nums[row][0] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row+1][2] == player and self.nums[row+2][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row+1][1] == player and self.nums[row+2][0] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1
        elif choice == 4:
            if self.nums[row-1][0] == player and self.nums[row+1][0] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row][1] == player and self.nums[row][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1
        elif choice == 5:
            if self.nums[row-1][1] == player and self.nums[row+1][1] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row][0] == player and self.nums[row][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row+1][0] == player and self.nums[row-1][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row-1][0] == player and self.nums[row+1][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1
        elif choice == 6:
            if self.nums[row-1][2] == player and self.nums[row+1][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row][0] == player and self.nums[row][1] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1
        elif choice == 7:
            if self.nums[row-1][0] == player and self.nums[row-2][0] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row-1][1] == player and self.nums[row-2][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row][1] == player and self.nums[row][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1
        elif choice == 8:
            if self.nums[row-1][1] == player and self.nums[row-2][1] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row][0] == player and self.nums[row][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1
        elif choice == 9:
            if self.nums[row-1][2] == player and self.nums[row-2][2] == player:
                print(player + "'s win!") 
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row][1] == player and self.nums[row][0] == player:
                print(player + "'s win!")
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            elif self.nums[row-1][1] == player and self.nums[row-2][0] == player:
                print(player + "'s win!")
                print("Would you like to play again? yes/no")
                exit_choice = input()
                return check_choice(exit_choice)
            else:
                return 1

    def check_full_board(self):
        if len(self.previousChoices) == 9:
            result = True
        else:
            result = False
        return result
 
def check_choice(exit_choice):
    if exit_choice != 'yes' and exit_choice != 'no':
        print('Please type yes or no')
        while exit_choice != 'yes' and exit_choice != 'no':
            exit_choice = input()
            return exit_choice
    elif exit_choice == 'yes':
        return exit_choice
    elif exit_choice == 'no':
        return exit_choice

def play_game():

    game = GameBoard()
    game.print_game_board()

    choice = ""
    count = 0
    player1 = 'X'
    player2 = 'O'

    while choice != 'quit':
        if count % 2 == 0:
            print(" ========== Player X's turn! ==========")
        else:
            print(" ========== Player O's turn! ==========")
        choice = input()
        if choice == 'quit':
            return 0
        if count % 2 == 0:
            result = game.append_choice(int(choice), player1)
            if result == 'yes':
                return 1
                del game
            elif result == 'no':
                return 0
        else:
            result = game.append_choice(int(choice), player2)
            if result == 'yes':
                return 1
                del game
            elif result == 'no':
                return 0
        count += result

if __name__ == '__main__':     

    
    result = play_game()
    if result == 1:
        while result != 0:
            print("=========== Resetting the game for you ===========")
            result = play_game()
    else: 
        print('Thanks for playing, bye')
