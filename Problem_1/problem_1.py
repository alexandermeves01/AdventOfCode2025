## Part 2

def lockpicking(line, position):
    line = line.strip()
    direction = line[0]
    n = int(line[1:])
    zero_point = 0

    if direction == "L":
        if position == 0:
            zero_point += n // 100
        else:
            if n < position:
                zero_point += 0
            else:
                zero_point += 1 + (n - position) // 100
        position = (position - n) % 100

    elif direction == "R":
        if position == 0:
            zero_point += n // 100
        else:
            dist_to_zero = 100 - position
            if n < dist_to_zero:
                zero_point += 0
            else:
                zero_point += 1 + (n - dist_to_zero) // 100
        position = (position + n) % 100

    return position, zero_point

def readinstructions():
    position = 50
    zero_count = 0
    with open("AoC2025_1.txt") as f:
        line_num = 1
        for line in f.readlines():

            position, zero_point = lockpicking(line, position)
            print("Line Number: " + str(line_num) + " Position: " + str(position), "Zero Point: " + str(zero_point))
            zero_count += zero_point
            print(zero_count)
            line_num += 1

readinstructions()