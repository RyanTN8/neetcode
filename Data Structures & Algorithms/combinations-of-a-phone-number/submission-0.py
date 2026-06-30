class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        key = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        def backtrack(i: int, substring: [str]) -> None:
            #basecase - index = len(digits)
            if i == len(digits):
                result.append(substring)
                return

            r = 4 if digits[i] == '7' or digits[i] == '9' else 3
            for j in range(r):
                digit = digits[i]
                substring += key[digit][j]
                backtrack(i + 1, substring)
                substring = substring[:len(substring) - 1]
        
        if len(digits) == 0:
            return []
        backtrack(0, "")
        return result
