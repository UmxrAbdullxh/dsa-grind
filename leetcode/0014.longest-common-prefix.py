class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = Trie()
            root = root.children[c]
        root.endOfWord = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie()
        for s in strs:
            if s == "":
                return ""
            root.addWord(s)
        self.res = ""
        def dfs(root):
            curr = root
            if len(curr.children.keys()) != 1:
                return
            w = list(curr.children.keys())[0]
            self.res = self.res + w
            curr = curr.children[w]
            if curr.endOfWord != True:
                dfs(curr)
        dfs(root)
        return self.res
        
