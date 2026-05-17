class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
            
        left, right = 0,1 
        max_length = 0

        for i in s[1:]:
            while i in s[left:right]:
                left += 1
            right += 1
            max_length = max(max_length, right-left)

        return max_length
            

        