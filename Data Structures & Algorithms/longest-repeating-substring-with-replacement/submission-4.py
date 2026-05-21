class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        max_frequent = longest = 0

        for right in range(len(s)):
            char = s[right]

            seen[char] = seen.get(char, 0) + 1

            max_frequent = max(max_frequent, seen[char])
            window_length = right - left + 1

            if window_length - max_frequent > k:
                seen[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)
        
        return longest








