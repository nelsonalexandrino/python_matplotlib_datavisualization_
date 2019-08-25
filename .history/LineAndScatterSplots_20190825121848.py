import matplotlib.pyplot as pyplot

with open('Goals.txt', 'r') as file:
    HomeTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]
    AwayTeamGoals = [int(x) for x in file.readline().strip(
        '\n').strip(' ').split(' ')]

xAxis = []
ticks = ['Game one', 'Game fifty', 'Game 100']
for i in range(len(HomeTeamGoals)):
    xAxis.append(i)

#pyplot.scatter(xAxis, AwayTeamGoals, c='red', s=5)
pyplot.plot(xAxis, AwayTeamGoals, c='red', ls='--')
pyplot.title(r'My first plot graph in Python $\frac{20}{19}$')
pyplot.plot(xAxis, HomeTeamGoals, c='blue', ls=':')


pyplot.xlim(0, 145)
pyplot.ylim(-0.5, 6)
pyplot.xlabel('Game number')
pyplot.ylabel('Goals scored')
pyplot.xticks([0, 49, 99, 120], ticks, rotation=45)
pyplot.yticks([3], ['Three Goals'], rotation=90)
pyplot.text(50, 4, 'Beautiful graphs', fontsize=2)
pyplot.show()
