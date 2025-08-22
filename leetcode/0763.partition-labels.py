class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []
        for i in range(len(s)):
            c = s[i]
            last[c] = max(last.get(c, 0), i)
        
        inital = 0
        while inital < len(s):
            first = s[inital]
            lastOccur = last[first]
            partitonLen = lastOccur - inital
            i = inital
            while i < lastOccur:
                lstOccur = last[s[i]]
                lastOccur = max(lstOccur, lastOccur)
                partitonLen = max(partitonLen, lastOccur-inital)
                i+=1
            res.append(partitonLen + 1)
            inital = lastOccur + 1
        return res

