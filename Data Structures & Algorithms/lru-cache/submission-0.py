class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage.move_to_end(key)
        self.storage[key] = value
        if len(self.storage) > self.capacity:
            self.storage.popitem(last=False)

        
