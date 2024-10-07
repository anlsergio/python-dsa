from reportlab.lib.pagesizes import letter


class HashTable:
    # Initialize the hash table with a default size of 7 (a prime number).
    # Prime numbers help to evenly distribute keys across the table,
    # reducing the chances of collisions.
    def __init__(self, size=7):
        # Create the data map (hash table) with the specified size,
        # initializing all slots to None.
        self.data_map = [None] * size

    # Private method to generate a hash for a given key.
    def __hash(self, key):
        # Start with a base hash value of 0.
        my_hash = 0

        # Iterate over each letter in the key.
        for letter in key:
            # Get the ASCII (numerical) value of the character.
            letter_ascii_numerical_value = ord(letter)

            # Multiply the ASCII value by an arbitrary prime number (23).
            # Using a prime number helps with spreading out the hash values.
            arbitrary_prime_number = 23

            # Get the size of the hash table.
            address_space = len(self.data_map)

            # Update the hash value by adding the product of the letter's
            # ASCII value and the prime number, and take the modulo of the
            # table size to ensure the hash fits within the array's index range.
            # (In the expression `number % len = X` any number will result in `X <= len-1`)
            my_hash = (my_hash + letter_ascii_numerical_value * arbitrary_prime_number) % address_space

        # Return the final hash value, which corresponds to an index in the hash table.
        return my_hash

    def print(self):
        for k, v in enumerate(self.data_map):
            print(k, ": ", v)

    def set_item(self, key, value):
        index = self.__hash(key)
        # if the list in the index is not initialized,
        # then it should be initialized prior to adding an item to it.
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item_value(self, key):
        index = self.__hash(key)
        items = self.data_map[index]
        if not items:
            return None
        for item in items:
            if item[0] == key:
                return item[1]
        return None

    def keys(self):
        keys = []
        for items in self.data_map:
            if items is None:
                continue
            for item in items:
                    keys.append(item[0])
        return keys

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print()

print("\n Get item:")

print(my_hash_table.get_item_value("lumber"))

print("\n Get Keys:")
print(my_hash_table.keys())

###############################
# Find Item in common Algorithm
###############################

# this is the naive approach, because it's
# not as efficient as it could be.
# Given it utilizes nested loops, it's time complexity
# is O(n^2)
def item_in_common_naive(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

# this is a more efficient way of solving the problem
# which relies on looping through both lists
# subsequently, which is O(2n), considering we always drop
# the constant, the time complexity becomes simply O(n).
def item_in_common(list1, list2):
    # we use a dictionary which is a built-in
    # form of hash table in Python to access values directly.
    my_dict = {}
    for item1 in list1:
        my_dict[item1] = True
    for item2 in list2:
        if item2 in my_dict:
            return True
    return False


l1 = [1,2,3]
l2 = [4,5,2]
l3 = [4,5,6]
print("\nFind Equal Item naive:")
print("Expects True:", item_in_common_naive(l1, l2))
print("Expects False:", item_in_common_naive(l1, l3))

print("\nFind Equal Item Optimal:")
print("Expects True:", item_in_common(l1, l2))
print("Expects False:", item_in_common(l1, l3))

###############################
# Find Duplicates Algorithm
###############################

def find_duplicates(ll):
    duplicates = []
    aux_dict = {}
    for l in ll:
        if l in aux_dict:
            duplicates.append(l)
        aux_dict[l] = "seen"
    return duplicates

print("\nFind duplicates:")
print(find_duplicates([1,2,3,4]))
print(find_duplicates([1,2,3,4,2,3,0]))

###############################
# First Non-Repeating Algorithm
###############################

def first_non_repeating_char(word):
    aux_dict = {}
    for w in word:
        aux_dict[w] = aux_dict.get(w, 0) + 1

    for w in word:
        if aux_dict[w] == 1:
            return w
    return None

print("\nFirst non repeating char:")
print("leetcode:", first_non_repeating_char("leetcode"))
print("hello:", first_non_repeating_char("hello"))
print("aabbcc:", first_non_repeating_char("aabbcc"))

###############################
# Group Anagrams Algorithm
###############################

def group_anagrams(words):
    aux_dict = {}
    for word in words:
        # word_added informs the outer loop if the current word
        # was added to any existing sub-list.
        word_added = False
        for sub_list_key in aux_dict:
            # In case there is at least 1 sub-list available,
            # start comparing the length of the current string with
            # the length of the 1st string in each sub-list
            if len(word) == len(sub_list_key):
                # If there's a match, start checking if all characters in the
                # current string are present in the first item of the sub-list
                all_chars_match = True
                for w in word:
                    # if at least 1 character fails the validation
                    # flag all_chars_match accordingly.
                    if w not in sub_list_key:
                        all_chars_match = False
                        break
                # If all chars match, proceed to add the current string to the same sub-list
                # of the item being compared
                if all_chars_match:
                    aux_dict[sub_list_key].append(word)
                    word_added = True
                    # bug is here: after appending it still adds the word
                    # as key in the outer loop.
            else:
                continue
        # If the loop reaches the end of the hash table without the current
        # string finding a perfect match, create a sub-list of its own.
        # The key of the hash-table is the base anagram word.
        if not word_added:
            aux_dict[word] = []

    anagrams = []

    # extract all anagrams subgroups into
    # a list's sub-list to be returned.
    for key in aux_dict:
        sub_list = list([key])
        for anagram in aux_dict[key]:
            sub_list.append(anagram)
        anagrams.append(sub_list)

    return anagrams

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )
