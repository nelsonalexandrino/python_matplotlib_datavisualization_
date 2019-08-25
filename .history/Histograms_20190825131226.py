import matplotlib.pyplot as pyplot
import numpy as np

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]


x = np.arange(20)
y = np.arange(20)
data = x[:, None]+y[None, :]

X, Y = np.meshgrid(x, y)
vmin = 0
vmax = 15

# My attempt
fig, ax = pyplot.subplots()
contourf_ = ax.contourf(X, Y, data, 400, vmin=vmin, vmax=vmax)

total_goals = HomeTeamGoals + AwayTeamGoals
pyplot.figure(figsize=(8, 5))
pyplot.hist(x=(HomeTeamGoals, AwayTeamGoals, total_goals), bins=range(8),
            label=['Home team gols', 'Away team gols', 'Total goals scored'], align='left')
pyplot.legend()
pyplot.xlabel('Goals scored')
pyplot.ylabel('Number of goals scored')
pyplot.show()

pyplot.hist2d(x=HomeTeamGoals, y=AwayTeamGoals, bins=(range(8), range(7)))
pyplot.figure(figsize=(8, 5))

pyplot.xlabel('Home team goals')
pyplot.ylabel('Away team goals')
//pyplot.colorbar(contourf_)
pyplot.show()
