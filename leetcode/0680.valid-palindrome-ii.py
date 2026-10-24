class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r):
            # plain converging check on s[l..r]
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # budget spent: try both options
                ans1 = is_pal(l+1, r)
                ans2 = is_pal(l, r-1)
                return ans1 or ans2
            l += 1
            r -= 1
        return True
        