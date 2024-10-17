class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                counter = 0
                matchStr = '' 
                while(counter<len(needle)):
                    if counter + i < len(haystack):
                        matchStr += haystack[counter+i]
                        print(matchStr)
                        if matchStr == needle:
                            return i
                    counter += 1
        return -1 
