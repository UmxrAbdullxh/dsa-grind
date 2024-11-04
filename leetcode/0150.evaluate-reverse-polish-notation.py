class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i in operators:
                if i == "+":
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    res = int(ele1) + int(ele2)
                    stack.append(res)
                elif i == "-":
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    res = int(ele2) - int(ele1)
                    stack.append(res)
                elif i == "*":
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    res = int(ele1) * int(ele2)
                    stack.append(res)
                elif i == "/":
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    res = int(int(ele2) / int(ele1))
                    stack.append(res)
            else:
                stack.append(i)
        return int(stack[-1])
