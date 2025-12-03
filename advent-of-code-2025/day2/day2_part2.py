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

    for i in range(length+1):
        subject = str(j[0]+i)
        l = len(subject)

        first = subject[0]
        prev = first 
        pat_len = int(l/2) 
        pattern = ""
        for k in range(pat_len):

            #if subject[pat_len] == first:
            pattern = subject[:pat_len]
            if pattern == subject[pat_len : 2*pat_len] and len(pattern) != 0 and pattern * int(l/len(pattern)) == subject:
                print(subject)
                total_count += int(subject)
                break
            pat_len -= 1 

print("total: ", total_count)



