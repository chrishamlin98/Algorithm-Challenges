/*
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
 */

Deemed not possible or realistic even, using Java... Close case

/*
import java.util.Arrays;

public class TwoSumBrute2
{

public static void main(String[] args) {
    System.out.println(Arrays.toString(twoSum(new int[]{1, 4, 5, 20}, 25)));
}

private static int[] twoSum(int[] v, int target) {
				// this is whats called a base case. It covers a unique
				// outlier that can only happen under these circumstances
				if (v.length <= 1) {
					return null;
				}

        for (int n = 1; n<v.length; n++)
					for (int m = n + 1; m < v.length; m++) {
            if (v[n] + v[m] == target) {
                return new int[] {n, m};
            }
        }
        return new int[] { -1, -1};
    }
}
 */
