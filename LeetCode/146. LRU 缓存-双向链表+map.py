from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.use = deque()
        self.cap = capacity


    def get(self, key: int) -> int:
        if key in self.m:
            # idx = self.use.index(key)
            self.use.remove(key)
            self.use.appendleft(key)

            return self.m[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.use.remove(key)
            self.use.appendleft(key)
            self.m[key] = value
        else:
            if len(self.use) < self.cap:
                self.use.appendleft(key)
                self.m[key] = value
            else:
                remove_key = self.use.pop()
                self.m.pop(remove_key)
                self.use.appendleft(key)
                self.m[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)