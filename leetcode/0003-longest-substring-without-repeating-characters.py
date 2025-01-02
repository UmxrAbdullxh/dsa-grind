class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ''
        res = 0
        for i in s:
            if i in string:
                while(i in string):
                    string = string[1:]
            string = string + i
            res = max(res, len(string))
        return res

