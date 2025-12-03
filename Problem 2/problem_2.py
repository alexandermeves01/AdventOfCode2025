
# Part 1

def isIDValid(id: str) -> bool:
    isValid = True
    if len(id)%2 == 0:
        windowSize = int(len(id)/2)
        if id[:windowSize] == id[windowSize:]:
            isValid = False
    return isValid


def getRanges():
    rollingSum = 0
    with open("AoC2025_2.txt") as f:
        wholeTextRanges = f.readline().strip().split(",")
        print(wholeTextRanges)
        for x in wholeTextRanges:
            numRange = x.split("-")
            for i in range(int(numRange[0].strip()), int(numRange[1].strip())+1):
                isValid = isIDValid(str(i))
                if not isValid:
                    rollingSum += i
    print(rollingSum)

getRanges()