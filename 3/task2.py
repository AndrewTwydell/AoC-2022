
points = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_char_value(char):
    return points.index(char) + 1

with open('input.txt') as input:

    lines = []
    total = 0

    for line in input:
        lines.append(line)

    total_lines = len(lines)
    for x in range(total_lines // 3):
        bag_1 = lines[3*x]
        bag_2 = lines[3*x+1]
        bag_3 = lines[3*x+2]

        for char in bag_1:
            if char in bag_2:
                if char in bag_3:
                    total += get_char_value(char)
                    break
    
    print(total)

