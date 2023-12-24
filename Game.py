import os
from Board import Board
from Menu import Menu
from Player import Player

def clear_screen():# to clear terminal when i want
    os.system("cls" if os.name=="nt" else "clear")
    
class Game:
    def __init__(self) :
        self.board=Board()
        self.menu=Menu()
        self.players=[Player(),Player()]
        self.current_player_index=0
    
    def start_game(self):
        choice=self.menu.start_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
            
    def swich_player(self):
        self.current_player_index = 1-self.current_player_index
        
    def play_turn(self):
        player=self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.getName()} with symbol {player.getSymbol()}")
        while True:
            try:
                choice=int(input("Enter your choice : "))
                if 1<=choice<=9 and self.board.updata_board(choice,player.getSymbol()):
                    self.board.updata_board(choice,player.getSymbol())
                    print("updata")
                    break
                else:
                    print("invalld move!!!")
                
            except ValueError:
                print("please enter number bettween 1-9 !!")
        
        self.swich_player()
 
    def check_win(self):
        win_cases=[[0,1,2],[3,4,5],[6,7,8],
                   [0,3,6],[1,4,7],[2,5,8],
                   [0,4,8],[2,4,6]]
        for comb in win_cases:
            if self.board.board[comb[0]]==self.board.board[comb[1]]==self.board.board[comb[2]]:
                return True
        return False
    
    def check_drow(self):
        return all(not cell.isdigit() for cell in self.board.get_board())# by list comprehinshin ==> 
        # for cell in self.board.get_board():
        #     if cell.isNotBusy():
        #         return False
            
        # return True
    
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.start_game()
    
    # def quit_game(self):
    #     pass
    
    def setup_players(self):
        self.players[0].choose_name()
        self.players[0].choose_symbol()
        clear_screen()
        while True:
            self.players[1].choose_name()
                
            if self.players[0].getName() != self.players[1].getName():
                break
            else:
                print("Please enter another name!!!")
                

        if self.players[0].getSymbol() == "X":
            print(f"{self.players[1].getName()} your symbol is O by defult ")
            self.players[1].setsymbol("O")
        else:
            print(f"{self.players[1].getName()} your symbol is X by defult ")
            self.players[1].setsymbol("X")
            
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_drow():
                choice=self.menu.end_menu()
                if choice =="1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
                
    
    def quit_game(self):
        print("thank you for Playing ❤")
    
# =========================== test ======================
game=Game()
game.start_game()
