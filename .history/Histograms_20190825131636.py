import matplotlib.pyplot as pyplot

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]


total_goals = HomeTeamGoals + AwayTeamGoals
pyplot.figure(figsize=(8, 5))
pyplot.hist(x=(HomeTeamGoals, AwayTeamGoals, total_goals), bins=range(8),
            label=['Home team gols', 'Away team gols', 'Total goals scored'], align='left')
pyplot.legend()
pyplot.xlabel('Goals scored')
pyplot.ylabel('Number of goals scored')
pyplot.show()

pyplot.figure(figsize=(8, 5))
pyplot.hist2d(x=HomeTeamGoals, y=AwayTeamGoals, bins=(range(8), range(7)))
pyplot.xlabel('Home team goals')
pyplot.ylabel('Away team goals')
pyplot.show()
