grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]


def picture_grid(grid_input):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            print(grid[y][x],end='')
        print()            

picture_grid(grid)