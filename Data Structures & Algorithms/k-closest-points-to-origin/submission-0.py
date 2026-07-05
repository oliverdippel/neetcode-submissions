import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            euc_dist = (x**2 + y**2)**(0.5)
            heapq.heappush(heap, (-euc_dist, x, y))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for _, x, y in heap]