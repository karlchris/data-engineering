# Object Relationship

## Interaction between class objects

While inheritance represents a relationship between classes, there are situations where there are relationships between objects.

Now we have to use different class objects to create the design of an application. This means that independent class objects will have to find a way to interact with each other.

![ilustration object relationship](../icons/object-relationship-ilustration.png)

## Challenge

- Follow on **Task: Implementing Sports team** and its solution

=== "Task"

    ```python
    """
        Implementing Sports team

        You have to implement 3 classes, School, Team, and Player, such that an instance of a School should contain instances of Team objects.
        Similarly, a Team object can contain instances of Player class.

        You have to implement a School class containing a list of Team objects and a Team class comprising a list of Player objects.

        Task 1
            The Player class should have three properties that will be set using an initializer:
                ID
                name
                teamName

        Task 2
            The Team class will have two properties that will be set using an initializer:
                name
                players: a list with player class objects in it

            It will have two methods:
                addPlayer(), which will add new player objects in the players list
                getNumberOfPlayers(), which will return the total number of players in the players list

        Task 3
            The School class will contain two properties that will be set using an initializer:
                teams, a list of team class objects
                name

            It will have two methods:
                addTeam, which will add new team objects in the teams list
                getTotalPlayersInSchool(), which will count the total players in all of the teams in the School and return the count
    """

    # Player class
    class Player:
        pass
        # Complete the implementation


    # Team class contains a list of Player
    # Objects
    class Team:
        pass

        # Complete the implementation


    # School class contains a list of Team
    # objects.
    class School:
        pass


    # Complete the implementation
    ```

=== "Solution"

    ```python
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
    ```
