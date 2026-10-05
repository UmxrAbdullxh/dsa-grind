class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n-k+1)]
        freq = {}
        temp = nums[:k]
        for t in temp:
            freq[t] = freq.get(t, 0) + 1
        def x_sum(x):
            top_x_arr = sorted([(value,key) for (key,value) in freq.items()])
            top_x_len = len(top_x_arr)
            top_sum = 0
            if top_x_len < x:
                for count, x in top_x_arr:
                    top_sum += count * x
                return top_sum
            top_x = top_x_arr[-x:]
            for count, x in top_x:
                top_sum += count * x
            return top_sum
        first_sum = x_sum(x)
        result[0] = first_sum
        result_pointer = 1
        for i in range(k, n):
            add = nums[i]
            freq[add] = freq.get(add, 0) + 1
            remove = nums[i-k]
            if freq[remove] - 1 <= 0:
                del freq[remove]
            else:
                freq[remove] = freq.get(remove, 0) - 1
            subsequent_sum = x_sum(x)
            result[result_pointer] = subsequent_sum
            result_pointer += 1
        return result
        