# --- Day 4: Secure Container ---
import re

# Parse input
with open('day04.txt') as f:
    start, end = [int(x) for x in f.read().split(',')]

def num_to_list(number):
    return [int(_) for _ in str(number)]
    
def check_decreasing(number):
    nums = num_to_list(number)
    flag = True
    for num, next in zip(nums, nums[1:]):
        if next < num:
            flag = False
            break
    return flag

def check_double_p1(number):
    nums = num_to_list(number)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

def check_double_p2(number):
    REPEAT = 2
    pattern = re.compile(r"44+|55+|66+|77+|88+|99+")
    results = re.findall(pattern, str(number))
    if results:
        return REPEAT in [len(x) for x in results]
    return False


# Part one
total = 0
for n in range(start, end + 1, 1):
    if check_decreasing(n) and check_double_p1(n):
        total += 1
print(f"Part one answer: Total possible passwords --> {total}")

# Part two
total = 0
for n in range(start, end + 1, 1):
    if check_decreasing(n) and check_double_p2(n):
        total += 1
print(f"Part two answer: Total possible passwords --> {total}")