import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #A is shorter array, B is longer array
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        #edge cases
        if not nums1:
            return statistics.median(nums2)
        elif not nums2:
            return statistics.median(nums1)
            
        if A[-1] <= B[0]:
            A.extend(B)
            return statistics.median(A)
        elif B[-1] <= A[0]:
            B.extend(A)
            return statistics.median(B)

        l = 0
        r = len(A) - 1
        valid = False
        half = (len(A) + len(B)) // 2
        m = 0
        n = 0
        while not valid and l < r:
            m = (l + r) // 2
            n = half - (m + 1) - 1

            if A[m] > B[n + 1]:
                r = m - 1
            elif A[m + 1] < B[n]:
                l = m + 1
            else:
                valid = True
        if (len(A) + len(B)) % 2 == 1:
            return max(A[m], B[n])
        return (max(A[m], B[n]) + min(A[m + 1], B[n + 1])) / 2

