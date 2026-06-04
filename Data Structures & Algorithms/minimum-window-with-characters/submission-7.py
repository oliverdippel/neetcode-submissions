class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        needed_lookup = {}
        storage = {}
        left = 0
        have = 0
        best_len = float("inf")
        ret_left = 0
        ret_right = 0

        for char in t:
            needed_lookup[char] = needed_lookup.get(char, 0) + 1
        
        need = len(needed_lookup)

        for right, char in enumerate(s):
            storage[char] = storage.get(char, 0) + 1

            if char in needed_lookup and needed_lookup[char] == storage[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    ret_left = left
                    ret_right = right 
                
                left_char = s[left]
                storage[left_char] -= 1

                if left_char in needed_lookup and storage[left_char] < needed_lookup[left_char]:
                    have -= 1
                
                left += 1

        return s[ret_left:ret_right + 1] if best_len != float("inf") else ""
            

        