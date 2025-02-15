# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        return self.remove(root, key)
    def remove(self, current, value):
        if current == None:
            return current
        if(value < current.val):
            current.left = self.remove(current.left, value)
            return current
        elif(value > current.val):
            current.right = self.remove(current.right, value)
            return current
        else:
            if( current.left == None and current.right == None):
                return None
            if(current.left == None):
                return current.right
            elif(current.right == None):
                return current.left
            else:
                tempNode = self.minRight(current.right)
                current.val = tempNode.val
                # delete existing value
                current.right = self.remove(current.right,tempNode.val)
                return current
    def minRight(self, current):
        while(current.left != None):
            current = current.left
        return current

        
