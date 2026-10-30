class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        current_index = 0
        n = len(intervals)
        out = []

        while current_index < n and intervals[current_index][1] < newInterval[0]:
            out.append(intervals[current_index])
            current_index += 1
        
        while current_index < n and newInterval[1] >= intervals[current_index][0]:
            newInterval[0] = min(newInterval[0], intervals[current_index][0])
            newInterval[1] = max(newInterval[1], intervals[current_index][1])
            current_index += 1
        
        out.append(newInterval)

        while current_index < n:
            out.append(intervals[current_index])
            current_index += 1

        return out


        