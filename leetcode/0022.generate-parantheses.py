class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add "(" when open count is less than n
        # Only add ")" when closed count is less than open
        # Only valid solution when open == closed == n

        stack = []
        res = []

        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                dfs(openN+1, closedN)
                # cleanup
                stack.pop()

            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN+1)
                # cleanup
                stack.pop()

        dfs(0, 0)
        return res
