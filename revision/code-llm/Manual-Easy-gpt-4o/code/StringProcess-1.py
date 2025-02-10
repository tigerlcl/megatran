def solution(input):
    # Find the start and end of the team name within the input string
    start = input.find('[[') + 2
    end = input.find(']]')
    
    # Extract the part of the string that contains the team name
    team_info = input[start:end]
    
    # Split the string to get the team name part
    team_name = team_info.split('|')[1]
    
    return team_name