import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


batting = pd.read_csv('data/BattingPost.csv')
batting = batting[batting['yearID'] > 1980]
batting = batting[batting['yearID'] < 2020]
batting


players_per_year = batting.groupby(by = 'yearID').count()['playerID']
plt.plot(players_per_year)

hr_per_year = batting.groupby(by = 'yearID').sum()['HR']
plt.plot(hr_per_year)

hr_per_player_per_year = hr_per_year / players_per_year


# Visualization 1

plt.xlabel('year')
plt.ylabel('hr per player')
plt.plot(hr_per_player_per_year)


hr_per_team = batting.groupby(by = 'teamID').sum()['HR'].sort_values()
fig = plt.figure()
ax = fig.add_axes([0,0,3,2])
ax.bar(hr_per_team.index, hr_per_team.values)
plt.show()


salaries = pd.read_csv('data/Salaries.csv')
salaries = salaries[salaries['yearID'] > 2000]
salaries = salaries[salaries['salary'] > 0]
salaries


maxes = salaries.groupby(by = 'teamID').max()['salary']
mins = salaries.groupby(by = 'teamID').min()['salary']
means = salaries.groupby(by = 'teamID').mean()['salary'].sort_values()

diff = maxes - mins
diff = diff.sort_values()
salary_ratio = (maxes / mins).sort_values()



# Visualization 2

fig = plt.figure()
ax = fig.add_axes([0,0,3,2])
ax.bar(means.index, means.values)
plt.xlabel('Team')
plt.ylabel('Avg Salary')
plt.show()


'''
fig = plt.figure()
ax = fig.add_axes([0,0,4,2])
n= len(diff)
r = np.arange(n)
width = .5
  
plt.bar(r, list(mins.values), color = 'b', width = width, edgecolor = 'black', label='mins')
plt.bar(r + width, list(maxes.values), color = 'g', width = width, edgecolor = 'black', label='maxes')
  
plt.xlabel("Year")
plt.ylabel("salary")
plt.title("Anual Team Salaries")
  
# plt.grid(linestyle='--')
plt.xticks(r + width/2, mins.index)
plt.legend()
  
plt.show()
'''
