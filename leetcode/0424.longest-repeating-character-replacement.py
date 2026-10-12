class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        count = [0] * 26
        l = 0
        for r in range(len(s)):
            ch = s[r]
            idx = ord(ch) - ord('A')
            count[idx] += 1
            while (r - l + 1) - max(count) > k:
                rem = s[l]
                idx = ord(rem) - ord('A')
                count[idx] -= 1
                l += 1
            best = max(best, r-l+1)
        return best

