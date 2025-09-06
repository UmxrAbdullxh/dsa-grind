class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i, j, memo):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1, memo)
                memo[(i, j)] = res
                return res
            else:
                res1 = max(dfs(i + 1, j, memo), dfs(i, j + 1, memo))
                memo[(i,j)] = res1
                return res1
            
        return dfs(0, 0,{})
