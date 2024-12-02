import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    print(lines)
    l = []
    r = []

    for line in lines:
        line.replace("   ", " ")
        nums = line.split()
        l.append(int(nums[0]))
        r.append(int(nums[1]))

    l = sorted(l)
    r = sorted(r)

    total = 0
    for i in range(len(l)):
        total += abs(l[i] - r[i])
    
    print(total)

    pass

def part2(lines):
    l = []
    r = {}

    for line in lines:
        line.replace("   ", " ")
        nums = line.split()
        l.append(int(nums[0]))
        occurrences = int(nums[1])
        if occurrences not in r:
            r[occurrences] = 0

        r[occurrences] += 1

    total = 0
    for num in l:
        if num in r:
            total += num * r[num]
    
    print(total)

    pass

def main():
    lines = read_file("input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()