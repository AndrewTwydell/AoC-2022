
def some_chars_match_others(char1, char2, char3, char4):
    if char1 == char2 or char1 == char3 or char1 == char4:
        return True
    elif char2 == char3 or char2 == char4:
        return True
    elif char3 == char4:
        return True
    else:
        return False

with open('input.txt') as input:
    inputString = input.read().strip()
    
    for i in range(len(inputString) - 3):
        char1 = inputString[i]
        char2 = inputString[i + 1]
        char3 = inputString[i + 2]
        char4 = inputString[i + 3]

        if not some_chars_match_others(char1, char2, char3, char4):
            print(i+4)
            exit(0)
        
        