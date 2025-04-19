class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        temp = []

        def dfs(i):
            if i >= len(s):
                res.append(temp.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    temp.append(s[i:j+1])
                    dfs(j+1)
                    temp.pop()

        dfs(0)
        return res

    def isPalindrome(self, string):
        if string[::-1] == string:
            return True
        else:
            return False
        
