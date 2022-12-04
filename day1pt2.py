f = open("day1input", "r")

outCalories = []
tempCalories = 0

for x in f:
    if x == '\n':
        outCalories.append(tempCalories) 
        tempCalories = 0

    else:
        tempCalories += int(x)

outCalories.sort()
outCalories.reverse()
print(outCalories[0] + outCalories[1] + outCalories[2])