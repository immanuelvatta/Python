class Player:
    # def __init__(self, name, age, position, team):
    #! updated constructor 
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    #TODO Add an @class method called get_team(cls, team_list) that, 
    #TODO given a list of dictionaries populates and returns a new list of Player objects. 
    #TODO Be sure to test your method!
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for dict in team_list:
            new_team.append(Player(dict))
        return new_team

    def displayPlayer(self):
        print(f"Name: {self.name}, Age: {self.age} Position: {self.position}, Team: {self.team}")
        return self
#players = [
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    }

jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    }
kyrie = {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    }
damian = {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    }
joel = {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    }
demar = {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
#]

# player_kevin = Player(players[0]["name"], players[0]["age"], players[0]["position"],players[0]["team"])
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)
player_demar = Player(demar)

# player_kevin.displayPlayer()
# player_jason.displayPlayer()
# player_kyrie.displayPlayer()
# player_joel.displayPlayer()
# player_demar.displayPlayer()


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team = []

for dict in players:
    player = Player(dict)
    new_team.append(player)


#! to print the actual players (you need another for loop and call the displayPlayer) (to get not the memory location)
for player in new_team:
    player.displayPlayer()

#* displaying get_team method
new_team1 = Player.get_team(players)
for player in new_team1:
    player.displayPlayer()
