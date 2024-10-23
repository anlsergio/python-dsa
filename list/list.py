# Given a list of integers nums and an integer val, write a function
# remove_element that removes all occurrences of val in the list in-place
# and returns the new length of the modified list.
#
# The function should not allocate extra space for another list; instead, it
# should modify the input list in-place with O(1) extra memory.

def remove_element(nums, val):
    pos = 0
    for i in range(len(nums)):
        # move all the values that doesn't match "val"
        # to the beginning of the list
        if nums[i] != val:
            nums[pos] = nums[i]
            pos += 1

    # start removing items from the end
    # (the difference between the nums length and pos is how many items
    # must be popped out from the list, that in this case, happen to be the
    # matching values).
    for i in range(len(nums) - pos):
        nums.pop()

    return len(nums)


# Test case 5: Removing all instances of a repeated value.
nums5 = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)
print("-----------------------------------")


# Write a Python function that takes a list of integers as input and returns
# a tuple containing the maximum and minimum values in the list.

def find_max_min(nums):
    if not nums:
        return ()

    max = min = nums[0]
    for n in nums:
        if n > max:
            max = n
        if n < min:
            min = n
    return (max, min)


print(find_max_min([5, 3, 8, 1, 6, 9]))


# Write a Python function called find_longest_string that takes a
# list of strings as an input and returns the longest string in the list.
# The function should iterate through each string in the list,
# check its length, and keep track of the longest string seen so far.
# Once it has looped through all the strings,
# the function should return the longest string found.

def find_longest_string(string_list):
    max_string = ""
    for s in string_list:
        if len(s) > len(max_string):
            max_string = s
    return max_string


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)


# Given a sorted list of integers, rearrange the list in-place such that
# all unique elements appear at the beginning of the list.
#
# Your function should return the new length of the list containing only unique elements.
# Note that you should not create a new list or use any additional
# data structures to solve this problem.
# The original list should be modified in-place.

# Constraints:
#
# - The input list is sorted in ascending order.
# - The input list may contain duplicates.
# - The function should have a time complexity of O(n), where n is the length of the input list.
# - The function should have a space complexity of O(1), i.e., it should not use any
# additional data structures or create new lists
# (this also means you cannot use a set like we did earlier in the course).

def remove_duplicates(nums):
    move_count = 0
    # there's no need of iterating through the last item,
    # because it's included in the i+1 validation.
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            to_move = nums.pop(i)
            nums.append(to_move)
            move_count += 1
    return len(nums) - move_count


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


# You are given a list of integers representing stock prices for a certain company over
# a period of time, where each element in the list corresponds to the stock price for a specific day.
#
# You are allowed to buy one share of the stock on one day and sell it on a later day.
#
# Your task is to write a function called max_profit that takes the list of
# stock prices as input and returns the maximum profit you can make by buying
# and selling at the right time.
#
# Note that you must buy the stock before selling it, and you are allowed to make only
# one transaction (buy once and sell once).
def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for p in prices:
        min_price = min(min_price, p)
        balance = p - min_price
        profit = max(profit, balance)
    return profit


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")

prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")

prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


# You are given a list of n integers and a non-negative integer k.
#
# Your task is to write a function called rotate that takes the list of
# integers and an integer k as input and rotates the list to the right by k steps.
#
# The function should modify the input list in-place, and you should not return anything.
#
# Constraints:
# - Each element of the input list is an integer.
# - The integer k is non-negative.

def rotate(nums, k):
    # Calculate the effective rotation.
    # The modulo operator (%) is used to handle cases where
    # k is larger than the length of the list. This ensures
    # that the rotation count is within the bounds of the list's length.
    k = k % len(nums)

    # nums[:] = nums[-k:] + nums[:-k]
    # This line performs the rotation of the list.
    # Let's break down the slicing operations:

    # nums[-k:]:
    # This slice gets the last 'k' elements of the list.
    # In Python, negative indices start counting from the end of the list.
    # So, -k is the k-th element from the end.
    # For example, if k is 2, nums[-2:] gets the last two elements.

    # nums[:-k]:
    # This slice gets all elements of the list except the last 'k'.
    # Here, -k as the stop index in slicing means to stop before
    # the k-th element from the end.
    # For example, if k is 2, nums[:-2] gets all elements except the last two.

    # nums[-k:] + nums[:-k]:
    # This concatenates the last 'k' elements (nums[-k:])
    # with the first part of the list (nums[:-k]),
    # effectively rotating the list.

    # nums[:] = ...
    # Finally, nums[:] = is used to update the list in place.
    # It changes the original list 'nums' to be the rotated version.
    # Without [:], a new list would be created, and the original list
    # would remain unchanged.
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)
