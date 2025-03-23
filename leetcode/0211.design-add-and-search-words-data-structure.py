class Node:

    def __init__(self, val=''):
        self.val = val
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        if not word:
            return None
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = Node(i)
            current = current.children[i]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord
        
        return dfs(0, self.root)
           
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
