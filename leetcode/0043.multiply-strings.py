class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Loop backward and maintain carry
        Loop the smaller string?
        How to handle subsequent iterations
        """
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1, -1, -1):
                total = int(num1[i]) * int(num2[j]) + res[i+j+1]
                res[i+j+1] = total % 10
                res[i+j] += total // 10
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        return "".join(map(str, res[start:]))
        