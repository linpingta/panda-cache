__all__ = (
    "LRUCache",
    "LFUCache",
    "FIFOCache",
    "LIFOCache",
    "RRCache",
    "MRUCache",
)

__version__ = "0.1.0"

from .lru_cache import LRUCache
from .lfu_cache import LFUCache
from .fifo_cache import FIFOCache
from .lifo_cache import LIFOCache
from .rr_cache import RRCache
from .mru_cache import MRUCache