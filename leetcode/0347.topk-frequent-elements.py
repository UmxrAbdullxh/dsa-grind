class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # My nlogn solution
        # nMap = {}
        # for i in nums:
        #     nMap[i] = nMap.get(i, 0) + 1

        # nValues = sorted(list(nMap.values()), reverse=True)
        # counter = 0
        # result = []
        # while( counter < k ):
        #     for key, value in nMap.items():
        #         if value == nValues[counter]:
        #             result.append(key)
        #             del nMap[key]
        #             break
        #     counter = counter + 1
        # return result

        # O(n) solution using bucket sort (sort of)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for c, n in count.items():
            freq[n].append(c)

        res = []
        for i in range(len(freq)-1, 0, -1):
            ele = freq[i]
            for j in ele:
                res.append(j)
                if len(res) == k:
                    return res
