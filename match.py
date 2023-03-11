import random as rd
import pandas as pd

all_wickets = pd.DataFrame()
h_scores = pd.DataFrame()


def match(bowling_t_name, bowling_team, batting_t_name,  batting_team, p_score):
    global all_wickets, h_scores
    bat_team = pd.DataFrame()
    bowl_team = pd.DataFrame()
    p_score = p_score
    bowling_t_name = bowling_t_name
    batting_t_name = batting_t_name
    bowling_team = bowling_team
    batting_team = batting_team
    bowling_index = 0
    bowler = bowling_team.iloc[bowling_index]
    bowler_wickets = 0
    batting_index = 0
    batsman = batting_team.iloc[batting_index]
    batsman_score = 0
    b_overs = 0
    t_score = 0
    t_wickets = 0
    t_overs = 20
    t_balls = 120
    print('-- Team', batting_t_name, 'is batting. --')
    print(batsman['Name'], 'is batting first.')
    print()
    print('-- Team', bowling_t_name, 'is bowling. --')
    print(bowler['Name'], 'is bowling first.')
    print()

    for i in range(1, t_balls+1):
        if p_score >= t_score:
            if t_overs > 0 and t_wickets < 10:
                v = False
                while not v:
                    try:
                        u = int(input('Enter a number between 1 to 6\n'))
                        if u > 6 or u < 1:
                            raise ValueError
                        v = True
                    except ValueError:
                        print('Enter a valid Input!')
                p = rd.randint(1, 6)
                if p == u:
                    t_wickets += 1
                    if p % 3 == 0:
                        print("It's a Catch!")
                    else:
                        print("It's a Wicket!")
                    bowler_wickets += 1
                    try:
                        bat_team = bat_team.append({'Cap': int(batting_team.iloc[batting_index]['Cap']),
                                                    'Name': batting_team.iloc[batting_index]['Name'],
                                                    'Runs': int(batsman_score)}, ignore_index=True)
                        h_scores = h_scores.append({'Team': batting_t_name,
                                                    'Name': batting_team.iloc[batting_index]['Name'],
                                                    'Runs': int(batsman_score)}, ignore_index=True)
                    except IndexError:
                        pass
                    print(batsman['Name'], 'out with', batsman_score, 'scores.')
                    print()
                    batsman_score = 0
                    batting_index += 1
                    try:
                        batsman = batting_team.iloc[batting_index]
                    except IndexError:
                        pass
                    if t_wickets < 10:
                        print('-', batsman['Name'], 'is batting now. -')
                        print()
                    else:
                        print('Oll out!')
                elif p % 3 == 0 and u % 3 == 0:
                    batsman_score += 6
                    t_score += 6
                    print("It's a 6!")
                    print(batsman['Name'], 'earned 6 points.')
                elif p % 2 == 0 and u % 2 == 0:
                    batsman_score += 4
                    t_score += 4
                    print("It's a 4!")
                    print(batsman['Name'], 'earned 4 points.')
                else:
                    batsman_score += u - 1
                    t_score += u - 1
                    print(batsman['Name'], 'earned', u - 1, 'points.')

                if i % 6 == 0:
                    b_overs += 1
                    t_overs -= 1

                print('Total score is', t_score, '.')
                if (t_balls - i) % 6 == 0:
                    print(t_overs, 'overs are left.')
                else:
                    print(t_overs - 1, 'overs and', (t_balls - i) % 6, 'balls are left.')
                print(t_wickets, 'Wickets.')
                print()
                if b_overs == 4 and t_wickets <= 10:
                    try:
                        bowl_team = bowl_team.append({'Cap': int(bowling_team.iloc[bowling_index]['Cap']),
                                                      'Name': bowling_team.iloc[bowling_index]['Name'],
                                                      'Wickets': int(bowler_wickets)}, ignore_index=True)
                        all_wickets = all_wickets.append({'Team': bowling_t_name,
                                                          'Name': bowling_team.iloc[bowling_index]['Name'],
                                                          'Wickets': int(bowler_wickets)}, ignore_index=True)
                    except IndexError:
                        pass

                    bowling_index += 1
                    bowler = bowling_team.iloc[bowling_index]

                    if b_overs == 4 and t_wickets < 10:
                        print('-', bowler['Name'], 'is bowling now. -')
                        print()
                    bowler_wickets = 0
                    b_overs = 0

    if t_wickets == 10 or p_score < t_score:
        try:
            bat_team = bat_team.append({'Cap': int(batting_team.iloc[batting_index]['Cap']),
                                        'Name': batting_team.iloc[batting_index]['Name'],
                                        'Runs': int(batsman_score)}, ignore_index=True)
            h_scores = h_scores.append({'Team': batting_t_name,
                                        'Name': batting_team.iloc[batting_index]['Name'],
                                        'Runs': int(batsman_score)}, ignore_index=True)
        except IndexError:
            pass
        bowl_team = bowl_team.append({'Cap': int(bowling_team.iloc[bowling_index]['Cap']),
                                      'Name': bowling_team.iloc[bowling_index]['Name'],
                                      'Wickets': int(bowler_wickets)}, ignore_index=True)
        all_wickets = all_wickets.append({'Team': bowling_t_name,
                                          'Name': bowling_team.iloc[bowling_index]['Name'],
                                          'Wickets': int(bowler_wickets)}, ignore_index=True)

    if p_score < t_score:
        print(batting_t_name, 'Won!')
        print()
    else:
        print('Team', batting_t_name)
    print('Total score is', t_score, '.')
    if t_overs != 0:
        print(t_overs - 1, 'overs are left.')
    else:
        print(t_overs, 'overs are left.')
    overs = 21 - t_overs
    print(t_wickets, 'Wickets.')
    print()

    ls = [bat_team, bowl_team, t_score, batting_t_name, bowling_t_name, overs, t_wickets]
    return ls
