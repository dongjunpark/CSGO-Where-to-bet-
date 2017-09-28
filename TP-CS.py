def game(team1, team2):
    return (team1 / (team1 + team2)) 


# ROR1 = Rate of Return 1
# ROR2 = Rate of Return 2
def match(team_name, team1_map1, team1_map2, team1_map3, team2_map1, team2_map2, team2_map3, ROR1, ROR2):

# calculates each maps' winrate of Team1
    map1_team1 = game(team1_map1, team2_map1)
    map2_team1 = game(team1_map2, team2_map2)
    map3_team1 = game(team1_map3, team2_map3)

# calculates each maps' winrate of Team2
    map1_team2 = game(team2_map1, team1_map1)
    map2_team2 = game(team2_map2, team1_map2)
    map3_team2 = game(team2_map3, team1_map3)
    
# Lose Win Win %
    LWW = (1 - map1_team1) * map2_team1 * map3_team1

# Win Lose Win %
    WLW = map1_team1 * (1 - map2_team1) * map3_team1
    
# Win Win %
    WW = map1_team1 * map2_team1

# RR = Real Return
    RR = int((ROR2 / (ROR1 + ROR2)) * 100)
    
    L = [team_name + " calculated percentage", int((LWW + WLW + WW) * 100),
         team_name + " real percentage", RR]
    
# Final winrate to win 2 maps out of 3 of the match for Team1 
    return L