class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # fixed window
        # take total_pts = sum of cardPoints
        # take out points with window size of n-k
        total_points = sum(cardPoints)
        max_points = 0
        N = len(cardPoints) - 1
        window_size = N - k + 1
        if window_size == 0:
            return total_points
        l, r = 0, 0
        current_points = 0
        while(r<=N):
            current_points += cardPoints[r]
            if((r-l+1) == window_size):
                max_points = max(max_points, total_points-current_points)
                current_points = current_points - cardPoints[l]
                l += 1
            r += 1

        return max_points 
        