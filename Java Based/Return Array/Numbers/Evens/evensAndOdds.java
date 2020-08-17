import java.util.Arrays;

public class ReturnEvenAndOdds2 {

		public static void main(String[] args) {
			//instantiate array and fill with numbers
			int[] nums = {1, 2, 3, 4, 5};
			System.out.println(Arrays.toString(ReturnEvenAndOdds2.sortArrayByParity(nums)));

		}

	    public static int[] sortArrayByParity(int[] A) {
	        int[] array = new int[A.length];
	        int t = 0;

	        for(int i = 0; i < A.length; i++) {
	            if (A[i] % 2 == 0)
	                array[t++] = A[i];}

	        for (int i = 0; i < A.length; i++) {
	            if (A[i] % 2 == 1)
	                array[t++] = A[i];
	        }
	        return array;
	    }
	}
