import pandas as pd
import teamProfiles as Tp
import random as rd
import match as m
import validity as v
import selection as s

print('---------- WELCOME TO THE T20 WORLD CUP 2021 ----------')
print()
print('-- Group A --')
for i in Tp.GroupA:
    print(i, end=", ")
print()
print()
print('-- Group B --')
for i in Tp.GroupB:
    print(i, end=", ")
print()
print()

# Selecting the group
userGroup = v.valid('Select a group.\nEnter\n1 for group A\n2 for Group B\n', 2)

# selecting Team


def displaying_team(user_group):
    if user_group == 1:
        print('Select a Team')
        print('Enter')
        counter = 1
        for w in Tp.GroupA:
            print(counter, 'for', w)
            counter += 1
    elif user_group == 2:
        print('Select a Team.')
        print('Enter')
        counter = 1
        for j in Tp.GroupB:
            print(counter, 'for', j)
            counter += 1


displaying_team(userGroup)
userTeam = input()

while userTeam != '1' and userTeam != '2' and userTeam != '3' and userTeam != '4':
    print('Enter a valid Input!')
    displaying_team(userGroup)
    userTeam = input()
userTeam = int(userTeam)

u_Team_name = s.selecting_team_name(userGroup, userTeam)
print('Team', u_Team_name)
uTeam = s.selecting_team(userGroup, userTeam)
print(uTeam)
print()

# Editing Team/player information
editT1 = v.valid('Do you want to edit the Team/players?\nEnter\n1 for Yes\n2 for no\n', 2)
if editT1 == 1:
    done = False
    while not done:
        editT2 = v.valid('Do you want to add/remove/edit player?\nEnter\n1 for Add player\n2 for remove player\n3 for '
                         'edit player\n', 3)
        if int(editT2) == 1:
            valid1 = False
            while not valid1:
                try:
                    c = int(input('Enter the cap number of the player.\n'))
                    valid1 = True
                except ValueError:
                    print('Enter a valid Input!')
            n = input('Enter the name of the player.\n')
            uTeam.loc[len(uTeam.index)] = [c, n]
            print(uTeam)
            print()
        elif int(editT2) == 2:
            r = v.valid('Enter the index of the player you want to remove.\n', 11)
            uTeam = uTeam.drop([uTeam.index[r]])
            print(uTeam)
            print()
        elif int(editT2) == 3:
            editT3 = v.valid('Enter the index of the player you want to edit.\n', 11)
            editT4 = v.valid('Enter\n1 for edit player cap number\n2 for edit player name\n', 2)
            if editT4 == 1:
                valid4 = False
                while not valid4:
                    try:
                        C = int(input('Enter the cap number.\n'))
                        valid4 = True
                    except ValueError:
                        print('Enter a valid Input!')
                uTeam.loc[int(editT3), 'Cap'] = C
                print(uTeam)
                print()
            elif editT4 == 2:
                N = input('Enter the name.\n')
                uTeam.loc[int(editT3), 'Name'] = N
                print(uTeam)
                print()
        edit = v.valid('Are you done with editing Team/Players?\nEnter\n1 for Yes\n2 for No\n', 2)
        if edit == 1:
            done = True
        else:
            done = False

# Selecting the other Team
print('- You will be competing with', end=' ')
pTeamNo = rd.randint(1, 4)
while pTeamNo == userTeam:
    pTeamNo = rd.randint(1, 4)

p_Team_name = s.selecting_team_name(userGroup, pTeamNo)
print('Team', p_Team_name, '-')
pTeam = s.selecting_team(userGroup, pTeamNo)
print(pTeam)
print()

# Toss
uToss = v.valid("For the Toss\nEnter\n1 for Head\n2 for Tail\n", 2)
pToss = rd.randint(1, 2)

if uToss == pToss:
    u_select = v.valid('You won!\nDo you want to bat first or bowl first?\nEnter\n1 for Batting\n2 for Bowling\n', 2)
else:
    print('You loss!\nYou will bowl first.')
    print()
    u_select = 2

if u_select == 1:
    bowling_t_name = p_Team_name
    batting_t_name = u_Team_name
    batting_Team = uTeam
    bowling_Team = pTeam
