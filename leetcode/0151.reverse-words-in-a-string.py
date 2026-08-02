class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = list(filter(self.filterSpace, words))
        l, r = 0, len(words) - 1
        while l < r:
            # move l forward until it points to a word
            while words[l] == "" and l < len(words) - 1:
                l += 1
            # move r backward until it points to a word
            while words[r] == "" and r > 0:
                r -= 1
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)

    def filterSpace(self, word):
        if word == "":
            return False
        else:
            return True
        