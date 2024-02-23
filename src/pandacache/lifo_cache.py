class LIFOCache(object):
    """
    LIFO Cache implementation using Python.
    """

    def __init__(self, capacity):
        """
        Initializes the LIFO Cache with a given capacity.

        :param capacity: Maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        :param key: The key to retrieve the value for.
        :return: The value associated with the key, or -1 if the key is not found.
        """
        if key in self.cache:
            # Move the accessed key to the top of the stack
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        Inserts or updates the value associated with the given key in the cache.

        :param key: The key to insert or update.
        :param value: The value to associate with the key.
        """
        if len(self.cache) >= self.capacity:
            # Evict the least recently used key
            removed_key = self.stack.pop(0)
            del self.cache[removed_key]
        self.cache[key] = value
        self.stack.append(key)


if __name__ == '__main__':
    lifo_cache = LIFOCache(3)

    # Insert some key-value pairs
    lifo_cache.put(1, 'a')
    lifo_cache.put(2, 'b')
    lifo_cache.put(3, 'c')

    # Access a key
    print(lifo_cache.get(2))  # Output: 'b'

    # Insert another key-value pair, causing eviction
    lifo_cache.put(4, 'd')

    # Access an evicted key
    print(lifo_cache.get(1))
