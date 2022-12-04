f = open("day3input", "r").read().strip().split("\n")

def getCharValue(char):
    ordVal = ord(char)
    
    if ordVal > 96:
        return ordVal - 96
    
    return ordVal - 38

def splitList(inList):
    half = len(inList) // 2
    return inList[:half], inList[half:]

score = 0
for x in f:
    print(x)
    it = map(getCharValue, list(x))
    firstHalf, secondHalf = splitList(list(it))
    firstHalfDict = dict.fromkeys(firstHalf) # dedup list

    for key in secondHalf:
        if key in firstHalfDict:
            print("DUPE: ", key)
            score += key
            break


print ("a: ", getCharValue('a'))
print ("z: ", getCharValue('z'))
print ("A: ", getCharValue('A'))
print ("Z: ", getCharValue('Z'))

print(score)
