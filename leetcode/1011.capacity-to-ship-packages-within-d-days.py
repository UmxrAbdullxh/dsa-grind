class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        res = r

        while l<=r:
            mid = (l+r) // 2
            totalDays = 1
            totalWeight = 0
            for w in weights:
                if totalWeight + w > mid:
                    totalWeight = 0
                    totalDays += 1
                totalWeight += w
            if totalDays <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
                    
