total = 0
grid = []

with open('04input.txt','r') as f:
    for line in f:
        grid.append(list(line.strip()))
    
while True:
    to_remove = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@': # found a roll
            # now count adjacents:
                adjacent_count = 0
                directions = [
                    (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
                    (0, -1),           (0, 1),    # left, right
                    (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
                ]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    # Check if this position is valid (within bounds)
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == '@':
                            adjacent_count += 1
                            
                if adjacent_count < 4:
                    to_remove.append((row, col))

    if len(to_remove) == 0:
        break

    for row, col in to_remove:
        grid[row][col] = '.'
        total += 1   

print(total)