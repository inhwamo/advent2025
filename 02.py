sum = 0

with open('02input.txt', 'r') as f:
    data = f.read().strip()  

ranges = data.split(',') # ranges split by commas
parsed_ranges = []
for ranges in ranges:
    start, end = ranges.split('-')
    parsed_ranges.append((int(start), int(end)))

# An invalid ID is some pattern repeated exactly twice - so the length must be even
# Split in half to check

# part 1
def is_invalid1(num):
    s = str(num)
    # if length is odd, can't be a repeated pattern
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

# part 2
def is_invalid2(num):
    s = str(num)
    
    # try all possible pattern lengths
    for pattern_length in range(1, len(s)):
        # can this pattern_length work?
        if len(s) % pattern_length != 0:
            continue  # skip, doesn't divide evenly
        
        # extract the pattern
        pattern = s[:pattern_length]
        
        # check if whole string is this pattern repeated
        # hint: pattern * (len(s) // pattern_length) should equal s
        
    return False  # if no pattern worked


for start, end in parsed_ranges:
    for num in range(start, end + 1):  # +1 because range is inclusive
        if is_invalid2(num):
            sum += num

print(sum)