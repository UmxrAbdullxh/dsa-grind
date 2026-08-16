class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(string, i, j):
            while i < j:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        
        reverse(s, 0, len(s)-1)
        