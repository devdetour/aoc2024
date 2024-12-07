import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

directions = [
    (1, 1),
    (1, 0),
    (1, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, 1),
    (0, -1),
]

def traverse(grid, start, dirVec):
    i = 1

    rows = len(grid)
    cols = len(grid[0])

    while i < 4:
        newRow = start[0] + dirVec[0] * i
        newCol = start[1] + dirVec[1] * i

        if newRow < 0 or newRow >= rows:
            return False
        if newCol < 0 or newCol >= cols:
            return False
        if grid[newRow][newCol] != "XMAS"[i]:
            return False
        
        i += 1

    return True

def isXMAS(grid, start):
    # check corners
    corners = [
        (-1, -1),
        (-1, 1),
        (1, 1,),
        (1, -1,),
    ]

    rows = len(grid)
    cols = len(grid[0])

    mCount = 0
    sCount = 0

    for c in corners:
        newRow = start[0] + c[0]
        newCol = start[1] + c[1]
        if newRow < 0 or newRow >= rows:
            return False
        if newCol < 0 or newCol >= cols:
            return False
        if grid[newRow][newCol] not in "MS":
            return False
        if grid[newRow][newCol] == "M":
            mCount += 1
        if grid[newRow][newCol] == "S":
            sCount += 1
    
    # at the end, we need 2 M, 2 S, and opposite corners NOT to match
    return mCount == sCount == 2 and \
        (grid[start[0] + 1][start[1] + 1] != grid[start[0] - 1][start[1] - 1]) and \
        (grid[start[0] - 1][start[1] + 1] != grid[start[0] + 1][start[1] - 1])


def part1(lines):
    grid = lines

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                for direction in directions:
                    if traverse(grid, (row, col), direction):
                        total += 1

    print(total)

def part2(lines):
    # start from A
    # corners
    # make sure 2 Ms and 2 Ss
    # make sure opposite corners !=

    grid = lines

    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'A':
                if isXMAS(grid, (row, col)):
                    total += 1

    print(total)

def main():
    lines = read_file("input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()