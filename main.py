import random

class Human:
    def __init__(self,name):
        self.name = name

class FootBallClub:
    capacity = 11
    def __init__(self,name):
        self.name = name
        self.players = []

    def getClubName(self):
        return self.name


class FootBallPlayer(Human):
    def __init__(self,name):
        super().__init__(name)
        self.club = None


clubA = FootBallClub('A')
clubB = FootBallClub('B')


names = ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی", "امین", "سعید",
         "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]

players = []
for name in names:
    player = FootBallPlayer(name)
    players.append(player)

for player in players:
    selectedClub = random.choice([clubA,clubB])
    if selectedClub == clubA and clubA.capacity <= 0:
        selectedClub = clubB
    if selectedClub == clubB and clubB.capacity <= 0:
        selectedClub = clubA
    player.club = selectedClub
    selectedClub.players.append(player)
    selectedClub.capacity -= 1

for player in players:
    print(f"{player.name} is in team {player.club.getClubName()}")
