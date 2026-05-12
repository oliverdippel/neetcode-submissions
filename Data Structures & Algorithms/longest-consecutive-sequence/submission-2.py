class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        seen = set()

        for i in set_nums:
            current = i
            seq_len = 0

            if current in seen:
                continue

            while current - 1 in set_nums:
                current -= 1

            while current in set_nums:
                seen.add(current)
                current +=1
                seq_len += 1
 
            longest = max(seq_len, longest)

        return longest 


     