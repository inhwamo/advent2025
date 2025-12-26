# Dial from 0 to 99
# L decreases the number. 
# Dial starts at 50
# For example, L68 subtracts 50, then 18 more, which is 82.

# 2 pieces of state:
count = 0
dial_position = 50

with open('01input.txt', 'r') as f:
    for line in f:
        line = line.strip()  # removes newline/whitespace

        # Get letter and number from each line
        letter = line[0] # first char is always L or R
        number = int(line[1:]) # rest are 1 integer

        if letter == "R":
            dial_position = (dial_position + number) % 100
        
        elif letter == "L":
            dial_position = (dial_position - number) % 100  

        if dial_position == 0:
            count = count + 1

print(count)