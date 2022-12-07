

def does_contain(biggest, smallest):    
    if int(smallest[0]) >= int(biggest[0]) and int(smallest[1]) <= int(biggest[1]):
        return True
    else:
        return False

with open('input.txt') as input:

    inputArr = []
    total = 0

    for line in input:
        inputArr.append(line.strip())
    
    for item in inputArr:
        p1 = item.split(',')[0]
        p2 = item.split(',')[1]

        diff1 = int(p1.split('-')[1]) - int(p1.split('-')[0])
        diff2 = int(p2.split('-')[1]) - int(p2.split('-')[0])

        if diff1 > diff2:
            biggest = p1.split('-')
            smallest = p2.split('-')
        else:
            biggest = p2.split('-')
            smallest = p1.split('-')
        
        if does_contain(biggest, smallest):
            total += 1
        
    print(total)