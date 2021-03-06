/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
problem, assume that your function returns 0 when the reversed integer overflows.
*/

class Solution {
	public int reverse(int x) {
		int x = 1234567, reversed = 0;
		for (; x != 0; x /= 10) {
			int digit = x % 10;
			reversed = reversed * 10 + digit;
		}
		System.out.println(reversed);
	}
}

*********************************

class Solution {
	public int reverse(int x) {
		int x = 1234, reversed = 0;
		while (x != 0) {
			int digit = x % 10;
			reversed = reversed * 10 + digit;
			x /= 10;
		}
		System.out.println(reversed);
	}

}

	/*
	 ********************************
	 * // This one works on leetcode, while the others run as a main method //
	 * 
	 * // However, it does not work for large test cases //
	 */

	public int reverse(int x) {
		int rev_num = 0;
		while (x != 0) {
			rev_num = rev_num * 10 + x % 10;
			x = x / 10;
		}
		return rev_num;
	}
	/*
	 *****************************************
	 * This one works for all test cases; however, I am unsure as to how the program
	 * understands MIN_VALUE... Is it just something built into Java?
	 */

	public class ReverseIntegers {

		public static void main(String[] args) {
			int x = 10795;
			System.out.println(reverse(x));

		}

		public static int reverse(int x) {
			long rev = 0;
			while (x != 0) {
				rev = rev * 10 + x % 10;
				x = x / 10;
			}
			if (rev < Integer.MIN_VALUE || rev > Integer.MAX_VALUE) {
				return 0;
			} else {
				return (int) rev;
			}
		}
	}

	**************************************************

// Leetcode solution //

class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
