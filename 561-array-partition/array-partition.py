class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[::2]
        return sum(a)