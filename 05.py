fresh_count = 0
ranges = []
ingredients = []

reading_ranges = True

with open('05input.txt', 'r') as f:
    for line in f:
        line = line.strip()

        if line == '': # blank line seperates ranges and ingredients
            reading_ranges = False
            continue

        if reading_ranges: # not yet past middle
            start, end = line.split('-')
            ranges.append((int(start), int(end)))
        else: #reading_ranges = False, past the ranges
            ingredients.append(int(line))

for ingredient in ingredients:
    is_fresh = False
    for start, end in ranges:
        if start <= ingredient <= end:
            is_fresh = True
            break  # found a range, don't need to check others
    
    if is_fresh:
        fresh_count += 1


print(fresh_count)