
grid = [
    ["Z","V","T","B","J","G","R"],
    ["L","V","R","J"],
    ["F","Q","S"],
    ["G","Q","V","F","L","N","H","Z"],
    ["W","M","S","C","J","T","Q","R"],
    ["F","H","C","T","W","S"],
    ["J","N","F","V","C","Z","D"],
    ["Q","F","R","W","D","Z","G","L"],
    ["P","V","W","B","J"]
]

with open("input.txt") as input:
    inputArr = []

    for line in input:
        formattedLine = line.strip().replace("move ", "").replace(" from ", "-").replace(" to ", "-")
        quantity = int(formattedLine.split("-")[0])
        fromList = int(formattedLine.split("-")[1]) - 1
        toList = int(formattedLine.split("-")[2]) - 1
        inputArr.append([quantity, fromList, toList])

    for move in inputArr:
        quantity = move[0]
        fromList = move[1]
        toList = move[2]

        toMove = grid[fromList][0:quantity]
        for item in reversed(toMove):
            grid[toList].insert(0,item)

        grid[fromList] = grid[fromList][quantity:]
    
    outStr = ""
    for row in grid:
        outStr += str(row[0])
    print(outStr)