from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        INF = float('inf')
        ans = [INF] * n

        seen = {}
        for i in range(n):
            j = nums[i]
            if j in seen:
                dist = i - seen[j]
                ans[i] = min(ans[i], dist)
                ans[seen[j]] = min(ans[seen[j]], dist)
            seen[j] = i

        seen = {}
        for i in range(n - 1, -1, -1):
            j = nums[i]
            if j in seen:
                dist = seen[j] - i
                ans[i] = min(ans[i], dist)
                ans[seen[j]] = min(ans[seen[j]], dist)
            seen[j] = i

        pos = {}
        for i, j in enumerate(nums):
            if j not in pos:
                pos[j] = []
            pos[j].append(i)
        for j, indices in pos.items():
            if len(indices) >= 2:
                first, last = indices[0], indices[-1]
                d = first + n - last
                ans[first] = min(ans[first], d)
                ans[last] = min(ans[last], d)

        result = []
        for q in queries:
            result.append(ans[q] if ans[q] != INF else -1)
        return result
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3, 1, 4, 1, 3, 2]
    queries1 = [0, 3, 5]
    print(sol.solveQueries(nums1, queries1))
    nums2 = [1, 2, 3, 4]
    queries2 = [0, 1, 2, 3]
    print(sol.solveQueries(nums2, queries2))
