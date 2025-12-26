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

