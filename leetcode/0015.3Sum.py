class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        copy = {}
        res = []
        for i in range(len(nums) - 1):
            start = i+1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    var = str(nums[i]) + str(nums[start]) + str(nums[end])
                    if var not in copy:
                        tmpArr = [nums[i], nums[start], nums[end]]
                        res.append(tmpArr)
                    copy[var] = 1
                    start += 1
                    while( nums[start] == nums[start-1] and start < end):
                        start += 1
                    #if var not in copy:
        return (res)
