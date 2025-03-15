class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def hasNeighbours(target):
            count = 0
            i = 0
            while i < N:
                if nums[i] <= target:
                    i += 2
                    count += 1
                    continue
                i += 1
            return count >= k
        left = 0
        right = 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# nums =
# [2,3,5,9]
# k =
# 2
