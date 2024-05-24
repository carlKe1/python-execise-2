#  Repeatedly ask the user to enter a team name and the how many games the team won and
# how many they lost. Store this information in a dictionary where the keys are the team names
# and the values are lists of the form [wins, losses].
# (a) Using the dictionary created above, allow the user to enter a team name and print out
# the team’s winning percentage.
# (b) Using the dictionary, create a list whose entries are the number of wins of each team.
# (c) Using the dictionary, create a list of all those teams that have winning records.

def calculate_winning_percentage(wins, losses):
    if wins + losses == 0:
        return 0
    return (wins / (wins + losses)) * 100

def team_operations(teams):
    # (a) Allow the user to enter a team name and print out the team’s winning percentage
    team_name = input("Enter a team name: ")
    if team_name in teams:
        wins, losses = teams[team_name]
        winning_percentage = calculate_winning_percentage(wins, losses)
        print("Winning percentage of {}: {:.2f}%".format(team_name, winning_percentage))
    else:
        print("Team '{}' not found.".format(team_name))

    # (b) Create a list whose entries are the number of wins of each team
    wins_list = [wins for wins, _ in teams.values()]
    print("Number of wins of each team:", wins_list)

    # (c) Create a list of all those teams that have winning records
    print("Teams with winning records:")
    for team, (wins, losses) in teams.items():
        if wins > losses:
            print(team)

def main():
    teams = {}
    for _ in range(3):
        team_name = input("Enter team name: ")
        wins = int(input("Enter number of wins: "))
        losses = int(input("Enter number of losses: "))
        teams[team_name] = [wins, losses]
    team_operations(teams)

if __name__ == "__main__":
    main()
