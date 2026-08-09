class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_index(string, index):
            backspace = 0
            while index >= 0:
                if string[index] == "#":
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                else:
                    break
                index -= 1
            return index
            
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_next_index(s, i)
            j = get_next_index(t, j)

            if i < 0 and j < 0:
                return True

            if i < 0 or j < 0:
                return False
            
            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1

        return True
