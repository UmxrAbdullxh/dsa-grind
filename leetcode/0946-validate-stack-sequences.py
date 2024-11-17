class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        count = 0
        for n, i in enumerate(pushed):
            stack.append(i)
            if i == popped[count]:
                while( count < len(popped) and stack and popped[count] == stack[-1] ):
                    stack.pop()
                    count += 1
        return not stack
        
