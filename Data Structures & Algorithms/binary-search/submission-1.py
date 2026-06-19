class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1 #2

        while left <= right:
            mid = (right - left) + left // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # 3
            else:
                right = mid - 1

        return -1  

        # 5 3 
        