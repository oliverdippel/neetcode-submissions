class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k == 7 -> 1 /// 0-2
        # k == 6 -> 2 /// 1-3
        # k == 5 -> 3 /// 2-4
        # k == 4 -> 4 /// 3-5
        # k == 3 -> 5 /// 4-6
        # k == 2 -> 6 /// 0-2
        # k == 1 -> 7

        output = [float("-inf")] * (len(nums) - k + 1)

        for i, num in enumerate(nums):
            lower = max(0, i - (k-1))
            upper = min(i + 1, len(output))
            for j in range(lower, upper):
                output[j] = max(output[j], num)
        
        return output





        