import matplotlib.pyplot as pyplot

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]


pyplot.hist2d(x=HomeTeamGoals, y=AwayTeamGoals, bins=(range(8), range(7)))
pyplot.figure(figsize=(8, 5))
pyplot.xlabel('Home team goals')
pyplot.ylabel('Away team goals')
pyplot.colorbar()
pyplot.show()
