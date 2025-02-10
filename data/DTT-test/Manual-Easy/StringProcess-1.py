def solution(input):
    # Find the start of the team name by locating the first occurrence of '[['
    start_index = input.find('[[') + 2
    # Find the end of the team name by locating the first occurrence of ']]'
    end_index = input.find(']]')
    # Extract the team name using the start and end indices
    team_name = input[start_index:end_index]
    # The team name is followed by a '|', so split and take the second part
    team_name = team_name.split('|')[1]
    return team_name