class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k, memo):
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            if len(s1) + len(s2) != len(s3): 
                return False
            if i >= len(s1) and j >= len(s2) and k >= len(s3):
                memo[(i,j,k)] = True
                return True
            # if k<len(s3) and (i < len(s1) and s1[i] != s3[k]) and (j<len(s2) and s2[j] != s3[k]):
            #     return False

            res = False
            if i<len(s1) and k<len(s3) and s1[i] == s3[k]:
                res = dfs(i+1, j, k+1, memo)
            if j<len(s2) and k<len(s3) and s2[j] == s3[k]:
                res = res or dfs(i, j+1, k+1, memo)

            memo[(i,j,k)] = res
            return res

        return dfs(0, 0, 0, {}) 
        
