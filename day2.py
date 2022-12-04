f = open("day2input", "r").read().strip().split("\n")

shapes = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}

def matchPoints(opp, me):
    result = shapes[opp] - shapes[me]
    if (result == 0):
        return 3 # draw
        
    if (result in [-1, 2]):
        return 6 # win

    return 0

total = 0
for x in f:
    match = x.split(" ")
    out = shapes[match[1]] + matchPoints(match[0], match[1])
    total += out

print(total)
