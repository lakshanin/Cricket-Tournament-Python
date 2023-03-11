import teamProfiles as Tp


def selecting_team_name(group_input, team_input):
    if group_input == 1:
        t = Tp.GroupA[team_input - 1]
    elif group_input == 2:
        t = Tp.GroupB[team_input - 1]
    return t


def selecting_team(group_input, team_input):
    team = Tp.slTeam
    if group_input == 1 and team_input == 1:
        team = Tp.slTeam
    elif group_input == 1 and team_input == 2:
        team = Tp.ausTeam
    elif group_input == 1 and team_input == 3:
        team = Tp.wiTeam
    elif group_input == 1 and team_input == 4:
        team = Tp.nzTeam
    elif group_input == 2 and team_input == 1:
        team = Tp.indTeam
    elif group_input == 2 and team_input == 2:
        team = Tp.banTeam
    elif group_input == 2 and team_input == 3:
        team = Tp.engTeam
    elif group_input == 2 and team_input == 4:
        team = Tp.pakTeam
    return team
