title = '''"Team Code","Game Code","Rush Att","Rush Yard","Rush TD","Pass Att","Pass Comp","Pass Yard","Pass TD","Pass Int","Pass Conv","Kickoff Ret","Kickoff Ret Yard","Kickoff Ret TD","Punt Ret","Punt Ret Yard","Punt Ret TD","Fum Ret","Fum Ret Yard","Fum Ret TD","Int Ret","Int Ret Yard","Int Ret TD","Misc Ret","Misc Ret Yard","Misc Ret TD","Field Goal Att","Field Goal Made","Off XP Kick Att","Off XP Kick Made","Off 2XP Att","Off 2XP Made","Def 2XP Att","Def 2XP Made","Safety","Points","Punt","Punt Yard","Kickoff","Kickoff Yard","Kickoff Touchback","Kickoff Out-Of-Bounds","Kickoff Onside","Fumble","Fumble Lost","Tackle Solo","Tackle Assist","Tackle For Loss","Tackle For Loss Yard","Sack","Sack Yard","QB Hurry","Fumble Forced","Pass Broken Up","Kick/Punt Blocked","1st Down Rush","1st Down Pass","1st Down Penalty","Time Of Possession","Penalty","Penalty Yard","Third Down Att","Third Down Conv","Fourth Down Att","Fourth Down Conv","Red Zone Att","Red Zone TD","Red Zone Field Goal"'''

title = [t.strip('"') for t in title.split(',')]
columns = []
for t in title:
    t = t.lower()
    print t
    t = t.split(" ")
    columns.append('_'.join(t))

crtStmt = "CREATE TABLE team_game_stats (num "
crtStmt += ", num ".join(columns)
print crtStmt
