class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string = ''
        key = {}
        for s in s1:
            key[s] = key.get(s, 0) + 1
        res = {}
        for i,n in enumerate(s2):
            string = string + n
            res[n] = res.get(n, 0) + 1
            if res == key:
                return True
            if len(string) == len(s1):
                tmp = string[0]
                if res[tmp] == 1:
                    del res[tmp]
                else:
                    res[tmp] = res[tmp] - 1
                string = string[1:]
        return False
        
