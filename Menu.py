class Menu:
    def start_menu(self):
        print("welcome to my X-O game")
        while True:
            print("1- start Game .  ")
            print("2- quit Game . : ")
            choose=input("choose 1 or 2 number : ")
            if self.isVallid_choice(choose):
                return choose
            print("invalld choose please enter true number!!!")
            
    def end_menu(self):
         while True:
            print("second menu!!!!")
            print("1- restart Game .  ")
            print("2- quit Game . : ")
            choose=input("choose 1 or 2 number : ")
            if self.isVallid_choice(choose):
                return choose
            print("invalld choose please enter true number!!!")
            
    def isVallid_choice(self,choose):
        if choose == "1" or choose == "2":
            return True
        else:
            return False
        
#========================== check the class ================================
# menu1=Menu()
# menu1.start_menu()
# menu1.end_menu()
