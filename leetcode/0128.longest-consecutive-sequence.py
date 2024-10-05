class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # My nlogn solution
        # if len(nums) == 0:
        #     return 0
        # counter = {}
        # nums = list(set(nums))
        # nums.sort()
        # counter[nums[0]] = 1
        # result = 1
        # localCounter = 1
        # for i in nums:
        #     if i - 1 in counter:
        #         localCounter = localCounter + 1
        #     else:
        #         localCounter = 1
        #     counter[i] = 1
        #     if localCounter > result:
        #         result = localCounter
        # return result

        # Optmised O(n) solution
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length = length + 1
                longest = max(length, longest)
        return longest
        
