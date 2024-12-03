import os
import re
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

DO = "O"
DONT = "N"

def find_idx(string, substring):
  indices = []
  start = 0
  while True:
    start = string.find(substring, start)
    if start == -1:
      return indices
    indices.append(start)
    start += 1





# do() -> enabled until don't()
# mul() only if we idx is > doIndex AND less than don't index

def should_count(s, idx):
    # idx = min(idx, len(s) - 1) # idk don't go off the end???
    print("checking",)

    while idx > 0:
        if s[idx] == DO:
            print("enabled")
            return True
        if s[idx] == DONT:
            print("disabled")
            return False
        idx -= 1
    

    print("defaulting to on")
    return True

def part1(lines):
    # just a sequence that looks like mul(xxx,yyy)
    # get all indices of "mul("
    # take substring to the closing parenthesis ")"
    # use a regex to check if substring valid valid
    # then if valid, split on comma, cast to int, multiple, add,  baddabingbaddaboom=
    total = 0

    for l in lines:
        l = l.replace("don't()", DONT).replace("do()", DO)
        
        potentials = find_idx(l, "mul(")
        for p in potentials:
            startIdx = p + 4 # because mul( is 4 long
            if ")" not in l[startIdx:]:
                break
            stopIdx = startIdx + l[startIdx:].index(")")
            subStr = l[startIdx:stopIdx]
            print(f"{startIdx} to {stopIdx} checking substr", subStr)
            if re.match("^[0-9]{1,3},[0-9]{1,3}$",subStr):
                print("match", subStr)
                nums = subStr.split(",")
                total += int(nums[0]) * int(nums[1])
            
    print(total)

def part2(lines):
    total = 0
    for l in lines:
        l = l.replace("don't()", DONT).replace("do()", DO)

        potentials = find_idx(l, "mul(")

        for p in potentials:
            startIdx = p + 4 # because mul( is 4 long
            if ")" not in l[startIdx:]:
                break
            stopIdx = startIdx + l[startIdx:].index(")")
            subStr = l[startIdx:stopIdx]
            print(f"{startIdx} to {stopIdx} checking substr", subStr)
            if re.match("^[0-9]{1,3},[0-9]{1,3}$",subStr):
                nums = subStr.split(",")
                # extra if statement here
                if should_count(l, startIdx):
                    total += int(nums[0]) * int(nums[1])
            
    print(total)
    pass

def main():
    lines = read_file("input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()