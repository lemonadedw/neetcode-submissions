class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.C = capacity
        

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)

        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if len(self.data) == self.C and key not in self.data:
            self.data.popitem(last=False)

        if key in self.data:
            self.data.move_to_end(key)

        self.data[key] = value
