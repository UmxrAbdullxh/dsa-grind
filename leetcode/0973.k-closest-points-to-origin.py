class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        tempDict = defaultdict(list)
        res = []
        for coords in points:
            dist = (coords[0]*coords[0]) + (coords[1]*coords[1])
            temp.append(dist)
            tempDict[dist].append(coords)
        temp.sort()
        temp = temp[:k]
        temp = set(temp)
        for i in temp:
            coords = tempDict[i]
            for j in coords:
                res.append(j)
        return res

        
