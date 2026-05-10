class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.cache = OrderedDict() # using a sorted dictionary so we can maintain recency of access as order
        self.cap = capacity

    def get(self, key: int) -> int:
        # invalid key
        if key not in self.cache:
            return -1
        
        # otherwise, we need to mark the cache element as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        
        # tag as recently used/updated
        if key in self.cache:
            self.cache.move_to_end(key)
        # update value
        self.cache[key] = value

        while len(self.cache) > self.cap:
            # pop least recently used element
            self.cache.popitem(last=False)
        
