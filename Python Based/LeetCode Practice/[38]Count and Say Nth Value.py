# The count-and-say sequence is a sequence of digit strings defined by the recur
# sive formula:
#
#
#  countAndSay(1) = "1"
#  countAndSay(n) is the way you would "say" the digit string from countAndSay(n
# -1), which is then converted into a different digit string.
#
#
#  To determine how you "say" a digit string, split it into the minimal number o
# f groups so that each group is a contiguous section all of the same character. T
# hen for each group, say the number of characters, then say the character. To con
# vert the saying into a digit string, replace the counts with a number and concat
# enate every saying.
#
#  For example, the saying and conversion for digit string "3322251":
#
#  Given a positive integer n, return the nth term of the count-and-say sequence
# .
#
#
#  Example 1:
#
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#
#
#  Example 2:
#
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
#
#
#
#  Constraints:
#
#
#  1 <= n <= 30
#
#  Related Topics String
#  👍 197 👎 636

# ALGO to read a see and say
#         if n == 1:
#             return '1'
#         if n == 2:
#             return '11'
#
#         i = 0
#         result = ''
#         n = str(n)
#         while i < len(n):
#             count = 1
#             while i+1 < len(n) and n[i] == n[i+1]:
#                 i += 1
#                 count += 1
#             result += (str(count) + n[i])
#             i += 1
#         return result
#

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'

        for i in range(2, n + 1):
            res = ''
            cur = output[0]
            count = 1
            for x in output[1:]:
                if x == cur:
                    count += 1
                else:
                    res += str(count) + cur
                    count = 1
                    cur = x

            res += str(count) + cur
            output = ''.join(res)

        return output

# leetcode submit region end(Prohibit modification and deletion)
