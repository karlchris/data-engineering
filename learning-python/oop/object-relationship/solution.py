""" Solution 1: Implementing Sports team """

class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def getNumberOfPlayers(self):
        return len(self.players)

    def addPlayer(self, player):
        self.players.append(player)


class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
        return length


p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)

print("Total players in mySchool:", mySchool.getTotalPlayersInSchool())
