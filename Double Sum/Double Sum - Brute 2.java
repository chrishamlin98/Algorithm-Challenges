import java.util.Arrays;

public class TwoSumBrute2 {

	public static void main(String[] args) {
		System.out.println(Arrays.toString(twoSum(new int[] { 1, 4, 5, 20 }, 25)));
	}

	private static int[] twoSum(int[] v, int target) {
		for (int n = 0; n < v.length; n++)
			for (int m = n + 1; m < v.length; m++) {
				if (v[n] + v[m] == target) {
					return new int[] { n, m };
				}
			}
		return new int[] { -1, -1 };
	}
}
