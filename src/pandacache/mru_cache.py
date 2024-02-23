from collections import OrderedDict


class MRUCache(object):
    def __init__(self, capacity):
        """
        Initialize the MRU cache.

        Args:
            capacity (int): Maximum number of items that can be stored in the cache.
        """
        self.capacity = capacity
        # Ordered dictionary to store key-value pairs, maintaining the insertion order
        self.cache = OrderedDict()

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache and update its access order.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key if present, otherwise -1.
        """
        if key not in self.cache:
            return -1

        # Move the key-value pair to the end of the OrderedDict to mark it as most recently used
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):
        """
        Insert or update the value associated with the given key in the cache.

        Args:
            key: The key to insert or update the value for.
            value: The value to associate with the key.
        """
        if key in self.cache:
            # If key already exists, update its value and move it to the end to mark it as most recently used
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # If cache is at full capacity, remove the least recently used item (first item in OrderedDict)
                self.cache.popitem(last=False)
            # Insert the new key-value pair to the end of the OrderedDict
            self.cache[key] = value


if __name__ == '__main__':
    # Create an instance of MRUCache with capacity 3
    cache = MRUCache(3)

    # Insert key-value pairs into the cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(3, 'C')

    # Retrieve values from the cache
    print(cache.get(1))  # Output: A
    print(cache.get(2))  # Output: B

    # Insert another key-value pair, exceeding the capacity of the cache
    cache.put(4, 'D')

    # Retrieve values from the cache
    print(cache.get(3))  # Output: C (This value should still be in the cache)
    print(cache.get(1))  # Output: -1 (This key was least recently used and evicted from the cache)
    print(cache.get(4))  # Output: D (This value should be present in the cache)