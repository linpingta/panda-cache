class FIFOCache(object):
    def __init__(self, capacity):
        """
        Initializes the FIFO Cache with a given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.queue = []  # List to maintain the order of keys

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key whose associated value is to be retrieved.

        Returns:
            The value associated with the key if present, else returns -1.
        """
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        Adds or updates a key-value pair in the cache. If the cache is full,
        removes the least recently used item before adding the new one.

        Args:
            key: The key to be added or updated.
            value: The value associated with the key.
        """
        if len(self.cache) >= self.capacity:
            # If cache is full, remove the least recently used item
            if self.queue:
                oldest_key = self.queue.pop(0)
                del self.cache[oldest_key]

        self.cache[key] = value
        self.queue.append(key)


if __name__ == '__main__':
    # Create a FIFO cache with a capacity of 2
    cache = FIFOCache(2)

    # Add key-value pairs to the cache
    cache.put(1, 'a')
    cache.put(2, 'b')

    # Retrieve values from the cache
    print(cache.get(1))  # Output: 'a'
    print(cache.get(2))  # Output: 'b'

    # Add another key-value pair, causing eviction of the least recently used item (key 1)
    cache.put(3, 'c')

    # Key 1 should no longer be in the cache
    print(cache.get(1))  # Output: -1

    # Key 2 should still be in the cache
    print(cache.get(2))  # Output: 'b'