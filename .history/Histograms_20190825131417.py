import matplotlib.pyplot as pyplot

with open("Goals.txt", "r") as f:
    HomeTeamGoals = [int(x)
                     for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [int(x)
                     for x in f.readline().strip("\n").strip(" ").split(" ")]

TotalGoals = HomeTeamGoals + AwayTeamGoals
pyplot.figure(figsize=(8, 5))
pyplot.hist(x=(HomeTeamGoals, AwayTeamGoals, TotalGoals),
            bins=range(8),
            label=["Home Team Goals", "Away Team Goals",
                   "Total Goals Scored"],
            align="left")
pyplot.legend()
pyplot.xlabel("Goals Scored")
pyplot.ylabel("Number of goals scored")
pyplot.show()

pyplot.figure(figsize=(8, 5))
pyplot.hist2d(x=HomeTeamGoals,
              y=AwayTeamGoals,
              bins=(range(8), range(7)))
pyplot.xlabel("Home Team Goals")
pyplot.ylabel("Away Team Goals")
pyplot.colorbar()
pyplot.show()
