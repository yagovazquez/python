import numpy as np

# Read entire file as a string
with open("input.txt", "r") as f:
    data = f.read().strip()

# Split by commas to get each "a-b" pair
pairs = data.split(",")

# Convert each "a-b" into [a, b]
matrix = np.array([list(map(int, p.split("-"))) for p in pairs])

total_count = 0

for j in matrix:
    length = j[1]-j[0]

    for i in range(length):
        subject = str(j[0]+i)
        l = len(subject)
        if l % 2 == 0:
            count = 0
            l = int(l/2)
            for k in range(l):
                if subject[k] == subject[l+k]:
                    count += 1
                    
            if count == l:
                total_count += int(subject)


print(total_count)
