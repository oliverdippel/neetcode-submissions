class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        seen = {}
        position = 0

        for i in strs:
            sorted_s = "".join(sorted(i))
            if sorted_s in seen:
                ret[seen[sorted_s]].append(i)
            else:
                seen[sorted_s] = position
                position += 1
                ret.append([i])
        
        return ret 