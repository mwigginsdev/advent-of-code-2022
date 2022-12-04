calorieSums = []
for x in open("day1input", "r").read().strip().split("\n\n"):
    calorieSums.append(sum(map(int, x.split())))

print(max(calorieSums))