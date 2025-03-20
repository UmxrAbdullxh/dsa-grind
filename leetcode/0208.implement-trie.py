class Node:
    def __init__(self, value=''):
        self.value = value
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        if not word:
            return None
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node(i)
            curr = curr.children[i]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        if not word:
            return False
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        if curr.endOfWord:
            return True
        else:
            return False       

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
