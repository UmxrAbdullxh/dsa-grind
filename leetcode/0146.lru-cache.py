class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # map to store key to nodes for constant time get
        self.cache = {}
        # initialise dummy nodes for keeping track of LRU and most recent
        # left is LRU, right is most recent
        self.left, self.right = Node(0,0), Node(0,0)
        # connect the pointers
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
        

    def get(self, key: int) -> int:
        # check if key exists in cache and return the val
        if key in self.cache:
            # update node to most recent used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # check if key already exists in cache
        if key in self.cache:
            # remove the key in cache and insert new key
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # check if capacity has exceeded
        if len(self.cache) > self.cap:
            # get the LRU
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

