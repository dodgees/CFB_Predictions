import sqlite3

csvStatsRowCount = 0
csvGameRowCount = 0
dbStatsRowCount = 0
dbGameRowCount = 0

startYear = 2005
endYear = 2014

for year in range(startYear, endYear):
    dirName = 'Season' + str(year)
    statFileName = dirName + '/team-game-statistics.csv'
    gameFileName = dirName + '/game.csv'

    csvStatsLines = open(statFileName)
    csvStatsRowCount += len(csvStatsLines.readlines()) - 1

    csvGameLines = open(gameFileName)
    csvGameRowCount += len(csvGameLines.readlines()) - 1

conn = sqlite3.connect('CFB.db')
c = conn.cursor()

c.execute("select count(*) from team_game_stats;")
dbStatsRowCount = c.fetchone()

c.execute("select count(*) from game;")
dbGameRowCount = c.fetchone()

print("The Stats csv file had {} records".format(csvStatsRowCount))
print("The Stats db table had {} records".format(dbStatsRowCount))
print("The Game csv file had {} records".format(csvGameRowCount))
print("The Game db file had {} records".format(dbGameRowCount))
