def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),  # horizontal right
        (0, -1), # horizontal left
        (1, 0),  # vertical down
        (-1, 0), # vertical up
        (1, 1),  # diagonal down-right
        (-1, -1),# diagonal up-left
        (1, -1), # diagonal down-left
        (-1, 1)  # diagonal up-right
    ]
    
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search(x, y, dx, dy):
        for i in range(word_len):
            if not in_bounds(x + i * dx, y + i * dy) or grid[x + i * dx][y + i * dy] != word[i]:
                return False
        return True
    
    occurrences = []
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    occurrences.append((i, j, dx, dy))
    
    return occurrences

def find_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':
                s1 = grid[i-1][j-1] + 'A' + grid[i+1][j+1]
                s2 = grid[i-1][j+1] + 'A' + grid[i+1][j-1]
                if (s1 == 'MAS' or s1 == 'SAM') and (s2 == 'MAS' or s2 == 'SAM'):
                    total += 1
    
    return total

def main():
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file.readlines()]
    
    xmas_occurrences = find_xmas(grid)
    # for occ in xmas_occurrences:
    #     print(f"Found XMAS starting at ({occ[0]}, {occ[1]}) in direction ({occ[2]}, {occ[3]})")
    print(f"Found {len(xmas_occurrences)} occurrences of XMAS")
    
    mas_occurrences = find_mas_patterns(grid)
    # for occ in mas_occurrences:
    #     print(f"Found MAS pattern starting at ({occ[0]}, {occ[1]})")
    print(f"Found {mas_occurrences} occurrences of MAS patterns")


if __name__ == "__main__":
    main()