# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if (node1 and not node2) or (node2 and not node1):
                return False
            if node1.val != node2.val:
                return False
            if (node1.left and not node2.left) or (node2.left and not node1.left):
                return False
            if (node1.right and not node2.right) or (node2.right and not node1.right):
                return False
            if node1.left and node2.left:
                queue1.append(node1.left)
                queue2.append(node2.left)
            if node1.right and node2.right:
                queue1.append(node1.right)
                queue2.append(node2.right)

        return True

