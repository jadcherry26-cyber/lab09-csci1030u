# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # - create a for loop for i in range that takes length of nums
    # - create a for loop for j in range for i + 1 (to go forward in the list) and checks length of nums
    # - create a condition for nums[j] that fi it is equal to target - nums[i] 
    # - then return i and j. and add return[] for the list

    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
    return[]

def max_profit(prices):
    # Outline:
    # - money is what i returns, days are just a constraint, so i must buy before i sell
    # - profit needs to be sell price - buy price, need biggest one or 0
    # - for [7, 1, 5, 3, 6, 4], best buy day is 1, best sell day is 6 (after 7 because cant sell before buying)
    # - so if buy at 1, sell at 6, profit = 5
    # - function takes list and returns 1 number (biggest profit) 
    #   create table to help 

    lowest_buy = float("inf")
    best_profit = 0
    for price in prices:
        if price < lowest_buy:
            lowest_buy = price
        
        profit = price - lowest_buy
        if profit > best_profit:
            best_profit = profit
    return best_profit

def max_subarray(nums):
    # Outline:
    #   Keep the best sum ending at the current position.
    #   Either extend the previous block or start a new one here.
    #   Track the largest sum seen so far.
    best_ending_here = best_so_far = nums[0]

    for num in nums[1:]:
        best_ending_here = max(num, best_ending_here + num)
        best_so_far = max(best_so_far, best_ending_here)

    return best_so_far


def is_balanced(s):   # Part 4 - stretch (optional)
    # Keep opening brackets on a stack. Each closing bracket must match
    # the most recent unmatched opening bracket.
    matching_open = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in matching_open:
            if not stack or stack.pop() != matching_open[char]:
                return False

    return not stack


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(is_balanced("({[]})"))  # True
    print(is_balanced("([)]"))    # False


if __name__ == "__main__":
    main()
