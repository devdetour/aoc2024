import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    # valid if
    # ( all increasing
    # OR all decreasing
    # )
    # AND difference is >= 1 and <= 3
    total = 0
    for l in lines:
        nums = [int(n) for n in l.split(" ")]
        prev = nums[0]
        
        increasing = nums[0] < nums[1]
        valid = True

        for n in nums[1:]:
            diff = abs(n - prev)
            if diff < 1 or diff > 3:
                valid = False
            
            if increasing != (prev < n):
                valid = False
            
            prev = n

        if valid:
            total += 1

    print(total)

def get_permutations(l):
    result = []
    for i in range(len(l)):
        result.append(l[0:i] + l[i+1:])
    return result

def part2(lines):
    total = 0
    for l in lines:
        nums = [int(n) for n in l.split(" ")]

        # BRUTE FORCE IT LOL
        for p in get_permutations(nums):
            prev = p[0]
            
            increasing = p[0] < p[1]
            valid = True

            for n in p[1:]:
                diff = abs(n - prev)
                if diff < 1 or diff > 3:
                    valid = False
                
                if increasing != (prev < n):
                    valid = False
                
                prev = n

            if valid:
                total += 1
                break

    print(total)
    pass

def main():
    lines = read_file("input.txt")
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()