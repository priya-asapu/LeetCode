class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i, x in enumerate(nums):
            if x != m and m < 2 * x:
                return -1
        return nums.index(m)