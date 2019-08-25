import matplotlib.pyplot as pyplot

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]


pyplot.figure(figsize=(8, 5))
pyplot.hist(HomeTeamGoals, bins=range(8),
            label='Home team gols')
pyplot.legend()
pyplot.show()
