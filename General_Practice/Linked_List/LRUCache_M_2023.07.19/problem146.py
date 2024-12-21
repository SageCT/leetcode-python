from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.cap = capacity

    # ? If key is within lru ordered dict
    # ? move the key to the end (most recently used)
    # ? and return key
    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        return -1

    # ? sets new item in dict and moves to the end
    # ? (most recently used)
    # ? If capacity is hit, popitem(False) for FIFO

    def put(self, key: int, value: int) -> None:
        self.lru[key] = value
        self.lru.move_to_end(key)
        if len(self.lru) > self.cap:
            self.lru.popitem(False)
