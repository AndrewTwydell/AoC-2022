
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

    for i in range(1, row_length - 1):
        for j in range(1, col_length - 1):
            tree_to_check = grid[i][j]
            
            visible_from_left = True
            for k in range(0,i):
                if grid[k][j] >= tree_to_check:
                    visible_from_left = False
                    break
            visible_from_right = True
            for l in range(i + 1, row_length):
                if grid[l][j] >= tree_to_check:
                    visible_from_right = False
                    break
            visible_from_top = True
            for m in range(0, j):
                if grid[i][m] >= tree_to_check:
                    visible_from_top = False
                    break
            visible_from_bottom = True
            for n in range(j + 1, col_length):
                if grid[i][n] >= tree_to_check:
                    visible_from_bottom = False
                    break
            
            if visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
                visible_trees += 1

    visible_trees += row_length + col_length + row_length + col_length - 4
    print(visible_trees)