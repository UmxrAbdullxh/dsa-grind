# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        modes = []
        modeCount = 0
        prev = None
        count = 0
        def dfs(root):
            nonlocal modeCount, prev, count
            if not root:
                return None
            dfs(root.left)
            if prev == root.val:
                count += 1
            else:
                count = 1
            prev = root.val
            if count > modeCount:
                modeCount = count
                modes.clear()
                modes.append(root.val)
            elif modeCount == count:
                modes.append(root.val)
            dfs(root.right)
            return None
        dfs(root)
        return modes
        