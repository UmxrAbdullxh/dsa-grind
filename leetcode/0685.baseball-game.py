class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif i == "D":
                c = stack[-1]
                stack.append(c*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
        
