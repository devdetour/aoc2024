import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

PLUS = "+"
TIMES = "*"
CONCAT = "Z"

def do_the_thing(result, nums, operator, end_map):
    if len(nums) == 0:
        # if we run out of numbers, mark where we ended up
        end_map[result] = True
        return
    
    if operator == PLUS:
        result += nums[0]

    if operator == TIMES:
        result *= nums[0]

    # do remainder on +
    do_the_thing(result, nums[1:], PLUS, end_map)

    # do remainder on *
    do_the_thing(result, nums[1:], TIMES, end_map)

def do_the_thing_2(result, nums, operator, end_map):
    if len(nums) == 0:
        # if we run out of numbers, mark where we ended up
        end_map[result] = True
        return
    
    if operator == PLUS:
        result += nums[0]

    if operator == TIMES:
        if result == 0:
            result = 1
        result *= nums[0]

    if operator == CONCAT:
        result = int(str(result) + str(nums[0]))
        # if len(nums) == 1:
        #     end_map[int(str(result) + str(nums[0]))] = True
        #     return
        # # a few cases if we're concatenating...
        # # concatenate result so far with next number, then continue
        # p1 = [int(str(result) + str(nums[0]))] + nums[1:]

        # do_the_thing_2(result, p1, PLUS, end_map)
        # do_the_thing_2(result, p1, TIMES, end_map)
        # # do_the_thing_2(result, p1, CONCAT, end_map)

        # if len(nums[1:]) > 1:
        #     # OR, concatenate next 2 numbers and add/multiply to result...
        #     p2 = [result, int(str(nums[0]) + str(nums[1]))] + nums[2:]
        #     do_the_thing_2(result, p2, PLUS, end_map)
        #     do_the_thing_2(result, p2, TIMES, end_map)
        #     # do_the_thing_2(result, p2, CONCAT, end_map)
    
    # do remainder on +
    do_the_thing_2(result, nums[1:], PLUS, end_map)

    # do remainder on *
    do_the_thing_2(result, nums[1:], TIMES, end_map)

    do_the_thing_2(result, nums[1:], CONCAT, end_map)

def part1(lines):
    total = 0

    for l in lines:
        parts = l.split(":")
        target = int(parts[0])
        nums = [int(n) for n in parts[1].strip().split(" ")]
        # do some math

        result = {}
        do_the_thing(0, nums, PLUS, result)
        do_the_thing(0, nums, TIMES, result)
        if target in result:
            total += target
            print("Hit target: ", l)

    print(total)

def part2(lines): 
    total = 0

    for l in lines:
        parts = l.split(":")
        target = int(parts[0])
        nums = [int(n) for n in parts[1].strip().split(" ")]

        # get all possible starting numbers
        result = {}
        do_the_thing_2(0, nums, PLUS, result)
        do_the_thing_2(0, nums, TIMES, result)
        do_the_thing_2(0, nums, CONCAT, result)
        if target in result:
            total += target
            print("Hit target: ", target)

    print(total)

def main():
    lines = read_file("input.txt")

    # result = {}
    # nums = [6, 8, 6, 15]
    # do_the_thing_2(0, nums, PLUS, result)
    # do_the_thing_2(0, nums, TIMES, result)
    # do_the_thing_2(0, nums, CONCAT, result)
    # print(result)

    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()