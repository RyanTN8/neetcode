class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if (matrix[mid][0] <= target and mid == len(matrix) - 1) or (matrix[mid][0] <= target < matrix[mid + 1][0]):
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        arr = matrix[mid]
        print(arr)
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

