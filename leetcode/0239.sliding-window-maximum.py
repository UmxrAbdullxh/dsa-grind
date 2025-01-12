class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = {}
        res = []
        maxV = float('-inf')
        for i in range(len(nums)):
            c = nums[i]
            window[c] = 1 + window.get(c, 0)
            maxV = max(maxV, c)
            if i + 1 >= k:
                res.append(maxV)
                start = (i + 1) - k
                window[nums[start]] -= 1
                if window[nums[start]] == 0:
                    del window[nums[start]]
                if nums[start] == maxV:
                    if len(window) > 0:
                        tmpMax = max(window.keys())
                        maxV = tmpMax
                    else:
                        maxV = float('-inf')
        return res
        
