from collections import OrderedDict


class LRUCache(object):
    """
    Initialize the LFU cache.

    Args:
        capacity (int): Maximum number of items that can be stored in the cache.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    # Initialize a cache with capacity of 2
    cache = LRUCache(2)

    # Put some key-value pairs into the cache
    cache.put(1, 1)
    cache.put(2, 2)

    # Retrieve and print the value associated with key 1
    print(cache.get(1))  # Output: 1

    # Put another key-value pair into the cache, which should evict key 2
    cache.put(3, 3)

    # Try to retrieve key 2, which should not be found in the cache
    print(cache.get(2))  # Output: -1 (Key not found)

    # Retrieve and print the value associated with key 3
    print(cache.get(3))  # Output: 3