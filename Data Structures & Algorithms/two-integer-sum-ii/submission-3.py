class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, 1

        while True:
            while right < len(numbers)-1 and numbers[left] + numbers[right] < target:
                right += 1
            
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            left +=1
            right = left + 1
        