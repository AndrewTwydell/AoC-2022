
def some_chars_match_others(chars):
    charSet = set(chars)
    if len(charSet) == len(chars):
        return False
    else:
        return True

with open('input.txt') as input:
    inputString = input.read().strip()

    for i in range(len(inputString) - 13):
        chars = []
        for j in range(14):
            chars.append(inputString[i + j])
        if not some_chars_match_others(chars):
            print(i+14)
            exit(0)
        
        