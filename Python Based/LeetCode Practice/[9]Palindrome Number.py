# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
#  Follow up: Could you solve it without converting the integer to a string?
#
#
#  Example 1:
#
#
# Input: x = 121
# Output: true
#
#
#  Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes
#  121-. Therefore it is not a palindrome.
#
#
#  Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
#  Example 4:
#
#
# Input: x = -101
# Output: false
#
#
#
#  Constraints:
#
#
#  -231 <= x <= 231 - 1
#
#  Related Topics Math
#  👍 2823 👎 1656

## My attempt at using a dictionary to store values and return true
# if there are no numbers with stored value 1
#        y = str(x)
#         pal = {}
#         for digit in y:
#             if digit[key] in pal:
#                 value += 1
#             else:
#                 pal.append(key)
#         for key, value in pal.items():
#             if value == 1:
#                 return False
#             else:
#                 return True

# This works for numbers
#         intAsString = str(x)
#         reverse = intAsString[::-1]
#         if reverse == intAsString:
#             return True
#         else:
#             return False

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numberString = str(x)
        palindromeVals = {}

        for digit in numberString:
            if digit in palindromeVals[digit]:
                palindromeVals[digit] += 1
            else:
                palindromeVals[digit] = 1

        if '1' in d.values():
            return False

# leetcode submit region end(Prohibit modification and deletion)
