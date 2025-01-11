class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initialise hashamps
        # check have and need are equal or not
        # run a loop if equal until they are not
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        window, count = {}, {}
        res, resLen = [-1, -1], float("infinity")
        for i in t:
            count[i] = 1 + count.get(i, 0)
        have, need = 0, len(count)
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            print("have", have, need)
            while have == need:
                # update result
                length = (r - l) + 1
                if length < resLen:
                    res = [l, r]
                    resLen = length
                # pop from start
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""


