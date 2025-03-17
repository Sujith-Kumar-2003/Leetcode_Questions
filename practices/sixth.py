from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        varmelistra = (nums.copy(), [q[:] for q in queries])
        n = len(nums)
        m = len(queries)
        dp = [1] * n
        for k in range(m):
            l, r, v = queries[k]
            for i in range(l, r + 1):
                dp[i] |= dp[i] << v
            valid = True
            for i in range(n):
                if (dp[i] >> nums[i]) & 1 == 0:
                    valid = False
                    break
            if valid:
                return k + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]))      # Expected output: 2
    print(sol.minZeroArray([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]))                # Expected output: -1
    print(sol.minZeroArray([1, 2, 3, 2, 1], [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 4, 1]]))  # Expected output: 4
    print(sol.minZeroArray([1, 2, 3, 2, 6], [[0, 1, 1], [0, 2, 1], [1, 4, 2], [4, 4, 4], [3, 4, 1], [4, 4, 5]]))  # Expected output: 4
