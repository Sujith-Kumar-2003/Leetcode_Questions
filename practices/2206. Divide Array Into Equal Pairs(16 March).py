class Solution:
    def divideArray(self, nums) -> bool:
        nums = sorted(nums)
        print(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return False
            i += 2
        return True
