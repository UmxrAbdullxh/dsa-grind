class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates = sorted(candidates)

        def dfs(combs, pos, currentSum):
            if currentSum == target:
                res.append(combs.copy()) 
            if currentSum > target:
                return
  
            prev = -1
            for i in range(pos, len(candidates)):
                temp = candidates[i]
                #print('prev', prev, temp)
                if prev == temp:
                    continue
                # print("temp", temp, combs)
                combs.append(temp)
                currentSum += temp
                dfs(combs, i+1, currentSum)

                temp2 = combs.pop()
                currentSum -= temp2
                prev = temp

        dfs([], 0, 0)
        return res
            
        
