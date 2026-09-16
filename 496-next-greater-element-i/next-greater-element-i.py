class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num
            stack.append(num)

        ans = []

        for num in nums1:
            if num in greater:
                ans.append(greater[num])
            else:
                ans.append(-1)

        return ans