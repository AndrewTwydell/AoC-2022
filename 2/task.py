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
        me = line[2]
        total += get_score(opponent, me)
        total += get_hand_value(me)
    
    print(total)
        
