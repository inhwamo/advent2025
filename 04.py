total = 0
grid = []

with open('04input.txt', 'r') as f:
    for line in f:
        grid.append = line.strip()

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '@': # found a roll
                # now count adjacents:
                    adjacent_count = 0
                    # count for adjacents
                    
                    if adjacent_count < 4:
                        total +=1


print (total)