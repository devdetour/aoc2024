import os
import random
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    mid = lines.index('')
    rules = lines[:mid]    
    seqs = lines[mid + 1:]

    rules_dict = {}

    for rule in rules:
        nums = rule.split("|")
        a = int(nums[1])
        if a not in rules_dict:
            rules_dict[a] = []
        
        rules_dict[a].append(int(nums[0]))
    
    good_sequences = []

    for s in seqs:
        nums = [int(x) for x in s.split(",")]
        if is_sequence_good(nums, rules_dict):
            good_sequences.append(nums)

    print(good_sequences)
    total = 0
    for s in good_sequences:
        total += s[len(s) // 2]
    print(total)

def is_sequence_good(nums, rules_dict):
    seq_good = True
    seen = {}
    for n in nums:
        # for each number, check if we have a rule
        if n in rules_dict:
            # have to check each number of the rule. if in sequence,
            # has to come before.
            for rule in rules_dict[n]:
                if rule in nums and rule not in seen:
                    seq_good = False
        seen[n] = True

    return seq_good

rules_dict = {}

# def compare(a, b):
#     if a in rules_dict:
#     # have to check each number of the rule. if in sequence,
#     # has to come before.
#         for rule in rules_dict[a]:
#             if rule in nums and rule not in seen:
#                 seq_good = False
#     pass

def build_list(elements, rules):
    result = []

    total_len = len(elements)

    while len(result) < total_len:
        result.append(get_lowest_element(elements, rules))
        elements = list(filter(lambda x: x not in result, elements))
    return result

def get_lowest_element(elements, rules):
    random.shuffle(elements)
    # check the first element
    # if it has something that has to come before it,
    # then check that one.
    # ....
    # if we reach one that DOESN'T have one that needs to come
    # before it, that counts as our lowest.
    candidates = [elements[0]]

    checked = {}

    while len(candidates) > 0:
        if len(candidates) > 100000:
            # something weird. stop and try again
            random.shuffle(elements)
            return get_lowest_element(elements, rules)
        current = candidates.pop(0)
        # checked[current] = True
        print("checking", elements)

        if current not in rules: # no requirements
            return current
        
        candidates += filter(lambda x: x in elements and x not in checked, rules[current])
    return current # should never happen

def part2(lines):
    mid = lines.index('')
    rules = lines[:mid]    
    seqs = lines[mid + 1:]

    rules_dict = {}

    for rule in rules:
        nums = rule.split("|")
        a = int(nums[1])
        if a not in rules_dict:
            rules_dict[a] = []
        
        rules_dict[a].append(int(nums[0]))
    
    bad_sequences = []

    for s in seqs:
        nums = [int(x) for x in s.split(",")]
        if not is_sequence_good(nums, rules_dict):
            bad_sequences.append(nums)

    good_sequences = []

    total = 0

    for s in bad_sequences:
        print(s)
        result = build_list(s, rules_dict)
        total += result[len(result) // 2]

    print(total)

def main():
    lines = read_file("input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()