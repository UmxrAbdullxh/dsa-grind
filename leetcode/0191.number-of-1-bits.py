class Solution:
    def hammingWeight(self, n: int) -> int:
        def convertToBin(number):
            s = bin(number)       # binary representation:  bin(-37) --> '-0b100101'
            s = s.lstrip('-0b') # remove leading zeros and minus sign
            return s      # len('100101') --> 6

        n = convertToBin(n)
        result = 0
        for i in n:
            if i == "1":
                result += 1
        return result

