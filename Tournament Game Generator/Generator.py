# Establishes global variables 
team_names = []
team_wins = []
names_and_wins = {}
games_played = 0

# Asks for the number of teams that are going to be in the tournament
# and checks to make sure there are at least 2 teams
# It is assumed that there will be an even number of teams
while True:
    num_teams = input("Enter the number of teams in the tournament: ")
    if int(num_teams) >= 2:
        break
    else:
        print("The minimum number of teams if 2, try again.")

# Asks for the names of each team and appends it to an array
# Checks that each team is at most two words and at last 2 letters
for i in range(1, int(num_teams) + 1):
    while True:
        team = input(f"Enter the name for team #{i}: ")
        if len(team) < 2:
            print("Team names must have at least 2 characters, try again.")
        elif len(team.split(" ")) > 2:
            print("Team names may have at most 2 words, try again.")
        else:
            break
        
    team_names.append(team)

# Asks for the number of games each team has played when each team has 
# played each other at least once in the regular season
while True:
    games_played = input("Enter the number of games played by each team: ")
    if int(games_played) < len(team_names) - 1:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    else: 
        break

# Asks for the number of wins each team had in the regular season
# and checks that its not greater then the number of games played
# then appends it to an array
for i in team_names:
    while True:
        wins = input(f"Enter the number of wins Team {i} had: ")
        if wins > games_played: 
            print(f"The maximum number of wins is {games_played}, try again.")
        elif int(wins) < 0:
            print("The minimum number of wins is 0, try again.")
        else:
            team_wins.append(wins)
            break

# Adds all wins associated with each team into a dictionary
print("Generating the games to be played in the first round of the tournament...")
for i, j in enumerate(team_names):
    names_and_wins[j] = team_wins[i]

# Sorts the dictionary by value in ascending order 
wins_sorted = {k: v for k, v in sorted(names_and_wins.items(), key=lambda item: item[1])}

# Gets key from the dictionary and puts them into an array
# Then pairs up the teams with the most wins to the team 
# with the least wins and then prints it and removes it from the array
keys = list(wins_sorted.keys())
while len(keys) > 1:
    least = keys[0]
    most = keys[-1]
    print(f"Home: {least} VS Away: {most}")
    keys.pop(0)
    keys.pop()