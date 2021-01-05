# You are climbing a staircase. It takes n steps to reach the top.
#
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top?
#
#
#  Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
#  Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
#  Constraints:
#
#
#  1 <= n <= 45
#
#  Related Topics Dynamic Programming
#  👍 5611 👎 178


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n):
        store = {}  # save the data to avoid recalculations

        def helper(n):
            if n == 1 or n == 2:
                return n
            elif n in store:
                return store[n]
            else:
                store[n] = helper(n - 1) + helper(n - 2)
                return store[n]

        return helper(n)

# leetcode submit region end(Prohibit modification and deletion)
