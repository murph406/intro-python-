'''>>> ws = WorldSeries('Boston Red Sox', 'New York Yankees', p=.73)
>>> # story=True says print out results of each game and the series winner
>>> bostonWins = ws.simulate(story=True)  
Game 1: Boston Red Sox win (Boston 1 games: New York 0 games)
Game 2: Boston Red Sox win (Boston 2 games: New York 0 games)
Game 3: New York Yankees win (Boston 2 games: New York 1 games)
Game 4: Boston Red Sox win (Boston 3 games: New York 1 games)
Game 5: Boston Red Sox win (Boston 4 games: New York 1 games)
Boston Red Sox win the series!
>>> bostonWins
True
>>> # without story (using the default of story=False, it just returns if team1 won
>>> ws.simulate() 
True
>>> if ws.simulate():
        print(ws.team1, "won!")
else:
        print(ws.team2), "won!")
    win = random.random() < p

New York Yankees won!'''

class WorldSeries(object):
    def __init__(self, team1,team2, p=.5):
        self.team1 =
        self.team2 = 
        self.p = p
    
    def simulte(self, story = False):
        
        return random.random() < self.p
