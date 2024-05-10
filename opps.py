class Madrid:
    def __init__(self,player,number) -> None:
       self.player=player
       self.number=number
    def details(self):
        print(f"the player name is  {self.player}")
        print(f"the jercy number  is  {self.number}")
    def ucl(self):
        print("valid to play ucl..")
    def pl(self):
        print("not enough to enter ucl..")

player1=Madrid("Kylian_mbappe",7)
player2=Madrid("Haaland",9)

player1.details()
player1.ucl()
player2.details()
player2.pl()