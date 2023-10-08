# Count for each grouping
counts = []
file = open("input.txt", "r")

num = 0
for line in file:
    # strip whitespace
    val = line.strip()

    # if its not "" then its a number
    if val != "":
        num += int(val)

    # if its not a number then append to counts and reset num=0
    if line in ["\n", "\r\n", ""]:
        counts.append(num)
        num = 0

# use the max function to get the highest number in counts
highest = max(counts)
print(highest)
