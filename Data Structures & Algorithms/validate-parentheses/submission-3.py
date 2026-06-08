class Solution:
    def isValid(self, s: str) -> bool:
        look_up = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack = []

        for p in s:
            if p in look_up:
                stack.append(look_up[p])
            else:
                if stack and p == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack

