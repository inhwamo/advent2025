total = 0

# naive unoptimized brute-force solution:

with open('03input.txt','r') as f:
    for line in f:
        line = str(line.strip())
        length = len(line)
        largest = 0

        for i in range (0,length):
            for j in range  (i+1,length):
                val = int(line[i] + line[j])
                if val > largest:
                    largest = val
        total += largest

print(total)
        
