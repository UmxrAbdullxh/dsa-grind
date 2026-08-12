class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        def summations(str1, str2):
            i, j = len(str1) - 1, len(str2) - 1
            carry = 0
            result = ""
            while i >=0 or j >= 0 or carry:
                num1 = int(str1[i]) if i >=0 else 0
                num2 = int(str2[j]) if j >=0  else 0
                add = num1 + num2 + carry
                digit = add % 10
                result = str(digit) + result
                carry = add // 10
                i -= 1
                j -= 1
            return result
        num2_len = len(num2) - 1
        result = ""
        for i in range(len(num2) -1, -1, -1):
            j = len(num1) - 1
            temp = ""
            carry = 0
            while j >= 0 or carry:
                n1 = int(num1[j]) if j >=0 else 0
                n2 = int(num2[i]) if i >=0 else 0
                mul = (n1 * n2 ) + carry
                digit = mul % 10
                temp = str(digit) + temp
                carry = mul // 10
                j -= 1
            backtick = num2_len - i
            if backtick:
                zero_to_add = "0" * backtick
                temp = temp + zero_to_add
            result = summations(temp, result)
        return result
