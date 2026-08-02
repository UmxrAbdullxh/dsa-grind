class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = len(people)
        people = sorted(people)
        l, r = 0, len(people) - 1
        boatCount = 0
        while l < r:
            totalWeight = people[l] + people[r]
            if totalWeight > limit:
                r -= 1
            else:
                boatCount += 1
                l += 1
                r -= 1
        remainingPairs = res - (boatCount * 2)
        boatCount += remainingPairs
        return min(res, boatCount)
        