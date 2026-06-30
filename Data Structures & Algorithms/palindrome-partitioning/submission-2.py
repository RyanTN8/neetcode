class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        result = []

        def backtrack(i: int, j: int, palindromes: List[str]) -> None:
            #base case
            if j == len(s):
                print(palindromes)
                if sum([len(x) for x in palindromes]) == len(s):
                    result.append(palindromes.copy())
                return

            #case 1: substring is palindrome and take palindrome
            flag = False
            if isPalindrome(s[i:j + 1]):
                palindromes.append(s[i:j + 1])
                backtrack(j + 1, j + 1, palindromes)
                flag = True
            #case 2: do not take palindrome
            if flag:
                palindromes.pop()
            backtrack(i, j + 1, palindromes)
        
        backtrack(0, 0, [])
        return result




