class Solution:
    def minimumSteps(self, s: str) -> int:
        minSteps = 0
        zeroCount = 0
        chars = list(s)
        for i in range(len(chars)-1, -1, -1):
            if chars[i] == "1":
                minSteps += zeroCount
            if chars[i] == "0":
                zeroCount += 1
        return minSteps
         