import csv
import matplotlib.pyplot as plt
#  GETS LIST OF PLAYERS WITH "LEBRONS" AND ORDERS THEM
players = {}
position = {}
heights = {}
years = {}

with open('lebrongames.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    
# ['Rk', 'Player', 'Age', 'Pos', 'Date', 'Tm', '', 'Opp', '',
#  'GS', 'MP', 'FG', 'FGA', 'FG%', '2P', '2PA', '2P%', '3P', 
#  '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
#  'STL', 'BLK', 'TOV', 'PF', 'PTS', 'GmSc']        
    for row in reader:
        
        if row[3] not in position.keys():
            position[row[3]] = 1
        else:
            position[row[3]] += 1
        
        date = row[4][:4]
        if date not in years.keys():
            years[date] = 1
        else:
            years[date] += 1
        
        name = row[1].split('\\')[0]
        if name not in players.keys():
            players[name] = 1
        else:
            players[name] += 1
        
        
    del(years['Date'])
    del(players['Player'])
    del(position['Pos'])
    print(years)           
    print(players)
    print(position)
    
#   CREATES HISTOGRAM SHOWING NUMBER OF PLAYERS WITH A CERTAIN AMOUNT OF LEBRONS    
    hist = []
    for p in players:
        hist.append(int(players[p]))
    
    #plt.hist(hist, bins=20)
    #plt.title('"Amount of players with Lebrons"')
    #plt.show()
#plt.scatter(


