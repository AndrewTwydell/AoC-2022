
highest = 0
highest2 = 0
highest3 = 0

totals = []

with open("input.txt") as input:
    total = 0
    for line in input:
        s = line.rstrip()
        if s == "":
            totals.append(total)
            total = 0
        else:
            total += int(s)
    
    totals.sort()
    print(totals[len(totals) - 1] + totals[len(totals) - 2] + totals[len(totals) - 3])
