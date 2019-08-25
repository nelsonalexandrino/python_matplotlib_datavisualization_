import matplotlib.pyplot as pyplot

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]

xAxis = []
for i in range(len(HomeTeamGoals)):
    xAxis.append(i)

#pyplot.plot(xAxis, AwayTeamGoals, c='red')
pyplot.scatter(xAxis, AwayTeamGoals, c='red', s=5)
pyplot.title(r'My first plot graph in Python $\frac{20}{19}$')
pyplot.scatter(xAxis, HomeTeamGoals, c='blue', s=5)
pyplot.xlim(0, 145)
pyplot.ylim(-0.5, 6)
pyplot.xlabel('Game number')
pyplot.ylabel('Goals scored')
pyplot.show()
