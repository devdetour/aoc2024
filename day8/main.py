import os
import itertools

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def xy_distance(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])
    # returns (x, y) diff between points

def part1(lines):
    # get sets of coordinates that each flavor of antenna occurs at
    # for each pair of coordinates:
    # - get the antinodes for each pair
    # - if on the map, add them to a set of antinodes
    # - count size of that set
    flavors = {} # 'a' => [(1, 2), (3, 4)]
    antinodes = {}

    # get coordinates for each type of antenna
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            char = lines[row][col]
            if char == "." or char == "#":
                continue
            if char not in flavors:
                flavors[char] = []
            flavors[char].append((row, col))
    
    for flavor in flavors:
        # check every pair of flavors, set antinodes
        pairs = itertools.combinations(flavors[flavor], 2)
        
        for p in pairs:
            distance = xy_distance(p[0], p[1])
            a1 = (p[0][0] - distance[0] * 2, p[0][1] - distance[1] * 2)
            a2 = (p[1][0] + distance[0] * 2, p[1][1] + distance[1] * 2)
        
            for node in [a1, a2]:
                if 0 <= node[0] < len(lines) and  0 <= node[1] < len(lines[0]):
                    antinodes[f"{node[0]},{node[1]}"] = flavor

    print(len(antinodes))

    # print(flavors)

def part2(lines):
    # get sets of coordinates that each flavor of antenna occurs at
    # for each pair of coordinates:
    # - get the antinodes for each pair
    # - if on the map, add them to a set of antinodes
    # - count size of that set
    flavors = {} # 'a' => [(1, 2), (3, 4)]
    antinodes = {}

    # get coordinates for each type of antenna
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            char = lines[row][col]
            if char == "." or char == "#":
                continue
            if char not in flavors:
                flavors[char] = []
            flavors[char].append((row, col))
    
    for flavor in flavors:
        # check every pair of flavors, set antinodes
        pairs = itertools.combinations(flavors[flavor], 2)
        
        for p in pairs:
            distance = xy_distance(p[0], p[1])

            # go up
            node = (p[0][0] - distance[0] , p[0][1] - distance[1] )
            while 0 <= node[0] < len(lines) and  0 <= node[1] < len(lines[0]):
                antinodes[f"{node[0]},{node[1]}"] = flavor
                node = (node[0] - distance[0], node[1] - distance[1])

            # go down
            node = (p[1][0] + distance[0] , p[1][1] + distance[1] )

            while 0 <= node[0] < len(lines) and  0 <= node[1] < len(lines[0]):
                antinodes[f"{node[0]},{node[1]}"] = flavor
                node = (node[0] + distance[0], node[1] + distance[1])
            

    print(len(antinodes))

def main():
    lines = read_file("input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()