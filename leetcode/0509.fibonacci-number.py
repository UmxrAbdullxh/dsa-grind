class Solution:
    def fib(self, n: int) -> int:
        def memo(n, memoObj):
            if n in memoObj:
                return memoObj[n]
            if n <= 2:
                return 1
            
            memoObj[n] = memo(n-1, memoObj) + memo(n-2, memoObj)
            return memoObj[n]
        
        return memo(n, {}) if n > 0 else 0
        
