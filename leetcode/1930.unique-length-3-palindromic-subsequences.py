class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set() # need to add mid, out to this
        left = set() # will hold the left to the middle character
        right = collections.Counter(s)
        # the middle character
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[i], c))
        
            left.add(s[i])
        return len(res)
