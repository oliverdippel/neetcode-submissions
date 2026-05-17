class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0

        for right, x in enumerate(s):
            while x in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(x)
            longest = max(longest, right-left+1)
        
        return longest 