# Opponent plays
# A for Rock
# B for Paper
# C for Scissors

# I Play
# X for Rock
# Y for Paper
# Z for Scissors

# I Score
# 1 for Rock
# 2 for Paper
# 3 for Scissors

# + 

# 0 if you lost
# 3 if the round was a draw
# 6 if you won

# A X = 3
# A Y = 6
# A Z = 0
# B X = 0
# B Y = 3
# B Z = 6
# C X = 6
# C Y = 0
# C Z = 3

# X Lose
# Y Draw
# Z Win

# A X = Z
# A Y = X
# A Z = Y
# B X = X
# B Y = Y
# B Z = Z
# C X = Y
# C Y = Z
# C Z = X

def get_me(opp, outcome):
    if opp == 'A':
        if outcome == 'X':
            return 'Z'
        elif outcome == 'Y':
            return 'X'
        else:
            return 'Y'
    elif opp == 'B':
        if outcome == 'X':
            return 'X'
        elif outcome == 'Y':
            return 'Y'
        else:
            return 'Z'
    else:
        if outcome == 'X':
            return 'Y'
        elif outcome == 'Y':
            return 'Z'
        else:
            return 'X'

def get_hand_value(me):
    if me == 'X':
        return 1
    elif me == 'Y':
        return 2
    else:
        return 3

def get_score(opp, me):
    if opp == 'A':
        if me == 'X':
            return 3
        elif me == 'Y':
            return 6
        else:
            return 0
    elif opp == 'B':
        if me == 'X':
            return 0
        elif me == 'Y':
            return 3
        else:
            return 6
    else:
        if me == 'X':
            return 6
        elif me == 'Y':
            return 0
        else:
            return 3

with open("input.txt") as input:

    total = 0

    for line in input:
        opponent = line[0]
        outcome = line[2]
        me = get_me(opponent, outcome)
        total += get_score(opponent, me)
        total += get_hand_value(me)
    
    print(total)
        
