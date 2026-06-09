class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(speed: int):
            hours = 0
            for pile in piles:
                hours += -(pile // -speed)
            if hours <= h:
                return True
            return False

        l = 1
        r = max(piles)
        minSpeed = r
        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                minSpeed = min(mid, minSpeed)
                r = mid - 1
            else:
                l = mid + 1
        return minSpeed
