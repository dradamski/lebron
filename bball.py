import csv
import matplotlib.pyplot as plt

with open('bball.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    year_list = []
    for row in reader:
        year_list.append(row[2][:4])
    del(year_list[0:2])

    #Creates dictionary of years and number of 25-5-5 players
    lebron_dict = {}
    for year in year_list:
        if year in lebron_dict:
            lebron_dict[year] += 1
        else:
            lebron_dict[year] = 1
    


with open('teams.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    poss_dic = {}
    year = []
    fga = []
    to = []
    for row in reader:
        if row[20] != '':
            year.append(row[1][:4])
            to.append(row[20])
            fga.append(row[9])
            
    del(fga[0:2])
    del(to[0:2])
    del(year[0:2])
    
    for i in range(len(fga)):
        poss_dic[year[i]] =(float(fga[i]) + float(to[i]))

        


# graph of possessions over time
lists = sorted(poss_dic.items())
x, y = zip(*lists)

#plt.scatter(x,y)
#plt.title('Average Possessions per Game vs Year')
#plt.show()

# graph of 'Lebrons' over time
#lists = sorted(lebron_dict.items())
#x, y = zip(*lists)
#plt.scatter(x,y)
#plt.show()


# graph "Lebrons" as a function of possessions
poss_list = []
lebron_list = []
final_dic = {}

for key in lebron_dict.keys():
    if key not in poss_dic.keys():
        continue
    else:
        poss_list.append(poss_dic[key])
        lebron_list.append(lebron_dict[key])


#plt.scatter(poss_list, lebron_list)
#plt.title('Lebrons in a year based on avg possessions')
#plt.show()

player_list = sorted(players, key = players.get, reverse = True)


    #for player in player_list:
        #temp = player.split('\\')
        #print('%s: %s' % (temp[0], str(players[player])))           
        
        
                
     
        
        
        
