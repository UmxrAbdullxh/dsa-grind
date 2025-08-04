class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(s, wordDict, memo):
            if s == "":
                return True
            if s in memo:
                return memo[s]

            for word in wordDict:
                if s.startswith(word):
                    suffix = s[len(word):]
                    if (dfs(suffix, wordDict, memo) == True):
                        memo[s] = True
                        return True
            
            memo[s] = False
            return False
        
        return dfs(s, wordDict, {})
        
