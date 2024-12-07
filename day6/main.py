import os

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def get_next_direction(direction):
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    return UP

def run_game(grid, visited, guard_pos, direction):
    while True:
        # if the guard is about to hit an obstacle, turn.
        # get the next position and then see where that puts us
        next_row = guard_pos[0] + direction[0]
        next_col = guard_pos[1] + direction[1]

        # if that takes us of the grid... return
        if not (0 <= next_row < len(grid)) or not (0 <= next_col < len(grid[0])):
            print("next coord would be off grid, ", next_row, next_row)
            for row in grid:
                print("".join(row))
            return visited

        # if there is an obstacle, turn right and try again.
        if grid[next_row][next_col] == "#":
            direction = get_next_direction(direction)
            print("changing direction to ", direction)
            continue

        # otherwise, if there is no obstacle continue
        # mark visited
        if (next_row, next_col) not in visited:
            grid[next_row][next_col] = "X"
            visited.append((next_row, next_col))
        
        guard_pos = [next_row, next_col]

def get_key_for_visited(pos, direction):
    return f"{pos[0]},{pos[1]},{direction}"

def run_game_2(grid, visited, guard_pos, direction):
    visited_with_direction = {}

    while True:
        # if the guard is about to hit an obstacle, turn.
        # get the next position and then see where that puts us
        next_row = guard_pos[0] + direction[0]
        next_col = guard_pos[1] + direction[1]

        # if that takes us of the grid... return
        if not (0 <= next_row < len(grid)) or not (0 <= next_col < len(grid[0])):
            # print("next coord would be off grid, ", next_row, next_row)
            # for row in grid:
                # print("".join(row))
            return False
        
        # if next position puts us in a place we've been WITH the same orientation,
        # we are in a loop. return true.
        if get_key_for_visited((next_row, next_col), direction) in visited_with_direction:
            return True

        # if there is an obstacle, turn right and try again.
        if grid[next_row][next_col] == "#":
            direction = get_next_direction(direction)
            # print("changing direction to ", direction)
            continue

        # otherwise, if there is no obstacle continue
        # mark visited
        if (next_row, next_col) not in visited:
            grid[next_row][next_col] = "X"
            visited.append((next_row, next_col))
            visited_with_direction[get_key_for_visited((next_row, next_col), direction)] = True
        
        guard_pos = [next_row, next_col]

def part1(lines):
    grid = [[n for n in l] for l in lines]

    guard_pos = None

    visited = []

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == "^":
                guard_pos = [row, col]
                visited.append((row, col))
                break
    # print(guard_pos)
    total_visited = run_game(grid, visited, guard_pos, UP)
    print(total_visited)
    print(len(total_visited))

    # print(lines)

def get_sim_grid(grid, row, col):
    newGrid = [[n for n in l] for l in grid]
    newGrid[row][col] = "#"
    return newGrid

def part2(lines):
    grid = [[n for n in l] for l in lines]
    guard_pos = None

    visited = []

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == "^":
                guard_pos = [row, col]
                visited.append((row, col))
                break
    
    candidates = run_game(grid, visited, guard_pos, UP)

    total = 0

    for c in candidates:
        row = c[0]
        col = c[1]
        print(f"running game for {row}, {col}")
        if grid[row][col] == "#" or (row == guard_pos[0] and col == guard_pos[1]):
            continue

        sim_grid = get_sim_grid(grid, row, col)
        # otherwise, copy grid, put coord, send it.
        if run_game_2(sim_grid, [], guard_pos, UP):
            total += 1
    print(total)
    return
    

def main():
    lines = read_file("input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()