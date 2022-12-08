
with open('input.txt') as input:
    grid = []
    for line in input:
        row = []
        for char in line.strip():
            row.append(int(char))
        grid.append(row)
    
    row_length = len(grid[0])
    col_length = len(grid)
    visible_trees = 0
    highest_score = 0
    best_location = (0, 0)

    for i in range(1, row_length - 1):
        for j in range(1, col_length - 1):
            tree_to_check = grid[i][j]

            left_count = 0
            for k in reversed(range(0, i)):
                left_count += 1
                if grid[k][j] >= tree_to_check:
                    break

            right_count = 0
            for l in range(i + 1, row_length):
                right_count += 1
                if grid[l][j] >= tree_to_check:
                    break
            
            top_count = 0
            for m in reversed(range(0, j)):
                top_count += 1
                if grid[i][m] >= tree_to_check:
                    break

            bottom_count = 0
            for n in range(j + 1, col_length):
                bottom_count += 1
                if grid[i][n] >= tree_to_check:
                    break
    
            scenic_score = left_count * right_count * top_count * bottom_count
            if scenic_score > highest_score:
                highest_score = scenic_score
                best_location = (i, j)

    print(best_location)
    print(highest_score)