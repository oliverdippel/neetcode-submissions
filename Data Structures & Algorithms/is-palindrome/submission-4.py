class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_string = "".join([x.lower() for x in s if x.isalnum()])

        left, right = 0, len(normalized_string)-1

        while left < right:
            if normalized_string[left] != normalized_string[right]:
                return False
            
            left += 1
            right -= 1

        
        return True
