class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i, x in enumerate(nums):
            left, right = i+1, len(nums)-1

            if i > 0 and nums[i-1] == x:
                continue
            
            if x > 0:
                break

            while left < right:
                if nums[left] + nums[right] + x == 0:
                    result.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < len(nums)-1 and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
                elif nums[left] + nums[right] + x > 0:
                    right -= 1
                
                else:
                    left += 1
            
        return result

                
                
                


