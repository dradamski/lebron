import pandas as pd
lebron_df= pd.DataFrame.from_csv('lebrongames.csv')
avg_df = pd.DataFrame.from_csv('teams.csv')

players = {}
position = {}
years = {}
for i, row in lebron_df.iterrows():
    name = row['Player'].split('\\')[0]
    year = row['Date'][:4]
    pos = row['Pos']
    if pos not in position.keys():
        position[pos] = 1
    else:
        position[pos] += 1

   
    if year not in years.keys():
        years[year] = 1
    else:
        years[year] += 1

    if name not in players.keys():
        players[name] = 1
    else:
        players[name] += 1
        
        
lists = sorted(years.items())
x, y = zip(*lists)
plt.plot(x,y)