class Solution:
    def countSubstrings(self, s: str) -> int:

        res = defaultdict(int)

        for i in range(len(s)):
            # odd condition
            l, r = i, i

            while(l>=0 and r<len(s) and s[l] == s[r]):
                pal = s[l:r+1]
                res[pal] = res[pal] + 1
                l -= 1
                r += 1
            
            # even length 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pal = s[l:r+1]
                res[pal] = res[pal] + 1
                l -= 1
                r += 1
        
        return sum(res.values())
        
