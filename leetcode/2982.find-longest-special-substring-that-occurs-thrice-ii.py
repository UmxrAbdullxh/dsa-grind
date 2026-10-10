class Solution:
    def maximumLength(self, s: str) -> int:
        streak = 0
        top = {}

        for i, ch in enumerate(s):
            if i > 0 and ch == s[i-1]:
                streak += 1
            else:
                streak = 1
            
            vals = top.setdefault(ch, [])
            vals.append(streak)
            vals.sort(reverse=True)
            del vals[3:]
        
        ans = -1
        for items in top.values():
            if len(items) == 3:
                ans = max(ans, items[2])

        return ans
        