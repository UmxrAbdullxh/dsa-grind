class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        #print(result)

        for s in strs:
            counter = [0] * 26 # a - z list
            for c in s:
                counter[ord(c) - ord("a")] += 1

            result[tuple(counter)].append(s)
        return result.values()
