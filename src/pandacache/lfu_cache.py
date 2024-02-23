from collections import defaultdict, OrderedDict


class LFUCache(object):
    """
    Initialize the LFU cache.

    Args:
        capacity (int): Maximum number of items that can be stored in the cache.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1

        value, freq = self.cache[key]
        self.freq_map[freq].pop(key)
        if not self.freq_map[self.min_freq]:
            self.min_freq += 1
        self.freq_map[freq + 1][key] = value
        self.cache[key] = (value, freq + 1)

        return value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)
            return

        if len(self.cache) >= self.capacity:
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[evict_key]

        self.cache[key] = (value, 1)
        self.freq_map[1][key] = value
        self.min_freq = 1
