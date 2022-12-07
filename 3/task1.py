
points = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_char_value(char):
    return points.index(char) + 1

with open('input.txt') as input:

    chars = []
    total = 0

    for line in input:
        part1 = line[:len(line) // 2]
        part2 = line[len(line) // 2:]

        for char in part1:
            if char in part2:
                chars.append(char)
                total += get_char_value(char)
                break

    print(total)
