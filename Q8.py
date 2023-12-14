# Hash Tables:
# Implement a hash table and write functions to insert, delete, and search for elements
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        # If the index is empty, create a new bucket (key-value pair)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # If the index already has buckets, check if the key already exists
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # If the key exists, update its value
                    self.table[index][i] = (key, value)
                    break
            else:
                # If the key does not exist, add a new bucket (key-value pair)
                self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)

        # If the index is not empty, search for the key
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value

        return None  # Return None if the key is not found

    def delete(self, key):
        index = self._hash_function(key)

        # If the index is not empty, search for and delete the key
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break

