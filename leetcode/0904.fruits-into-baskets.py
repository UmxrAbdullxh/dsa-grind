class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        best = 0
        l = 0
        freq = {}
        for r in range(n):
            fruit = fruits[r]
            freq[fruit] = freq.get(fruit, 0) + 1
            while len(freq.keys()) > 2:
                remove = fruits[l]
                freq[remove] = freq.get(remove, 0) - 1
                if freq[remove] <= 0:
                    del freq[remove]
                l += 1
            best = max(best, r-l+1)
        return best

        