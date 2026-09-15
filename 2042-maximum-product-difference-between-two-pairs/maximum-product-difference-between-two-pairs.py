class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        l = []
        l1 = []
        
        nums.sort()
        
        for i in range(0, 2):
            l.append(nums[i])
        
        for i in range(len(nums)-2, len(nums)):
            l1.append(nums[i])
        
        return (l1[0] * l1[1]) - (l[0] * l[1])