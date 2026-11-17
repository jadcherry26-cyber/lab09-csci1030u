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
    # NEED TO MAKE AN ALGORITHM!
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
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    pass


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
