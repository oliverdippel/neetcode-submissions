from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or self.time_map[key][0][-1] > timestamp:
            return ""
        else:
            timeline = self.time_map[key]
            left=0
            right = len(timeline)-1

            while left <= right:
                mid = (left + right) // 2
                if timeline[mid][-1] <= timestamp:
                    left = mid+1
                else:
                    right = mid-1

            return timeline[right][0]
