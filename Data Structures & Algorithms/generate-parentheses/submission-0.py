class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(subset: List[str], o: int, c: int):
            #base case: more closed than open
            if c > o or len(subset) > n * 2:
                return

            #if filled and o == c, its valid
            if len(subset) == n * 2 and o == c:
                result.append(subset)
                return

            #case 1: open parenthesis
            subset += '('
            backtrack(subset, o + 1, c)

            subset = subset[:len(subset) - 1]

            #case 2: closed parenthesis
            subset += ')'
            backtrack(subset, o, c + 1)
        
        backtrack("", 0, 0)
        return result