class GameBoard():
    
    nums = [1,2,3,4,5,6,7,8,9]
    
    def __init__ (self, num):
        self.num = num
    
    def print_game_board(self, num):
        num = 0
        print("-" * 15)
        #nums = [1,2,3,4,5,6,7,8,9]
        i = 0
        for x in range(3):
            print("| " + str(self.nums[i]) + " |" + "| " + str(self.nums[i]) + " |" "| " + str(self.nums[i]) + " |" )
            print("-" * 15)
            i += 2
    
    def append_choice(self, choice):
        if choice >= 1 and choice <= 9:
            self.nums.insert(choice, 'X')
        else: 
            print("Nope")
        self.print_game_board(0)
        
            
game = GameBoard(0)
game.print_game_board(0)

print("Let's play a game. Please enter your choice")
choice = int(input())
game.append_choice(choice)
