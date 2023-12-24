class Board:
    def __init__(self):
        # self.board=["","","",
        #             "","","",
        #             "","",""]
        self.board=[str(i) for i in range(1,10)]
        
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("-"*5)
                
    def updata_board(self,index,symbol):
        if  self.isNotBusy(index-1):
            self.board[index-1]=symbol
            print("done")
            return True 
        else:
            print("not Done")
            return False 
        
    def reset_board(self):
       self.board=[str(i) for i in range(1,10)]
       
    def isNotBusy(self,index):
        return self.board[index].isdigit()# or do this ==> return self.board[index].isalpha()
    
    def get_board(self):
        return self.board
            
# ======================================= test class ======================================
# board=Board()
# board.display_board()
# board.updata_board(2,"x")
# board.display_board()
# board.updata_board(2,"x")
# board.display_board()
# # print(board.isNotBusy(0))
# board.reset_board()
# board.display_board()