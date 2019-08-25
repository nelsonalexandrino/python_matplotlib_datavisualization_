import matplotlib.pyplot as pyplot

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]

xAxis = []
for i in range(len(HomeTeamGoals)):
    xAxis.append(i)

pyplot.xlim(0, 145)
pyplot.ylim(0, 6)
pyplot.plot(xAxis, AwayTeamGoals, c='red')
pyplot.show(block=False)
pyplot.plot(xAxis, HomeTeamGoals, c='blue')
pyplot.show(block=False)
