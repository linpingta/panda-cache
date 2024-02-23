class RRCache(object):
    """
    Round Robin Cache implementation in Python.
    """

    def __init__(self, capacity):
        """
        Initialize the Round Robin Cache with a given capacity.

        Parameters:
        - capacity (int): The maximum number of elements the cache can hold.
        """
        self.capacity = capacity
        self.cache = []
        self.current_index = 0

    def put(self, item):
        """
        Add an item to the cache.

        If the cache is full, the oldest item is replaced with the new item.

        Parameters:
        - item: The item to be added to the cache.
        """
        if len(self.cache) < self.capacity:
            self.cache.append(item)
        else:
            self.cache[self.current_index] = item
            self.current_index = (self.current_index + 1) % self.capacity

    def get(self):
        """
        Retrieve an item from the cache.

        Returns:
        - item: The oldest item in the cache.
        """
        if not self.cache:
            return None
        item = self.cache[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.cache)
        return item


if __name__ == '__main__':
    # Create a Round Robin Cache with capacity of 3
    cache = RRCache(3)

    # Add items to the cache
    cache.put("A")
    cache.put("B")
    cache.put("C")

    # Retrieve items from the cache
    print(cache.get())  # Output: A
    print(cache.get())  # Output: B

    # Add more items to the cache
    cache.put("D")
    cache.put("E")

    # Retrieve items again
    print(cache.get())  # Output: C
    print(cache.get())  # Output: D
    print(cache.get())  # Output: E