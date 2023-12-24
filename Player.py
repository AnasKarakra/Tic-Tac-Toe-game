class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):# i need the name just be an alpabalticl letter
        while True:
            name=input("Enter your name : ")
            if name.isalpha():
                self.name=name
                break
            print("Invallid name, please enter alpahbatical name: ")
    
    def choose_symbol(self):
       while True:
           symbol=input("choose X or O : ")
           if symbol=="x" or symbol=="X" or symbol=="o" or symbol=="O":
               self.symbol=symbol.upper()
               break
           print("invalld character !!! :")
           
    def getSymbol(self):
        return self.symbol
    
    def getName(self):
        return self.name
    
    def setsymbol(self,symbol):
        self.symbol=symbol
           
#======================== check if the class run corrcltly =================================
# player1=Player()
# player1.choose_name()
# player1.choose_symbol()