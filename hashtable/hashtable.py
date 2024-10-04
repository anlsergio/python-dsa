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
            my_hash = (my_hash + letter_ascii_numerical_value * arbitrary_prime_number) % address_space

        # Return the final hash value, which corresponds to an index in the hash table.
        return my_hash

    def print(self):
        for k, v in enumerate(self.data_map):
            print(k, ": ", v)

my_hash_table = HashTable()

my_hash_table.print()
