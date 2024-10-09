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
