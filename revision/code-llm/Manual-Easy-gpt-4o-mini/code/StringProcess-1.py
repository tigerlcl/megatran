def solution(input):
    # Split the input string to isolate the part containing the team name
    parts = input.split('|')
    
    # The relevant part is the second part after the split
    sort_part = parts[1]
    
    # Extract the team name from the sort part
    # The team name is located between "Sort|" and the first "|"
    team_name = sort_part.split('Sort|')[1].split('|')[0]
    
    return team_name