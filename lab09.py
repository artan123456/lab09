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
    # Outer index (i) starts at 0
    # Inner index (j) starts at i + 1 (The element after i)
    # Each iteration checks the sum of the elements at i and j
    # Once the sum is equal to the target, it will return a list [i, j]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def max_profit(prices):
    # Outline:
    # Outer index (i) starts at 0
    # Inner index (j) starts at i + j (The element after i)
    # See what happens if you sell on each day j, hold onto largest
    highest_profit = 0
    for i in range(len(prices)):
        buy_balance = -prices[i] # Balance after buying
        for j in range(i + 1, len(prices)):
            profit = buy_balance + prices[j] # Profit if sold that day
            if (profit > highest_profit): # See if this is a better buy/sell pair
                highest_profit = profit # Found a better buy/sell pair
    return highest_profit



def max_subarray(nums):
    # Outline:
    # Outer index (i) starts at 0
    # Middle index (j) starts at i + j (The element after i)
    # Inner index (k) starts at i and goes to j & adds the numbers up
    # See if it is larger than the largest sum
    # If yes, make it the new largest sum
    # If no, do nothing, keep going 
    if len(nums) == 1:
        return nums[0]
    else:
        largest_sum = nums[0] # I don't want to put 0 because there's a chance that all subarrays add up to negative numbers
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j+1):
                    sum += nums[k]
                if sum > largest_sum: # Larger sum found
                    largest_sum = sum
        return largest_sum
    
                





def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # Loop through the string
    # Get a list to use like a stack
    # Add any open bracket you see to the list (push)
    # If you see a closed bracket, check if it is the same type as the last element in the list
    # If it is the same type, pop it
    # If it is a different type, break and return false
    # At the end of the loop, if the lists used like a stack is empty, return true, otherwise return false
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    brackets = []
    bracket_types = { # A dictionary for the bracket types
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }
    for character in s: # Break the string up into a list

        if character in "({[": # If it is an open bracket
            # Push to "stack"
            brackets.append(character)

        elif character in ")}]": # If it is a closed bracket

            if len(s) == 1:
                return False # First bracket is a closed bracket, cannot be balanced

            # Check if the closed bracket is of the right type, if so pop from "stack"
            if (bracket_types[brackets[-1]] == character): 
                brackets.pop()
            else:
                return False # Different type of bracket, not balanced
            
        else: # This isnt even a bracket
            return False
        
    if (brackets == []): # No brackets left, all brackets are closed
        return True
    else: # Some brackets left unclosed
        return False


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])   # returns 6   (4 + -1 + 2 + 1)
    print(is_balanced("()"))
    pass


if __name__ == "__main__":
    main()
