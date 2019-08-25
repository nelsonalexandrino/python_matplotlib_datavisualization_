import matplotlib.pyplot as pyplot

x = []
y = []

for i in range(-10000, 10000):
    x.append(i/100)
    y.append(i/100)

pyplot.plot(x, y)
pyplot.xscale('linear')
pyplot.yscale('linear')
pyplot.show()
