class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis = []
        star = []

        for i, char in enumerate(s):
            if char == '(':
                parenthesis.append(i)
            elif char == '*':
                star.append(i)
            else:
                if parenthesis:
                    parenthesis.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while parenthesis:
            if not star or parenthesis[-1] > star[-1]:
                return False
            else:
                parenthesis.pop()
                star.pop()
        return True

