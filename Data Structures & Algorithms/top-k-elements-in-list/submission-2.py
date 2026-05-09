

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            buckets[freq].append(num)

        for bucket in buckets[::-1]:
            for num in bucket:
                result.append(num)

                if len(result) == k:
                    return result