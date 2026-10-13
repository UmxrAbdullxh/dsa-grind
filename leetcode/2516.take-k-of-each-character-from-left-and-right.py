class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = {}
        n = len(s)
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        l = 0
        best = float("-inf")
        for r in range(len(s)):
            add = s[r]
            freq[add] = freq.get(add) - 1
            while((freq.get('a', 0) < k or freq.get('b', 0) < k or freq.get('c', 0) < k) and l < n and l <= r ):
                rem = s[l]
                freq[rem] = freq.get(rem) + 1
                l += 1
            best = max(best, r-l+1)
        if best == 0:
            if min(freq.values()) < k or len(freq.keys()) != 3:
                return -1
            else:
                return n
        else:
            return n - best
        