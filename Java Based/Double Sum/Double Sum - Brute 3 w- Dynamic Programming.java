import java.util.Arrays;

public class TwoSumBrute3 {

	public static void main(String[] args) {
		int[] vals = { 1, 2, 7, 9, 5, 3, 10 };
		System.out.println(Arrays.toString(twoSum(vals, 0, 1, 15)));
	}

	public static int[] twoSum(int[] v, int n, int m, int target) {
		if (n == v.length) {
			return new int[] { -1, -1 };
		}
		if (m == v.length) {
			return twoSum(v, n + 1, n + 2, target);
		}
		if (v[n] + v[m] == target) {
			return new int[] { n, m };
		}
		return twoSum(v, n, m + 1, target);
	}

}
