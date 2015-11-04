import sqlite3

def getValues(fileName):
    """Gets values from CSV and returns in list"""
    dataFile = open(fileName)
    lines = dataFile.readlines()
    dataLineValues = []
    for line in lines:
        dataLineValues.append([x.strip('"\n') for x in line.split(',')])
    return dataLineValues

def insertTeamRows(curs, fileName):
    try:
        csvLines = getValues(fileName)
        header = csvLines[0]
        dataLines = csvLines[1:]
        values = [tuple(x) for x in dataLines]
        c.executemany(
                      "insert or replace into team values(?, ?, ?)",
                      values
                      )
        conn.commit()
        print("Succeeded in inserting {}".format(fileName))
    except:
        print("Errored while inserting {}".format(fileName))

def insertTeamStatsRows(curs, fileName):
    try:
        csvLines = getValues(fileName)
        header = csvLines[0]
        dataLines = csvLines[1:]
        values = [tuple(x) for x in dataLines]
        c.executemany(
                      """insert or replace into team_game_stats
                      values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                             ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                             ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                             ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                             ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                             ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                             ?, ?, ?, ?, ?, ?, ?, ?)""",
                      values
                      )
        conn.commit()
        print("Succeeded in inserting {}".format(fileName))
    except Exception as e:
        print("Errored while inserting {}".format(fileName))
        print(e)

def insertGameRows(curs, fileName):
    try:
        csvLines = getValues(fileName)
        header = csvLines[0]
        dataLines = csvLines[1:]
        values = [tuple(x) for x in dataLines]
        c.executemany(
                      """insert or replace into game
                      values(?, ?, ?, ?, ?, ?)""",
                      values
                      )
        conn.commit()
        print("Succeeded in inserting {}".format(fileName))
    except Exception as e:
        print("Errored while inserting {}".format(fileName))
        print(e)

if __name__ == "__main__":
    startYear = 2005
    endYear = 2014

    conn = sqlite3.connect("CFB.db")
    c = conn.cursor()

    for year in range(startYear, endYear):
        dirName = "Season" + str(year)
        teamFileName = dirName + '/team.csv'
        statsFileName = dirName + '/team-game-statistics.csv'
        gameFileName = dirName + '/game.csv'

        print "Starting inserts for {}".format(teamFileName)
        insertTeamRows(c, teamFileName)
        print "Starting inserts for {}".format(statsFileName)
        insertTeamStatsRows(c, statsFileName)
        print "Starting inserts for {}".format(gameFileName)
        insertGameRows(c, gameFileName)

    print "Completed insertions. Please verify the load was successful"

    conn.close()
