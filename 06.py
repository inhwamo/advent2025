with open('06input.txt', 'r') as f:
    grid = [line.rstrip('\n') for line in f] # grid is a list of strings, one per row

max_width = max(len(row) for row in grid)
# Pad all rows to same width
grid = [row.ljust(max_width) for row in grid] # ljust pads with spaces on the right so every row has the same length

# Defines a separator column, which is all spaces vertically
def is_separator(col_idx):
    return all(grid[row][col_idx] == ' ' for row in range(len(grid)))

# Find problem boundaries
problems = []
start = None

for col in range(max_width):
    if is_separator(col):
        if start is not None: # end the current problem, if currently inside a problem and you reach separator
            problems.append((start, col)) # add defined problem
            start = None
    else:
        if start is None: # start a new problem, if not currently inside a problem
            start = col

# last problem 
if start is not None:
    problems.append((start, max_width))

total = 0

for (start_col, end_col) in problems:
    # Extract the slice for this problem
    operator = None
    numbers = []
    
    for row in grid:
        segment = row[start_col:end_col].strip()

        # For each problem, slice horizontally across every row:

        # row[start_col:end_col]  →  "123" or " 45" or "  6" or "*  "
        # .strip()                →  "123" or "45"  or "6"  or "*"

        if segment in ['+', '*']:
            operator = segment
        elif segment:
            # This is a number
            numbers.append(int(segment))
    
    # Calculate result
    if operator == '+':
        result = sum(numbers)
    else:  # '*'
        result = 1
        for n in numbers:
            result *= n
    
    total += result

print(total)