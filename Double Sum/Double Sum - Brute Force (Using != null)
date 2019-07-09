/*  Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// This a workable solution using a brute force method //

public class twoSumArrayBruteForce {
    public static void main(String[] args) {
        int[] answer = twoSum(new int[]{2, 7, 11, 15}, 9);
        if (answer != null)
            System.out.println("[" + answer[0] + ", " + answer[1] + "]");
    }

    public static int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[i] + numbers[j] == target) return new int[]{ i, j };
            }
        }
        // no answer
        return null;
    }
}
