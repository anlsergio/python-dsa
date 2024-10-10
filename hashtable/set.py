# Sets, like dictionaries, are implemented using a hash table.
#
# Sets can only contain unique elements (meaning that duplicates are not allowed).
#
# They are useful for various operations such as finding the distinct elements in
# a collection and performing set operations such as union and intersection.

###############################
# De-dup Algorithm
###############################

def remove_duplicates(dup_list):
    # Turn the dup list into a set so that duplicates are
    # automatically left out, and turn it back to a list to be returned.
    return list(set(dup_list))

print("\nDe-dup:")

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)

###############################
# Has Unique Chars Algorithm
###############################

def has_unique_chars(chars):
    aux_set = set(chars)
    return len(chars) == len(aux_set)

print("\nHas unique chars:")

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False

###############################
# Find Pairs Algorithm
###############################

def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    result = []

    for n in arr2:
        diff = target - n
        if diff in set1:
            result.append((diff, n))

    return result

print("\nFind pairs:")

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)

#########################################
# Longest consecutive sequence Algorithm
#########################################

def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    max_count = 0
    nums_set = set(nums)

    for num in nums_set:
        # detects the first num of the current sequence
        # in a sequence of [1, 2, 3, 11, 12, 13, 14], for example
        # in case num is 11, num-1 is 10, which breaks the sequence,
        # and therefore, 11 is a new sequence.
        if num-1 not in nums_set:
            counter = 1
            # add to the counter until the num has sequence in the set.
            while num+1 in nums_set:
                counter +=1
                num += 1
            max_count = max(max_count, counter)

    return max_count


print("\nLongest consecutive sequence:")

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2, 10, 11, 12, 13, 14, 15]) )
