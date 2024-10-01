class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphaMap = {}
        for i in s:
            if i in alphaMap:
                alphaMap[i] = alphaMap[i] + 1
            else:
                alphaMap[i] = 1
        for j in t:
            if j in alphaMap:
                if alphaMap[j] == 1:
                    del alphaMap[j]
                else:
                    alphaMap[j] = alphaMap[j] - 1
            else:
                return False
        if len(alphaMap) == 0:
            return True
        else:
            return False
