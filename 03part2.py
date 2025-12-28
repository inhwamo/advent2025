# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; 
# the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

total = 0

# naive unoptimized brute-force solution:

with open('03input.txt','r') as f:
    for line in f:
        line = str(line.strip())
        length = len(line)
        largest = 0

    # first digit must have at least 11 to the right.
    # pick largest largest first digit that still has at least 11 to the right
        

    