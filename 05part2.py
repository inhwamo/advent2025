ranges = []

# parsing
with open('05input.txt','r') as f:
    for line in f:
        line = line.strip()
        
        if line == '': # blank line seperates ranges and ingredients, don't need to go past. Check b4 splitting
            break

        start, end = line.split('-')
        ranges.append((int(start), int(end)))


ranges.sort()

# many overlapping ranges. need to merge
# only check if the current range touches the last one in merged[], because ranges[] is sorted already.


merged = []
for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:  # overlaps or adjacent
        # Extend the last merged range
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        # No overlap, add as new range
        merged.append((start, end))

# Count total IDs in merged ranges
total = 0
for start, end in merged:
    total += (end - start + 1)  # +1 because inclusive

print(total)
