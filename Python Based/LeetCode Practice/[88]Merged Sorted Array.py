# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
#  sorted array.
#
#  The number of elements initialized in nums1 and nums2 are m and n respectively.
#  You may assume that nums1 has enough space (size that is equal to m + n) to
# hold additional elements from nums2.
#
#
#  Example 1:
#  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#  Example 2:
#  Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
#
#  Constraints:
#
#
#  0 <= n, m <= 200
#  1 <= n + m <= 200
#  nums1.length == m + n
#  nums2.length == n
#  -109 <= nums1[i], nums2[i] <= 109
#
#  Related Topics Array Two Pointers
#  👍 3054 👎 4761


# trial and error
#         for digit in nums1:
#             if digit == 0:
#                 nums1.remove(digit[m])

# This did not work either
#         nums1 = nums1 + nums2
#         nums1.sort()
#
#         remove = [nums1.pop(0) for i in range(m)]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for j in nums2[:n]:
            nums1[m + i] = j
            i += 1
        nums1.sort()

# leetcode submit region end(Prohibit modification and deletion)
