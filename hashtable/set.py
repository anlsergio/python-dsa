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
