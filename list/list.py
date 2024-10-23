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
