# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; 
# the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

total = 0

with open('03input.txt','r') as f:
    for line in f:
        line = str(line.strip())
        result = ""

        # first digit must have at least 11 to the right.
        # pick largest first digit that still has at least 11 to the right
        # and repeat for the rest of the digits
        start = 0
        for position in range(12):  # picking digit #0, #1, #2, ... #11
            remaining_needed = 12 - position  # after this pick, how many more?
            
            # Can search from 'start' up to a point that leaves enough digits
            search_end = len(line) - remaining_needed + 1
            
            # Find max digit in this range
            best_digit = line[start]
            best_index = start
            
            for i in range(start, search_end):
                if line[i] > best_digit:
                    best_digit = line[i]
                    best_index = i
            
            result += best_digit
            start = best_index + 1  # next search starts right after this pick
        total += int(result)

print (total)