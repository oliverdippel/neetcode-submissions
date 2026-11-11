class Solution:
    def isValid(self, s: str) -> bool:
        machting_brackets = {
            "{":"}",
            "[":"]",
            "(":")",
        }

        stack = []

        for i in s:
            if i in machting_brackets:
                stack.append(machting_brackets[i])
            else:
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        
        return not stack