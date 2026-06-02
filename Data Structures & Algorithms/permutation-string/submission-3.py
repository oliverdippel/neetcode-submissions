class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 

        char_count_s1 = [0] * 26
        char_count_s2 = [0] * 26

        n_s1 = len(s1)

        for char in s1:
            index = ord(char) - ord("a")
            char_count_s1[index] += 1

        for i, char in enumerate(s2):
            index = ord(char) - ord("a")
            char_count_s2[index] += 1

            # Once the window is larger than len(s1),
            # remove the character that falls out of the window.
            if i >= n_s1:
                sub_index = ord(s2[i - n_s1]) - ord("a")
                char_count_s2[sub_index] -= 1

            # Check whether current window matches s1's frequency.
            if char_count_s1 == char_count_s2:
                return True

        return False