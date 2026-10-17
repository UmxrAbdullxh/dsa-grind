class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # Have required and formed which are counts
        # Have need and window map counter.
        # Maintain a window size of k which is len(p)
        need = Counter(p)
        required = len(need)
        formed = 0
        window = {}
        result = []
        k = len(p)

        for i, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            # check conditions if formed word
            if ch in need and window[ch] == need[ch]:
                formed += 1
            if ch in need and window[ch] == need[ch] + 1:
                formed -= 1
            
            if i >= k:
                left = s[i-k]
                if left in need and window[left] == need[left]:
                    formed -= 1
                window[left] -= 1
                if left in need and window[left] == need[left]:
                    formed += 1
            
            if formed == required:
                result.append(i-k+1)
        return result
        