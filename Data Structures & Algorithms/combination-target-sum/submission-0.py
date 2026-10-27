class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        stack = []
        
        def backtrack(start, current, current_sum):
            if current_sum == target:
                stack.append(current.copy())
                return
            
            if current_sum > target:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, current_sum+nums[i])
                current.pop()
            
        backtrack(0, [], 0)
        return stack 