else:
    bowling_t_name = u_Team_name
    batting_t_name = p_Team_name
    batting_Team = pTeam
    bowling_Team = uTeam

# 1st inning
print('--- The First Inning Starts! ---')
print()
f_inning = m.match(bowling_t_name, bowling_Team, batting_t_name, batting_Team, 10000)
print('Team', batting_t_name)
print(f_inning[0])
print()
print('Team', bowling_t_name)
print(f_inning[1])
print()
score = f_inning[2]


def convert(lst):
    res_dct = {lst[k]: 0 for k in range(len(lst))}
    return res_dct


groupA_dct = convert(Tp.GroupA)
groupB_dct = convert(Tp.GroupB)


def score_assigning(a):
    if userGroup == 1:
        if u_select == a:
            groupA_dct[u_Team_name] = score
        else:
            groupA_dct[p_Team_name] = score
    else:
        if u_select == a:
            groupB_dct[u_Team_name] = score
        else:
            groupB_dct[p_Team_name] = score


score_assigning(1)

# 2nd inning
if u_select == 1:
    batting_t_name = p_Team_name
    bowling_t_name = u_Team_name
    batting_Team = pTeam
    bowling_Team = uTeam
else:
    batting_t_name = u_Team_name
    bowling_t_name = p_Team_name
    batting_Team = uTeam
    bowling_Team = pTeam

print('--- The Second Inning Starts! ---')
print()
p_score = f_inning[2]
s_inning = m.match(bowling_t_name, bowling_Team, batting_t_name, batting_Team, p_score)
print('Team', batting_t_name)
print(s_inning[0])
print()
print('Team', bowling_t_name)
print(s_inning[1])
print()
score = s_inning[2]
score_assigning(2)

# winner selecting
winner_score = max(f_inning[2], s_inning[2]) - min(f_inning[2], s_inning[2])

if f_inning[2] > s_inning[2]:
    winner = f_inning[3]
    looser = s_inning[3]
else:
    winner = s_inning[3]
    looser = f_inning[3]

print('!!!!!!', winner, 'BEATS', looser, 'BY', winner_score, 'RUNS !!!!!!')
print()

# match summary
print('--- Match Summary ---')
print()
if pToss == uToss:
    if u_select == 1:
        print(u_Team_name, 'WON THE TOSS AND CHOSE TO BAT')
    else:
        print(u_Team_name, 'WON THE TOSS AND CHOSE TO BOWL')
else:
    print(p_Team_name, 'WON THE TOSS AND CHOSE TO BAT')
print()

print('Team', f_inning[3])
print('Score -', f_inning[2])
print('Overs -', f_inning[5])
print('Wickets -', f_inning[6])
print()
print('Team', s_inning[3])
print('Score -', s_inning[2])
print('Overs -', s_inning[5])
print('Wickets -', s_inning[6])
print()

# Top 5 Batsmen and Bowlers
print('- Top 5 Batsmen -')
hs = m.h_scores.sort_values('Runs', ascending=False)
print(hs.head(5))
print()
print('- Top 5 Bowlers -')
hw = m.all_wickets.sort_values('Wickets', ascending=False)
print(hw.head(5))
print()

# Tournament standings
print('- Tournament standings - ')
print()
groupA = pd.DataFrame()
groupB = pd.DataFrame()

for key in groupA_dct:
    groupA = groupA.append({'Team': key, 'Score': groupA_dct[key]}, ignore_index=True)
for key in groupB_dct:
    groupB = groupB.append({'Team': key, 'Score': groupB_dct[key]}, ignore_index=True)
t_standingsA = groupA.sort_values('Score', ascending=False)
t_standingsB = groupB.sort_values('Score', ascending=False)
print('Group A')
print(t_standingsA)
print()
print('Group B')
print(t_standingsB)

# match information
dic = {'Team 1': f_inning[3], 'Team 1 Score': f_inning[2], 'Team 2': s_inning[3],
       'Team 2 Score': s_inning[2], 'Winner': winner, }
match_info = open('Match Info.txt', 'a')
for key in dic:
    match_info.write(key)
    match_info.write(' - ')
    match_info.write(str(dic[key]))
    match_info.write('\n')
match_info.write('\n')
match_info.close()
