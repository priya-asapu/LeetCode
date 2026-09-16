class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        for x in nums1:
            found = False

            for i in range(len(nums2)):
                if nums2[i] == x:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > x:
                            ans.append(nums2[j])
                            found = True
                            break
                    break

            if not found:
                ans.append(-1)

        return ans