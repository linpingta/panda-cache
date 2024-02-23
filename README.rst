pandacache
========================================================================

[![GitHub stars](https://img.shields.io/github/stars/linpingta/chinese-poem-generator.svg?style=social&label=Star)](https://https://github.com/linpingta/panda-cache/stargazers)

[![Fork](https://img.shields.io/badge/-Fork-green?logo=github&style=for-the-badge)](https://https://github.com/linpingta/panda-cache/fork)

[![Clone](https://img.shields.io/badge/Clone-HTTPS-blue.svg)](https://https://github.com/linpingta/panda-cache.git)


Pandacache is a Python package that provides various caching mechanisms to efficiently store and retrieve data in your Python applications.

This module provides a lot of cache implementation with Python and AI.

Support Cache Type
------------------------------------------------------------------------
FIFO(First In, First Out) Cache

LIFO(Last In, First Out) Cache

LRU(Least Recently Used) Cache

LFU(Least Frequently Used) Cache

MRU(Most Recently Used) Cache

RR(Round Robin) Cache

Usage
------------------------------------------------------------------------
LRU Cache

.. code-block:: python

    from pandacache import LRUCache

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



RR Cache

.. code-block:: python

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


Installation
------------------------------------------------------------------------

Install with pip: (You can install `pandacache` via pip)

    pip install pandacache

Install local

    python setup.py sdist


Related Projects
------------------------------------------------------------------------

- cachetools: The project structure learn from it