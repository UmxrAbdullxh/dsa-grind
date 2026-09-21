# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.container = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.container.append(root)
            dfs(root.right)
            return None
        dfs(root)
        self.pointer = -1
        
        

    def next(self) -> int:
        if self.pointer < len(self.container):
            current = self.pointer+1
            node = self.container[current]
            self.pointer = current
            return node.val
        

    def hasNext(self) -> bool:
        if self.pointer < len(self.container)-1:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()