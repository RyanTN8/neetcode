class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        guide = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in guide.values():
                stack.append(char)
            elif char in guide.keys():
                if stack and stack[-1] == guide[char]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
