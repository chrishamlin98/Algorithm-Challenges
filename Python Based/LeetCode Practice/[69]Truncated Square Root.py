# Given a non-negative integer x, compute and return the square root of x.
#
#  Since the return type is an integer, the decimal digits are truncated, and on
# ly the integer part of the result is returned.
#
#
#  Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
#  Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is
#  truncated, 2 is returned.
#
#
#  Constraints:
#
#
#  0 <= x <= 231 - 1
#
#  Related Topics Math Binary Search
#  👍 1708 👎 2174

# Binary Search method
#         l = 1
#         r = x
#         while l <= r:
#             mid = (l + r) // 2
#             if mid * mid <= x:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#
#         return l - 1


# leetcode submit region begin(Prohibit modification and deletion)
import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return math.trunc(sqrt(x))
# leetcode submit region end(Prohibit modification and deletion)
