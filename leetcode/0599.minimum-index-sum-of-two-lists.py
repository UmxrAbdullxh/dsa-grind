class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = float("inf")
        common = []
        result = []
        string_map = defaultdict(list)
        for i,n in enumerate(list1):
            string_map[n].append(i)
        for j, m in enumerate(list2):
            if m in string_map:
                common.append(m)
                index_val = string_map[m][0]
                index_sum = j + index_val
                string_map[m][0] = index_sum
                min_index = min(min_index, index_sum)
        for k in common:
            if string_map[k][0] <= min_index:
                result.append(k)
        return result
            
        