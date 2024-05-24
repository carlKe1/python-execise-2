# . Using a for loop, create the list below, which consists of ones separated by increasingly many
# zeroes. The last two ones in the list should be separated by ten zeroes.
# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

# Initialize an empty list to store the sequence
sequence = []

# Initialize the number of zeroes to add between ones
zeroes_count = 0

# Iterate over a range from 1 to 10
for i in range(1, 11):
    # Append a one to the sequence
    sequence.append(1)
    
    # Append zeroes based on the current value of i
    sequence.extend([0] * zeroes_count)
    
    # If i is less than 10, increment the number of zeroes to add
    if i < 10:
        zeroes_count += 1

# Print the resulting sequence
print(sequence)
