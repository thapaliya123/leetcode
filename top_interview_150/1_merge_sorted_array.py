"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        nums1.extend(nums2)

        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                if nums1[i] > nums1[j]:
                    temp = nums1[j]
                    nums1[j] = nums1[i]
                    nums1[i] = temp

        print(nums1)

sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3) # [1,2,2,3,5,6]
sol.merge([1], 1, [], 0) # [1]
sol.merge([0], 0, [1], 1) # [1]