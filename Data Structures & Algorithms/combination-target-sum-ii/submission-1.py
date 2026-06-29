class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i: int, subset: List[int], total: int):
            if total == target:
                result.append(subset[:])
                return
            if i == len(candidates) or total > target:
                return

            subset.append(candidates[i])
            total += candidates[i]
            backtrack(i + 1, subset, total)

            total -= subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, subset, total)
        backtrack(0, [], 0)
        return result