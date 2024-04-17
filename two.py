import re
import sys
def parse_match_data(input_string):
    match_id = input_string.split()[0]
    team_data = re.findall(r'(\d+)\((\d+)(p|o)\)', input_string)
    teams_partner = {}
    teams_opponent = {}
    for team, match, role in team_data:
        team = int(team)
        match = int(match)
        if role == 'p':
            if team not in teams_partner or teams_partner[team][0] < match:
                teams_partner[team] = (match, 1 if team not in teams_partner else teams_partner[team][1] + 1)
            else:
                teams_partner[team] = (teams_partner[team][0], teams_partner[team][1] + 1)
        elif role == 'o':
            if team not in teams_opponent or teams_opponent[team][0] < match:
                teams_opponent[team] = (match, 1 if team not in teams_opponent else teams_opponent[team][1] + 1)
            else:
                teams_opponent[team] = (teams_opponent[team][0], teams_opponent[team][1] + 1)
    combined_data = []
    all_teams = set(teams_partner.keys()).union(set(teams_opponent.keys()))
    for team in all_teams:
        last_partner_match = teams_partner.get(team, (0, 0))
        last_opponent_match = teams_opponent.get(team, (0, 0))
        combined_data.append((last_partner_match[0], last_opponent_match[0], last_partner_match[1], last_opponent_match[1], team))
    combined_data.sort(reverse=True, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
    sorted_teams = [data[4] for data in combined_data][::-1]
    return sorted_teams
#input_str = "qm1 2607(34p) 4573(51p)(92o) 3142(27p) 1257 321 1640(84p)"
sys.stdin = open('in', 'r')
output2 = []
go = True
while go:
    input_str = input()
    if input_str == 'END':
        go = False
        break
    output = parse_match_data(input_str)
    print(output)
    output2.append(output)
sys.stdout = open('out.csv', 'a')
print('qm q1 q2 d1 d2 d3 d4')
for i in range(len(output2)):
    print(i+1, *output2[i])
