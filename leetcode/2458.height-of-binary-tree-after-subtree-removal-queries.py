# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:
        depth = {}
        height = {}
        top1 = {}
        top2 = {}
        result = []

        def dfs(root, d):
            if not root:
                return -1
            
            depth[root.val] = d
            h = 1 + max(dfs(root.left, d+1), dfs(root.right, d+1))
            deepest_level = d + h
            height[root.val] = h

            if deepest_level > top1.get(d, -1):
                top2[d] = top1.get(d, -1)
                top1[d] = deepest_level
            elif deepest_level > top2.get(d, -1):
                top2[d] = deepest_level

            return h
        dfs(root, 0)
        for q in queries:
            dep = depth[q]
            hei = height[q]
            reach = dep + hei
            best_other = -1
            if reach == top1.get(dep):
                best_other = top2.get(dep)
            else:
                best_other = top1.get(dep)
            result.append(max(dep - 1, best_other))
        return result
        