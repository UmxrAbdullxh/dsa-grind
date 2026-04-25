class MyHashSet:
    """
    Optimized HashSet using direct addressing.
    Supports keys in the range [0, 10^6].
    All operations run in O(1) time.
    """
    def __init__(self):
        self._present = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self._present[key] = True

    def remove(self, key: int) -> None:
        self._present[key] = False

    def contains(self, key: int) -> bool:
        return self._present[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)