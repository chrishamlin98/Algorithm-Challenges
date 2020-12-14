# Given a string, determine if it is a palindrome, considering only alphanumeric
#  characters and ignoring cases.
#
#  Note: For the purpose of this problem, we define empty string as valid palind
# rome.
#
#  Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
#  Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#
#  Constraints:
#
#
#  s consists only of printable ASCII characters.
#
#  Related Topics Two Pointers String
#  👍 1613 👎 3361

## This only works to check for a palindrome, but not for case "abb"
#        s = ''.join(ch.lower() for ch in s if ch.isalnum())
#
#         pal = defaultdict(int)
#         for letter in s:
#             pal[letter] += 1
#
#         odd_count = 0
#         for value in pal.values():
#             if value % 2 != 0:
#                 odd_count += 1
#
#         return odd_count <= 1


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]

# leetcode submit region end(Prohibit modification and deletion)
