class football:
    def __init__(self,name,club) -> None:
        self.name=name
        self.club=club
    def clubname(self):
        print(f"this player {self.name} is belong to {self.club}")
p1=football("lewandowsiki","barcelona")
p1.clubname()