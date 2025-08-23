class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = []
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            temp.append(t)

        target_a = False
        target_b = False
        target_c = False
        for t in temp:
            if t[0] == target[0]:
                target_a = True
            if t[1] == target[1]:
                target_b = True
            if t[2] == target[2]:
                target_c = True

        if target_a == True and target_b == True and target_c == True:
            return True
        else:
            return False
        
