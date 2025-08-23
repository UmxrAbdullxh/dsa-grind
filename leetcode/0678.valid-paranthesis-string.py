class Solution:
    def checkValidString(self, s: str) -> bool:
        # make two variables, minLeft and maxLeft which will be the range of possibilites
        # loop over string, if open paranthesis then add 1 to both
        # if closing paranthesis, then sub 1 from both
        # if wildcard, then sub 1 from minLeft and add 1 to maxLeft
        # Edge cases, if maxLeft < 0, then return false
        # if minLeft < 0, assign minLeft = 0

        minLeft, maxLeft = 0,0
        for c in s:
            if c == "(":
                minLeft, maxLeft = minLeft + 1, maxLeft + 1
            elif c == ")":
                minLeft, maxLeft = minLeft - 1, maxLeft - 1
            else:
                minLeft = minLeft - 1
                maxLeft = maxLeft + 1
            if maxLeft < 0:
                return False
            if minLeft < 0:
                minLeft = 0
        return minLeft == 0
        
