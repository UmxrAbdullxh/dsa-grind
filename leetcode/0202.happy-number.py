class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(n):
            return sum(int(d) ** 2 for d in str(n))
        
        slow, fast = n, n
        while True:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(fast)
            fast = digit_square_sum(fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False
