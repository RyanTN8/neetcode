class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [-1] * n

        def dp(i):
            if i >= n:
                return i == n
            if stairs[i] != -1:
                return stairs[i]
            stairs[i] = dp(i + 1) + dp(i + 2)
            return stairs[i]
        return dp(0)