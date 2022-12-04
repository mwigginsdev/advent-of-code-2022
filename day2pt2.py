f = open("day2input", "r").read().strip().split("\n")

shapes = {'A': 1, 'B': 2, 'C': 3}

# rock, paper, sciss
shapeScores = {
    'A': {'X': 3, 'Y': 1, 'Z': 2}, 
    'B': {'X': 1, 'Y': 2, 'Z': 3}, 
    'C': {'X': 2, 'Y': 3, 'Z': 1}
}

score = {'X': 0, 'Y': 3, 'Z': 6}

total = 0
for x in f:
    match = x.split(" ")
    out = shapeScores[match[0]][match[1]] + score[match[1]]
    total += out

print(total)
