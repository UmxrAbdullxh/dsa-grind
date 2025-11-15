class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []
        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k = k-1
            stack.append(n)

        if k > 0:
            stack = stack[:-k]

        result = ''.join(stack).lstrip("0")
        return result if result else "0"
        
