## Part 1

def lockpicking(line, position):
    #Turn to smaller numbers if left (overflow is modulo-ed)
    if line[0] == "L":
        position = (100 + (position - int(line[1::]))) % 100
    # Turn to higher numbers if right (overflow is modulo-ed)
    if line[0] == "R":
        position = (100 + (position + int(line[1::]))) % 100
    return position

def readinstructions():
    position = 50
    zero_count = 0
    with open("AoC2025_1.txt") as f:
        for line in f.readlines():
            position = lockpicking(line, position)
            if position == 0:
                zero_count += 1
    print(zero_count)

readinstructions()