# Write a function to find the longest common prefix string amongst an array of
# strings.
#
#  If there is no common prefix, return an empty string "".
#
#
#  Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
#  Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
#  Constraints:
#
#
#  0 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] consists of only lower-case English letters.
#
#  Related Topics String
#  👍 3378 👎 2047


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commons = list(zip(*strs))
        prefix = ""
        for index in commons:
            if len(set(index)) == 1:
                prefix += index[0]
            else:
                break
        return prefix

# leetcode submit region end(Prohibit modification and deletion)
