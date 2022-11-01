# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
# # Pass in all the values from the dictionary by their keys
# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
# print(player_kevin.position) # prints small forward

class Player:

    all_players = []

    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]
        Player.all_players.append(self)

    @classmethod
    def print_all_players(cls):
        for players in cls.all_players:
            print(f"Name: {players.name}, age: {players.age}, position: {players.position}, team: {players.team}" )

    @classmethod
    def get_team(cls, team_list):
        new_team = [0]*len(team_list)
        for i in range(len(team_list)):
            new_team[i] = Player(team_list[i])
        return new_team

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

player_jason = Player(players[1])
player_demar = Player(players[5])
player_joel = Player(players[4])

new_team = [0]*len(players)
for i in range (len(players)):
    new_team[i] = Player(players[i])

# for i in range (len(players_info)):
#     print(players[i])

# Player.print_all_players()

new_new_team = Player.get_team(players)
# for i in range (len(new_new_team)):
#     print(new_new_team[i])