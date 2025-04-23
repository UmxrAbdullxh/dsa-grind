class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        if len(digits) <= 0:
            return []
        if len(digits) == 1:
            for i in keyboard[digits]:
                res.append(i)
            return res

        def dfs(d):
            if len(d) == 1:
                key = keyboard[d]
                tmp1 = []
                for i in key:
                    tmp1.append(i)
                return tmp1
            tmp = dfs(d[1:])
            f = d[0]
            key2 = keyboard[f]
            tmp3 = []
            if tmp != None:
                for k in key2:
                    for char in tmp:
                        combination = k + char
                        tmp3.append(combination)
            return tmp3

            
            

        test = dfs(digits)
        return test

