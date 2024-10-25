class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumStr = ""
        for i in s:
            if i.isalnum():
                alnumStr += i.lower()
        start = 0
        end = len(alnumStr) - 1
        while start < end:
            if alnumStr[start] == alnumStr[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

